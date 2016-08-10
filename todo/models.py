from django.db import models

# Create your models here.

class Todo(models.Model):
	todo = models.CharField(max_length=50)
	priority = models.CharField(max_length=2)

	def __str__(self):
		return u'%s' % (self.todo)

	class Meta:
		ordering = ['priority']
