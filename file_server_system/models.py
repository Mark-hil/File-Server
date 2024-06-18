from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Document(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=300)
    file = models.FileField(upload_to='documents/', unique=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    download_count = models.IntegerField(default=0)
    email_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title