from django.db import models

# Create your models here.
class ContactBox(models.Model):
    name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    description = models.TextField(max_length = 300)
    created_at = models.DateTimeField(auto_now_add=True)
