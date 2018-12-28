from django.db import models

# Create your models here.

class Page(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)

    def __str__(self):
        return self.name
