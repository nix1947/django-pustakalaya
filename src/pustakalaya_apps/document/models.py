#  document/models.py
import uuid
import time
import os
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext as _
from elasticsearch.exceptions import NotFoundError
from hitcount.models import HitCount
from hitcount.views import HitCountMixin
from pustakalaya_apps.core.validators import validate_number
from django.core import urlresolvers
from pustakalaya_apps.collection.models import Collection
from pustakalaya_apps.core.abstract_models import (
    AbstractItem,
    AbstractSeries,
    AbstractTimeStampModel,
    LinkInfo
)
from pustakalaya_apps.core.models import (
    Publisher,
    Biography,
    Keyword,
    Sponsor,
    EducationLevel,
    Language,
    LicenseType
)
from .search import DocumentDoc

from django.contrib.contenttypes.models import ContentType
from star_ratings.models import Rating

def __file_upload_path(instance, filepath):
    # Should return itemtype/year/month/filename
    # return instance.type
    # return document/pdf/year/month/filename
    pass


class FeaturedItemManager(models.Manager):
    def get_queryset(self):
        return super(FeaturedItemManager, self).get_queryset().filter(published="yes", featured="yes")[:3]


class Document(AbstractItem, HitCountMixin):
    """Book document type to store book type item
    Child class of AbstractItem
    """

    ITEM_INTERACTIVE_TYPE = (
        ("yes", _("Yes")),
        # ("no", _("No")),
        ("NA", _("Not applicable")),
    )

    DOCUMENT_TYPE = (
        ("book", _("Book")),
        ("working paper", _("Working paper")),
        ("thesis", _("Thesis")),
        ("journal paper", _("Journal paper")),
        ("technical report", _("Technical report")),
        ("article", _("Article")),

    )

    DOCUMENT_FILE_TYPE = (
        ("ppt", _("PPT")),
        ("doc", _("Doc")),
        ("docx", _("Docx")),
        ("pdf", _("PDF")),
        ("xlsx", _("Excel")),
        ("epub", _("Epub")),
        ("rtf", _("Rtf")),
        ("mobi", _("Mobi")),
    )

    collections = models.ManyToManyField(
        Collection,
        verbose_name=_("Add to these collections"),
    )

    document_type = models.CharField(
        _("Document type"),
        max_length=40,  # TODO: Change to match the exact value.
        choices=DOCUMENT_TYPE
    )

    document_file_type = models.CharField(
        _("Document file type"),
        choices=DOCUMENT_FILE_TYPE,
        max_length=23,
        default="pdf"
    )

    document_series = models.ForeignKey(
        "DocumentSeries",
        verbose_name=_("Series"),
        #on_delete=models.CASCADE,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    education_levels = models.ManyToManyField(
        EducationLevel,
        verbose_name=_("Education Levels"),
        blank=True
    )

    languages = models.ManyToManyField(
        Language,
        verbose_name=_("Language(s)")
    )

    document_interactivity = models.CharField(
        verbose_name=_("Interactive"),
        max_length=15,
        choices=ITEM_INTERACTIVE_TYPE,
        blank=True,
        default="NA"
    )

    # This field should be same on all other model to make searching easy in search engine.
    type = models.CharField(
        max_length=255, editable=False, default="document"
    )

    # document_category = models.ForeignKey(
    #     Category,
    #     on_delete=models.CASCADE,
    #     verbose_name=_("Document Category")
    # )

    document_total_page = models.CharField(
        verbose_name=_("Total Pages"),
        blank=True,
        validators=[validate_number],
        max_length=7
    )

    document_authors = models.ManyToManyField(
        Biography,
        verbose_name=_("Author(s)"),
        related_name="authors",
        blank=True,
    )

    # document_authors_name_in_other_language = models.ManyToManyField(
    #     Biography,
    #     verbose_name=_("Author(s) Name in other language"),
    #     related_name="authors_in_other_language",
    #     blank=True,
    # )

    document_editors = models.ManyToManyField(
        Biography,
        verbose_name=_("Editor(s)"),
        related_name="editors",
        blank=True,
    )

    document_translator = models.ManyToManyField(
        Biography,
        verbose_name=_("Translator(s)"),
        related_name="translators",
        blank=True,
    )

    document_illustrators = models.ManyToManyField(
        Biography,
        verbose_name=_("Illustrator"),
        related_name="illustrators",
        blank=True
    )

    # publisher = models.ForeignKey(
    #     Publisher,
    #     verbose_name=_("Publisher name"),
    #     blank=True,
    #     null=True
    # )

    publisher = models.ManyToManyField(
        Publisher,
        verbose_name=_("Publisher name"),
        related_name="publisher",
        blank=True,

    )

    # Better to have plural name
    keywords = models.ManyToManyField(
        Keyword,
        verbose_name=_("Select list of keywords"),
        blank=True


    )


    license = models.ForeignKey(
        LicenseType,
        on_delete=models.SET_NULL,
        verbose_name=_("license"),
        blank=True,
        null=True,

    )

    thumbnail = models.ImageField(
        upload_to="uploads/thumbnails/document/%Y/%m/%d",
        max_length=255,
        blank=True,
        help_text=_("maximum size of thumbnail should be 255px by 300px")
    )

    sponsors = models.ManyToManyField(
        Sponsor,
        verbose_name=_("Sponsor"),
        blank=True,

    )

    submitted_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        editable=False,
        null=True
    )

    # Manager to return the featured objects.
    objects = models.Manager()
    featured_objects = FeaturedItemManager()

    # View count properties.
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')

    class Meta:
        ordering = ('title',)

    @property
    def getauthors(self):
        author_list = [(author.getname, author.pk) for author in self.document_authors.all()]
        return author_list or [None]  # If emtpy, return something otherwise it will break elastic index while searching.

    @property
    def get_view_count(self):
        return self.hit_count_generic.count() or 0


    def get_similar_items(self):
        return Document.objects.filter(keywords__in=[keyword.id for keyword in self.keywords.all()]).distinct()[:12]

    def __str__(self):
        return self.title

    def doc(self):
        """Create and return document object"""

        item_attr = super(Document, self).doc()
        document_attr = dict(
            **item_attr,
            type=self.type,
            education_levels=[education_level.level for education_level in self.education_levels.all()],
            communities=[collection.community_name for collection in self.collections.all()],
            collections=[collection.collection_name for collection in self.collections.all()],
            collections_ids=[collection.pk for collection in self.collections.all()],
            languages=[language.language.lower() for language in self.languages.all()],
            publisher=[publisher.publisher_name for publisher in self.publisher.all()],
            sponsors=[sponsor.name for sponsor in self.sponsors.all()],  # Multi value # TODO some generators
            keywords=[keyword.keyword for keyword in self.keywords.all()],
            # License type
            license_type=self.license.license if self.license else None,
            # Document type specific
            thumbnail=self.thumbnail.name,
            # document_identifier_type=self.document_identifier_type,
            document_file_type=self.document_file_type,
            document_type=self.document_type,
            document_authors=[
                author.getname for author in self.document_authors.all()
                ],
            document_illustrators=[
                illustrator.getname for illustrator in self.document_illustrators.all()
                ],  # Multi value TODO generator
            document_editors=[
                editor.getname for editor in self.document_editors.all()
                ],  # Multi value
            document_translator=[
                translator.getname for translator in self.document_translator.all()
            ],
            document_total_page=self.document_total_page,
            # Document interactivity
            document_interactivity=self.document_interactivity,
            # author with name and id.
            author_list=self.getauthors,
            url=self.get_absolute_url()

        )

        # Create ES Document for indexing
        obj = DocumentDoc(
            **document_attr,
        )

        return obj

    @property
    def get_publisher_name(self):
        """
        Method that return publisher name to index in elastic search server
        If publisher name is None return empty string
        :return:
        """

        if self.publisher is None:
            return " "

        return self.publisher.publisher_name


    def delete_index(self):
        try:
            self.doc().delete()
        except NotFoundError:
            # TODO:
            pass

    def index(self):
        """index or update a document instance to elastic search index server"""
        # Index to index server if any doc is not empty and published status is "yes"
        if self.published == "no":
            # delete this if the published is set to no form
            self.delete_index()
        else:
            #save only when published is yes
            self.doc().save()

        # Print all the collections.
        #print(self.collections)

    def bulk_index(self):
        # Do bulk index if doc item is not empty.
        return self.doc().to_dict(include_meta=True)



    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("document:detail", kwargs={"title": slugify(self.title), "pk": self.pk})

    def get_admin_url(self):
        return urlresolvers.reverse("admin:%s_%s_change" %(self._meta.app_label, self._meta.model_name), args=(self.pk,))

    def document_title(self):
        return self.title

    def published_yes_no(self):
        return self.published

    def featured_yes_no(self):
        return self.featured

    def updated_date_string(self):
        return self.updated_date

    def submited_by(self):
        return self.submitted_by

    def document_link_name(self):
        return self.link_name;


