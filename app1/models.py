from django.db import models
from django.utils.html import mark_safe
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length = 30)
    price = models.CharField(max_length = 30)
    islike = models.BooleanField(default = False)
    image = models.ImageField(upload_to='images/')

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.image))
    image_tag.short_description = 'Image'

    def __str__(self) -> str:
        return self.name
