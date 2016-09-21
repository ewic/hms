import datetime

from django.db import models

from django.db import models
from django.utils import timezone

'''
Defining EnvironmentalExposures and GeneticMutations as models and attaching
them to the participants via ManyToMany relationships allows us to dynamically
create them and attach them to Participants on the fly.
'''
class EnvironmentalExposure(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()

	def __str__(self):
		return self.name

class GeneticMutation(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()

	def __str__(self):
		return self.name

class Participant(models.Model):
	name = models.CharField(max_length=200)
	birthdate = models.DateField('birthdate')
	siblings = models.BooleanField()
	environmental_exposure = models.ManyToManyField(EnvironmentalExposure)
	genetic_mutation = models.ManyToManyField(GeneticMutation)

	reviewed = models.BooleanField(default=False)
	accepted = models.BooleanField(default=False)

	def __str__(self):
		return self.name

	def getAge(self):
		now = datetime.date.today()
		age = now.year - self.birthdate.year
		return age
	def getEnvironmentalExposures(self):
		ee = self.environmental_exposure.all()
		return ee
	def getGeneticMutations(self):
		gm = self.genetic_mutation.all()
		return gm

	def getStatus(self):
		if (self.reviewed == False):
			return 'new'
		if (self.reviewed == True and self.accepted == False):
			return 'not accepted'
		if (self.reviewed == True and self.accepted == True):
			return 'accepted'