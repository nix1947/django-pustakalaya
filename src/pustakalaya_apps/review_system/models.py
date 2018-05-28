from django.db import models
from django.contrib.auth.models import User
import uuid


class Review(models.Model):
    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # object_id = models.PositiveIntegerField()
    # content_object = GenericForeignKey('content_type', 'object_id')

    content_type = models.CharField(max_length=20, null=True,editable=False)
    content_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=False)

    user = models.ForeignKey(User)
    title = models.CharField(max_length=255, null=True)
    post = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    published = models.BooleanField(default=False)


    class Meta:
        ordering = ['-created']
        #proxy = True

    def __str__(self):
        return 'Comment by {} on {}'.format(self.user, self.post)

