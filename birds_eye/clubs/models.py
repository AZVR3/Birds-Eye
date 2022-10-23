from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django import template
import misaka as m

# Create your models here.
User = get_user_model()
register = template.Library()

class Group(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    slogan = models.TextField(blank=True, default='')
    slogan_html = models.TextField(editable=False, default='', blank=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User,through="GroupMember")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.slogan = m.html(self.slogan)
        self.description = m.html(self.description)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("clubs:single", kwargs={"slug": self.slug})

    class Meta:
        ordering = ['name']

class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name='memberships', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_groups', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
    class Meta:
        unique_together = ('user', 'group')
