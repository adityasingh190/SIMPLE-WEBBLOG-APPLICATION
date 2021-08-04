from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse #to use get_absolute_url
from django.db.models.signals import pre_save # to implement slug (a dynamic name for posts not just the id)

from django.utils.text import slugify # to import slugify
# Create your models here.


def upload_location(instance, filename):
	return "%s/%s"%(instance.id , filename)


class Post(models.Model):
	
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1) #imp
	title = models.CharField(max_length=120)
	slug = models.SlugField(unique=True)
	image = models.ImageField(upload_to=upload_location,
	null = True,blank = True,
	height_field="height_field",
	width_field="width_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	content = models.TextField()
	
	updated = models.DateTimeField(auto_now = True, auto_now_add = False) #auto_now = True coz it needs to be updated
	timestamp = models.DateTimeField(auto_now =False, auto_now_add = True) #auto_now = False coz it doesnt need to be updated,its the time when post was created

	def __unicode__(self): #in python 3 __str __ is used
		return self.title

	def get_absolute_url(self): #it can be used in a href in html
		return reverse("posts:detail", kwargs={"slug":self.slug})

def create_slug(instance, new_slug=None): # slug implementation
	slug = slugify(instance.title)
		#"Tesla item 1" --> "tesla-item-1"

	if new_slug is not None:
		slug = new_slug
	qs = Post.objects.filter(slug=slug).order_by("-id")
	exists=qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug =new_slug)
	return slug 


def pre_save_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)
		


 

pre_save.connect(pre_save_post_receiver, sender=Post)
		
