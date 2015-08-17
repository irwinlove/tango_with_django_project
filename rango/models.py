from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Category(models.Model):
	"""docstring for Category"""
	name=models.CharField(max_length=128,unique=True)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	slug = models.SlugField(unique=True)
		#null=True,blank=True)
	def save(self, *args, **kwargs):
		if slugify(self.name):
			self.slug = slugify(self.name)
			super(Category, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name
		
class Page(models.Model):
	category=models.ForeignKey(Category)
	title= models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)
	def __unicode__(self):
		return self.title
		pass