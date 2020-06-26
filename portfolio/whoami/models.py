from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.urls import reverse
from tinymce.models import HTMLField

# Create your models here.
class Me(models.Model):
    image = models.ImageField(upload_to='pictures/')
    title_shortInfo = models.CharField(max_length=200)
    text_shortInfo = models.TextField()
    title_education = models.CharField(max_length=200)
    text_education = models.TextField()
    title_thesis = models.CharField(max_length=200)
    text_thesis = models.TextField()
    title_workExperience = models.CharField(max_length=200)
    text_workExperience = models.TextField()
    title_currentPosition = models.CharField(max_length=200)
    text_currentPosition = models.TextField()
    title_skills = models.CharField(max_length=200)
    text_skills = models.TextField()
    title_codingTechnologies = models.CharField(max_length=200)
    text_codingTechnologies = models.TextField()
    title_hobbies = models.CharField(max_length=200)
    text_hobbies = models.TextField()



    def publish(self):
        self.save()

    def get_absolute_url(self):
        return reverse("whoami:me_detail",kwargs={'pk':self.pk})


    def __str__(self):
        return 'My Info'