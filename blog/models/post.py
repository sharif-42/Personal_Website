import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _

from commons.constant import POST_CATEGORY

from django.contrib.auth import get_user_model
User = get_user_model()

class Post(models.Model):
    uuid = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name=_("UUID"),
        help_text=_("This will be exposed to the outside world."),
    )
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='posts', null=True, blank=True)
    title = models.CharField(
        max_length=200,
        help_text=_('Title of the post.'),
    )
    slug = models.SlugField()
    image = models.ImageField(
        help_text=_('Related image'),
        blank=True,
        null=True
    )
    content = models.TextField(
        help_text=_('Small Details of the post'),
    )
    category = models.CharField(
        max_length=32,
        choices=POST_CATEGORY,
        default='Others',
        help_text=_('Category of the post'),
    )
    created_at = models.DateTimeField(
        help_text=_('Created Date Time'),
        auto_now_add=True,
        null=True
    )
    updated_at = models.DateTimeField(
        help_text=_('Updated Date Time'),
        auto_now=True
    )

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'All Posts'
        ordering = ["-id"]

    def __str__(self):
        return self.title