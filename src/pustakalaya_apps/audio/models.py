from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext as _
from elasticsearch.exceptions import NotFoundError
from django.core import urlresolvers
from pustakalaya_apps.collection.models import Collection
from pustakalaya_apps.core.abstract_models import (
    AbstractItem,
    AbstractTimeStampModel,
    AbstractSeries,
    LinkInfo,
)
from pustakalaya_apps.core.models import (
    Keyword,
    Publisher,
    Biography,
    Sponsor,
    Language,
    EducationLevel,
    LicenseType,
    genre_audio_video
)
from .search import AudioDoc



class FeaturedItemManager(models.Manager):
    def get_queryset(self):
        return super(FeaturedItemManager, self).get_queryset().filter(featured="yes", published="yes").order_by("-updated_date")[:5]



class Audio(AbstractItem):
    """Audio class to store audio"""

    audio_types = models.ManyToManyField(
        "AudioType",
        verbose_name=_("Audio types"),
        blank=True,

    )

    collections = models.ManyToManyField(
        Collection,
        verbose_name=_("Add this audio to these collection"),
        blank=True,

    )

    type = models.CharField(
        default="audio",
        max_length=255,
        editable=False
    )
    audio_running_time = models.CharField(
        verbose_name=_("Running time in minutes"),
        max_length=255,
        blank=True,
    )

    # TODO file size
    # Like that format the given no in MB, KB, GB for entered MB size

    audio_original_document_authors = models.ManyToManyField(
        Biography,
        verbose_name=_("Original Author(s)"),
        related_name="audio_original_document_authors",
        blank=True,

    )

    audio_release_date = models.CharField(
        verbose_name=_("Release date"),
        max_length=255,
        blank=True,
    )

    audio_read_by = models.ManyToManyField(
        Biography,
        verbose_name=_("Read / Voice by"),
        related_name="audio_read_by",
        blank=True,

    )

    # publisher = models.ForeignKey(
    #     Publisher,
    #     verbose_name=_("Audio publisher"),
    #     blank=True,
    #     null=True
    # )

    publisher = models.ManyToManyField(
        Publisher,
        verbose_name=_("Audio publisher"),
        blank=True,

    )

    # Manager to return the featured objects.
    objects = models.Manager()
    featured_objects = FeaturedItemManager()

    keywords = models.ManyToManyField(
        Keyword,
        verbose_name=_("Select list of keywords"),
        blank=True,

    )

    license = models.ForeignKey(
        LicenseType,
        verbose_name=_("license"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True

    )
    #genre_audio_video

    # audio_genre = models.ForeignKey(
    #     "AudioGenre",
    #     verbose_name=_("Audio Genre"),
    #     blank=True,
    #     null=True
    # )
    audio_genre = models.ManyToManyField(
        genre_audio_video,
        verbose_name=_("Audio Genre"),
        blank=True,

    )

    languages = models.ManyToManyField(
        Language,
        verbose_name=_("Languages"),
        blank=True,

    )

    education_levels = models.ManyToManyField(
        EducationLevel,
        verbose_name=("Education Levels"),
        blank=True,

    )

    audio_series = models.ForeignKey(
        'AudioSeries',
        verbose_name=_("Series"),
        blank=True,
        null=True
    )

    sponsors = models.ManyToManyField(
        Sponsor,
        verbose_name=_("Sponsor"),
        blank=True,

    )

    thumbnail = models.ImageField(
        upload_to="uploads/thumbnails/audio/%Y/%m/%d",
        max_length=255,
        blank=True

    )

    @property
    def getauthors(self):
        if not self.audio_read_by.all():
            return None

        return [(author.getName, author.pk) for author in self.audio_read_by.all()] or [None]




    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("audio:detail", kwargs={"title": slugify(self.title), "pk": self.pk})

    def doc(self):
        # Parent attributes
        item_attr = super(Audio, self).doc()
        # Audio attributes
        audio_attr = dict(
            **item_attr,
            publisher=[publisher.publisher_name for publisher in self.publisher.all()],
            sponsors=[sponsor.name for sponsor in self.sponsors.all()],  # Multi value # TODO some generators
            keywords=[keyword.keyword for keyword in self.keywords.all()],
            audio_types=[audio.name for audio in self.audio_types.all()],
            type=self.type,
            education_levels=[education_level.level for education_level in self.education_levels.all()],
            communities=[collection.community_name for collection in self.collections.all()],
            collections=[collection.collection_name for collection in self.collections.all()],
            collections_ids=[collection.pk for collection in self.collections.all()],
            languages=[language.language.lower() for language in self.languages.all()],
            audio_running_time=self.audio_running_time,
            thumbnail=self.thumbnail.name,

            # License type
            license_type=self.license.license if self.license else None,
            audio_read_by= self.getauthors,
            # audio_genre=self.audio_genre.genre if self.audio_genre else None,
            audio_genre=[audio_genre.custom_genre for audio_genre in self.audio_genre.all()],
            audio_series=self.audio_series.series_name if self.audio_series else None,
            author_list = self.getauthors,
            url = self.get_absolute_url()

        )

        obj = AudioDoc(
            **audio_attr
        )

        return obj

    def index(self):
        """index an instance of audio to elastic search index server"""
        if self.published == "no":
            # delete this if the published is set to no form
            self.delete_index()
        else:
            # save only when published is yes
            self.doc().save()

    def bulk_index(self):
        return self.doc().to_dict(include_meta=True)

    def get_admin_url(self):
        return urlresolvers.reverse("admin:%s_%s_change" %(self._meta.app_label, self._meta.model_name), args=(self.pk,))

    def audio_title(self):
        return self.title;

    def published_yes_no(self):
        return self.published

    def featured_yes_no(self):
        return self.featured

    def updated_date_string(self):
        return self.updated_date

    def delete_index(self):
        try:
            self.doc().delete()
        except NotFoundError as e:
            pass

    def __str__(self):
        return self.title

    class Meta:
        db_table = "audio"




class AudioGenre(AbstractTimeStampModel):
    genre = models.CharField(
        _("Genre name"),
        max_length=255,
    )

    genre_description = models.TextField(
        verbose_name=_("Genre description"),
        blank=True,
    )

    class Meta:
        db_table = "audio_genre"

    def __str__(self):
        return self.genre


class AudioSeries(AbstractSeries):
    def __str__(self):
        return "{}".format(self.series_name)

    class Meta:
        db_table = "audio_series"

from django import forms
class AudioFileUpload(AbstractTimeStampModel):
    """Class to upload the multiple document objects"""

    file_name = models.CharField(
        _("File name"),
        max_length=255,
        blank=True,
        #widget=forms.CharField(attrs={'placeholder': 'Less then 255 chars'})


    )

    audio = models.ForeignKey(
        Audio,
        on_delete=models.CASCADE
    )

    upload = models.FileField(
        upload_to="uploads/audio/%Y/%m/",
        max_length=255
    )

    def __str__(self):
        return self.file_name

    class Meta:
        db_table = "audio_file"
        ordering = ["created_date"]


class AudioLinkInfo(LinkInfo):
    audio = models.ForeignKey(
        Audio,
        verbose_name=_("Link"),
        on_delete=models.CASCADE,

    )

    def __str__(self):
        return self.audio.title

    class Meta:
        ordering=["created_date"]


class AudioType(models.Model):
    """DB to store type of audios"""
    AUDIO_TYPES = (
        ('rhymes', _('Rhymes')),
        ('novel', _('Novel')),
        ('short story', _('Short Story')),
        ('children song', _('Children Song')),
    )

    name = models.CharField(
        verbose_name=_("Audio type"),
        max_length=255,
    )

    description = models.TextField(
        verbose_name=_("Audio description"),
        blank=True
    )

    def __str__(self):
        return self.name
