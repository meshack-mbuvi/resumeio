from django.db import models
from django.contrib.auth.models import User


class TemplateCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class ResumeTemplate(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to='resume_templates', verbose_name='template_image')
    category = models.ForeignKey(
        TemplateCategory,
        on_delete=models.CASCADE,
        related_name='category'
    )

    def __str__(self):
        return self.name


class PersonalDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField( max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    job_title = models.TextField(default='', null=True, blank=True)
    phone = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        return self.user.username

