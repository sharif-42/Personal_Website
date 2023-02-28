import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _

from blog.models.post import Post

from django.contrib.auth import get_user_model
User = get_user_model()


class Comment(models.Model):
    uuid = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name=_("UUID"),
        help_text=_("This will be exposed to the outside world."),
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        help_text=_("Related post of this comment."),
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='commentators',
        help_text=_("Owner of this comment."),
        verbose_name=_("Commentator"),
        blank=True,
        null=True,
    )
    parent = models.ForeignKey(
        "self",
        related_name="subcomments",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name=_("Parent Comment"),
        help_text=_("Parent of this comment. If none, this is the Parent comment."),
    )
    name = models.CharField(
        max_length=100,
        blank=True,
        help_text=_("Name of the commentator."),
    )
    email = models.EmailField(
        blank=True,
        help_text=_("Email of the commentator."),
    )
    description = models.TextField(
        help_text=_("Comment Description."),
        verbose_name=_("Comment Description"),
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
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ["-id"]

    def __str__(self):
        if self.user:
            return str(self.post.title) + '-' + str(self.user.full_name)
        elif self.name:
            return str(self.post.title) + '-' + str(self.name)
        elif self.email:
            return str(self.post.title) + '-' + str(self.email)
        else:
            return '-'