class UnpublishedDocument(Document):
    """
    This is the proxy model of Document,
    Used in admin.py to display the list of unpublished document.
    """
    class Meta:
        proxy = True

class DocumentSeries(AbstractSeries):
    """BookSeries table inherited from AbstractSeries"""

    class Meta:
        verbose_name_plural = _("Document series")

    def __str__(self):
        return self.series_name


def uploadpath(instance, filename):
    directory_path = "uploads/documents/{}/{}_{}/{}".format(
        time.strftime("%Y/%m/%d"),
        "_".join(instance.file_name.split(" ")),
        str(uuid.uuid4())[:8],
        filename
    )
    return directory_path


class DocumentFileUpload(AbstractTimeStampModel):
    """Class to upload the multiple document objects"""

    file_name = models.CharField(
        _("File name"),
        max_length=255,
        blank=True,
        default=""
    )

    document = models.ForeignKey(
        Document,
        on_delete=models.CASCADE
    )

    upload = models.FileField(
        upload_to=uploadpath,
        max_length=255
    )

    total_pages = models.IntegerField(default=0, editable=False)

    def get_files(self):
        images = []
        for i in range(self.total_pages):
            path, file_name = os.path.split(self.upload.url)
            images.append("{}/{}.png".format(path, i))

        return images

    def __str__(self):
        return self.file_name

    class Meta:
        ordering=['created_date']


class DocumentLinkInfo(LinkInfo):
    document = models.ForeignKey(
        Document,
        verbose_name=_("Link"),
        #on_delete=models.CASCADE,

    )

    def __str__(self):
        return self.link_name

    class Meta:
        ordering=['created_date']


class DocumentIdentifier(AbstractTimeStampModel):
    identifier_type = models.CharField(
        verbose_name=_("Identifier Type"),
        max_length=8,
        blank=True,
        choices=(
            ("issn", _("ISSN")),
            ("ismn", _("ISMN")),
            ("govt_doc", _("Gov't Doc")),
            ("uri", _("URI")),
            ("isbn", _("ISBN"))
        )
    )
    identifier_id = models.CharField(
        _("Identifier ID"),
        blank=True,
        max_length=30
    )

    document = models.OneToOneField(
        Document,
        verbose_name=_("document"),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.identifier_type
