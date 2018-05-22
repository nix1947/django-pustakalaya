# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext as _
from pustakalaya_apps.collection.models import Collection
from elasticsearch.exceptions import NotFoundError
from .search import VideoDoc
from django.core import urlresolvers
from pustakalaya_apps.core.abstract_models import (
    AbstractItem,
    AbstractSeries,
    AbstractTimeStampModel,
    LinkInfo

)

from pustakalaya_apps.core.models import (
    Keyword,
    Biography,
    Sponsor,
    Publisher,
    Language,
    EducationLevel,
    LicenseType,
    genre_audio_video
)


class FeaturedItemManager(models.Manager):
    def get_queryset(self):
        return super(FeaturedItemManager, self).get_queryset().filter(published="yes", featured="yes").order_by("-updated_date")[:3]


class Video(AbstractItem):
    """
    Video item class
    """

    collections = models.ManyToManyField(
        Collection,
        verbose_name=_("Add this video to these collection"),
        blank=True,

    )

    video_original_document_authors = models.ManyToManyField(
        Biography,
        verbose_name=_("Original Author(s)"),
        related_name="video_original_document_authors",
        blank=True,

    )

    video_release_date = models.CharField(
        verbose_name=_("Release date"),
        max_length=255,
        blank=True,
    )

    video_director = models.ManyToManyField(
        Biography,
        verbose_name=("Director"),
        related_name="directors",
        blank=True,

    )

    video_producers = models.ManyToManyField(
        Biography,
        verbose_name=_("Producer"),
        related_name="producers",
        blank=True,

    )

    education_levels = models.ManyToManyField(
        EducationLevel,
        verbose_name=_("Education Level"),
        blank=True,

    )
    languages = models.ManyToManyField(
        Language,
        verbose_name=_("Languages"),
        blank=True,

    )

    # Manager to return the featured objects.
    objects = models.Manager()
    featured_objects = FeaturedItemManager()

    video_series = models.ForeignKey(
        "VideoSeries",
        verbose_name=_("Video series"),
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    type = models.CharField(
        editable=False,
        default="video",
        max_length=255
    )
    video_certificate_license = models.CharField(
        verbose_name=_("Certification"),
        max_length=255,
        blank=True
    )
    age = models.CharField(
        verbose_name=_("Age group"),
        max_length=255,
        blank=True,
    )

    sponsors = models.ManyToManyField(
        Sponsor,
        verbose_name=_("Sponsor"),
        blank=True,

    )

    # custom video genre inherit from genre_audio_video

    # video_genre = models.ForeignKey(
    #     "VideoGenre",
    #     verbose_name=_("Video Genre"),
    #     blank=True,
    #     null=True
    # )

    video_genre = models.ManyToManyField(
        genre_audio_video,
        verbose_name=_("Video Genre"),
        blank=True,

    )
    # publisher = models.ForeignKey(
    #     Publisher,
    #     verbose_name=_("Publisher"),
    #     blank=True,
    #     null=True
    # )

    publisher = models.ManyToManyField(
        Publisher,
        verbose_name=_("Publisher"),
        blank=True,

    )

    keywords = models.ManyToManyField(
        Keyword,
        verbose_name=_("Keywords"),
        blank=True,

    )

    license = models.ForeignKey(
        LicenseType,
        verbose_name=_("license"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    thumbnail = models.ImageField(
        upload_to="uploads/thumbnails/video/%Y/%m/%d",
        max_length=255,
        blank=True
    )

    video_running_time = models.CharField(
        verbose_name=_("Running time in minutes"),
        max_length=255,
        blank=True,

    )

    @property
    def getauthors(self):
        if not self.video_director:
            return [None]

        return [(author.getName, author.pk) for author in self.video_director.all()] or [None]



    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("video:detail", kwargs={"title": slugify(self.title), "pk": self.pk})

    def doc(self):
        # Parent attr
        item_attr = super(Video, self).doc()
        # Combine item attr and video attr to index in search server
        videoattr = dict(
            **item_attr,
            publisher=[publisher.publisher_name for publisher in self.publisher.all()],
            sponsors=[sponsor.name for sponsor in self.sponsors.all()],  # Multi value # TODO some generators
            keywords=[keyword.keyword for keyword in self.keywords.all()],
            type=self.type,
            education_levels=[education_level.level for education_level in self.education_levels.all()],
            communities=[collection.community_name for collection in self.collections.all()],
            collections=[collection.collection_name for collection in self.collections.all()],
            collections_ids=[collection.pk for collection in self.collections.all()],
            languages=[language.language.lower() for language in self.languages.all()],
            video_running_time=self.video_running_time,
            thumbnail=self.thumbnail.name,
            # License type
            license_type=self.license.license if self.license else None,
            video_director=self.getauthors,#getattr(self.video_director, "getname", ""),
            video_series=getattr(self.video_series, "series_name", ""),
            video_certificate_license=self.video_certificate_license,
            # video_genre=getattr(self.video_genre, "genre", ""),
            video_genre=[video_genre.custom_genre for video_genre in self.video_genre.all()],
            #video_genre=self.video_genre.genre if self.video_genre else None,
            author_list=self.getauthors,
            url = self.get_absolute_url()

        )
        # Create a video  instance
        obj = VideoDoc(**videoattr)
        return obj


    def index(self):
        """
        Call this method to index an instance to search server
        """
        if self.published == "no":
            # delete this if the published is set to no form
            self.delete_index()
        else:
           # save the doc
            self.doc().save()

    def get_admin_url(self):
        return urlresolvers.reverse("admin:%s_%s_change" %(self._meta.app_label, self._meta.model_name), args=(self.pk,))

    def video_title(self):
        return self.title;

    def published_yes_no(self):
        return self.published

    def featured_yes_no(self):
        return self.featured


    def updated_date_string(self):
        return self.updated_date

    def bulk_index(self):
        """
        call this method to during bulk indexing an instance to search server.
        method used by `search.py module`
        """
        return self.doc().to_dict(include_meta=True)

    def delete_index(self):
        """method to delete a video instance from search server
        This method is called by `signals.py` module
        """
        try:
            self.doc().delete()
        except NotFoundError:
            pass

    def __str__(self):
        return self.title

    def get_admin_url(self):
        return urlresolvers.reverse("admin:%s_%s_change" %(self._meta.app_label, self._meta.model_name), args=(self.pk,))



class VideoSeries(AbstractSeries):

    class Meta:
        verbose_name_plural = _("Video series")
        ordering = ["created_date"]

    def __str__(self):
        return "{}".format(self.series_name)


class VideoFileUpload(AbstractTimeStampModel):
    """Class to upload the multiple document objects"""

    file_name = models.CharField(
        _("File name"),
        max_length=255,
        blank=True,
    )

    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE
    )

    upload = models.FileField(
        upload_to="uploads/videos/%Y/%m/",
        max_length=255
    )

    def __str__(self):
        return self.file_name

    class Meta:
        ordering = ["created_date"]


class VideoLinkInfo(LinkInfo):
    video = models.ForeignKey(
        Video,
        verbose_name=_("Link"),
        on_delete=models.CASCADE,

    )

    def __str__(self):
        return self.video.title
    class Meta:
        ordering=["created_date"]


class VideoGenre(AbstractTimeStampModel):
    genre = models.CharField(
        _("Genre name"),
        max_length=255
    )

    genre_description = models.TextField(
        verbose_name=_("Genre description"),
        blank=True
    )

    class Meta:
        db_table = "video_genre"

    def __str__(self):
        return self.genre

