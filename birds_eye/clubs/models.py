from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Member(models.Model):
    name = models.CharField(max_length=200, verbose_name="Student Name", help_text="Enter the student name")
    id = models.IntegerField(primary_key=True, verbose_name="Student ID", help_text="ID of the student")

    def __int__(self):
        return self.id

class Club(models.Model):
    name = models.CharField(max_length=100, unique=True)
    id = models.AutoField(primary_key=True)
    slogan = models.TextField(max_length=70)
    description = models.TextField(blank=True, null=True)
    member = models.ManyToManyField(Member, help_text="Select a student to join the club")

    class Meta:
        ordering = ['name', 'slogan']

    def display_member(self):
        return ', '.join([member.name for member in self.member.all()[:3]])

    display_member.short_description = "Member"

    def get_absolute_url(self):
        return reverse('clubs:club-detail', args=[str(self.id)])

    def __str__(self):
        return self.name