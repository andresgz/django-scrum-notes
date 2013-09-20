from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
	user = models.ForeignKey(User, unique=False, null=True)
	project = models.ForeignKey('scrum.Project')
	task = models.CharField(max_length=255)
	comment = models.TextField(blank=True,default='')
	date = models.DateField()
	completed = models.BooleanField(default=False)
	def __unicode__(self):
		return self.project.name +': '+ self.task + ' - ' + self.date.strftime("%m/%d/%Y" )

class Project(models.Model):
	name = models.CharField(max_length=255)	
	def __unicode__(self):
		return self.name