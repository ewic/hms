from django.db import models

from django.db import models
from django.utils import timezone

# Create your models here.
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

	def __str__(self):
		return self.name

	def getAge(self):
		now = datetime.datetime.now()
		age = now.year - self.birthdate.year
		return age

