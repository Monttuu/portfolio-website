from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Project(models.Model):
    #author = models.ForeignKey('auth.User',related_name='my_projects',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    description = models.TextField(default="Description")
    image = models.ImageField(upload_to='pictures/')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("my_projects:project_detail",kwargs={'pk':self.pk})


    def __str__(self):
        return self.title
