from django.db import models

# model for storing the site settings


class siteSettings(models.Model):
    banner= models.ImageField(upload_to='media/site')
    caption = models.CharField(max_length=100, blank=True, null=True)
 
