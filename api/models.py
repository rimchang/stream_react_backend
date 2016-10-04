from django.db import models
from django.utils import timezone
#from django.template.defaultfilters import slugify
#for utf-8 encoding
from slugify import slugify
from django.db.models import F
from django.contrib.auth.models import User
from django.forms.fields import ImageField


from actstream import action
from actstream.actions import follow, unfollow

class BaseModel(models.Model):
	created_at= models.DateTimeField(auto_now_add=True)
	modified_at= models.DateTimeField(auto_now=True)
	class Meta:
		abstract = True
	
class Comment(BaseModel):
	user_id = models.ForeignKey('auth.User') 
	upload_id= models.ForeignKey('api.Upload', blank=True, null=True,related_name='comments')
	comment = models.TextField(null=False,max_length=500)
	
	def save(self, *args, **kwargs):
		action.send(self.user_id, verb='comment',target=self.upload_id)
		super(Comment, self).save(*args, **kwargs)
		
class Follow(BaseModel):
	user_id = models.ForeignKey('auth.User', related_name='friends') 
	follower_id = models.ForeignKey('auth.User', related_name='followers')
	
	class Meta:
		unique_together = ('user_id', 'follower_id',)
		
	def save(self, *args, **kwargs):
		follow(self.user_id, self.follower_id)
		super(Follow, self).save(*args, **kwargs)

	def delete(self, *args, **kwargs):
		unfollow(self.user_id, self.follower_id)
		super(Follow, self).delete(*args, **kwargs)
		
class Like(BaseModel):
	user_id = models.ForeignKey('auth.User') 
	upload_id = models.ForeignKey('Upload', blank=True, null=True)
	class Meta:
		unique_together = ('user_id', 'upload_id',)
		
	def save(self, *args, **kwargs):
		action.send(self.user_id, verb='like',target=self.upload_id)
		super(Like, self).save(*args, **kwargs)
		
class Search(BaseModel):
	user_id = models.ForeignKey('auth.User') 
	search_text = models.TextField(null=False)

class Upload(BaseModel):
	user_id = models.ForeignKey('auth.User')
	image_file = models.ImageField(upload_to='original/%Y/%m/%d')
	caption = models.TextField(max_length=500, blank=True)
	location = models.CharField(max_length=120)
	latitude = models.FloatField()
	longitude = models.FloatField()
	
	# for self refrence after save to do action.save
	def save(self, *args, **kwargs):
		self.create_hashtags()
		super(Upload, self).save(*args, **kwargs)
		action.send(self.user_id, verb='upload',target=self)

		
	def create_hashtags(self):
		hashtag_set = set(self.parse_hashtags())
		for hashtag in hashtag_set:
			h, created = Hashtag.objects.get_or_create(name=hashtag)
			h.save()
		Hashtag.objects.filter(name__in=hashtag_set).update(occurrences=F('occurrences')+1)
        
	def parse_hashtags(self):
		return [slugify(i)  for i in self.caption.split() if i.startswith("#")]
		
class Hashtag(models.Model):
    name = models.CharField(max_length=160)
    occurrences = models.IntegerField(default=0)
    