from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
	message = models.TextField()
	created_by = models.ForeignKey(User, related_name="created_message")
	created_datetime = models.DateTimeField()
	likes = models.PositiveIntegerField(default=0)

	def __unicode__(self):
		return u'%s' % self.message

	class Meta:
		ordering = ['-id']