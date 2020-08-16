from django.db import models

# Create your models here.

class Create(models.Model) : 
    title = models.CharField(max_length=50)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
