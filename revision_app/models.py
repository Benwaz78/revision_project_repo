from django.db import models
# Create your models here.

class About(models.Model):
	name = models.CharField(max_length=100)
	about_img = models.ImageField(verbose_name='About Image', blank=True, null=True)
	about_desc = models.TextField(verbose_name='About Description')

	def __str__(self):
		return self.name

class Service(models.Model):
	service_title = models.CharField(max_length=100)
	service_desc = models.TextField(verbose_name='Service Description')

	def __str__(self):
		return self.service_title
