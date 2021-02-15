import hashlib
import urllib
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.templatetags.static import static
from django.core.exceptions import ValidationError

from sorl.thumbnail import ImageField, get_thumbnail


def avatar_path(instance, filename):
    """
    Custom avatar path: avatar/u123-12345678.png
    """
    return 'avatar/u{}-{}.{}'.format(
        instance.id,
        int(instance.date_joined.timestamp()),
        filename.split('.')[-1]
    )


class User(AbstractUser):
    date_modified = models.DateTimeField(auto_now=True)
    avatar = ImageField(
        upload_to=avatar_path,
        blank=True,
        null=True,
        default=None
    )
    point = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True, default='')

    def avatar_url(self, size=100):
        """
        If user upload their picture manually, use it. Otherwise generate from default Gravatar image.
        """
        if self.avatar:
            return get_thumbnail(self.avatar, '{}x{}'.format(size, size), crop='center', quality=99).url
        return 'https://www.gravatar.com/avatar/{}?d=retro&f=y&s={}'.format(self.id, size)

    def get_absolute_url(self):
        return reverse('coders:detail', args=[self.username])

    def get_display_name(self):
        return self.user if not self.first_name else self.first_name


class Link(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='link')
    github = models.CharField(
        'Github', max_length=200, blank=True, null=True)
    gitlab = models.CharField(
        'GitLab', max_length=200, blank=True, null=True)
    bitbucket = models.CharField(
        'Bitbucket', max_length=200, blank=True, null=True)
    linkedin = models.CharField(
        'LinkedIn', max_length=200, blank=True, null=True)
    facebook = models.CharField(
        'Facebook', max_length=200, blank=True, null=True)
    twitter = models.CharField(
        'Twitter', max_length=200, blank=True, null=True)
    youtube = models.CharField(
        'Youtube', max_length=200, blank=True, null=True)
    website = models.CharField(
        'Website', max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
