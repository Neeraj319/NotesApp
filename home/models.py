from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify
import random
# Create your models here.


class Notes(models.Model):
    # notes model
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    content = models.TextField()
    slug = models.SlugField(blank=True, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.title}-{self.id}')
        super(Notes, self).save(*args, **kwargs)

    def __str__(self):
        return f'note of {self.user}'
