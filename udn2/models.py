from django.db import models
import datetime
import json

# Create your models here.
class Participant(models.Model):
	name = models.CharField(max_length=200)
	birthdate = models.DateField('birthdate (mm/dd/yyyy')
	siblings = models.BooleanField()

	## Eventually this should be some kind of list structure, so we could
	##   do analytics on them.
	environmental_exposures = models.TextField()
	genetic_mutations = models.TextField()

	status_choices = (
		('new', 'New Entry'),
		('not_accepted', 'Reviewed - Not Accepted'),
		('accepted', 'Reviewed - Accepted'),
	)
	status = models.CharField(
		max_length = 15,
		choices =  status_choices,
		default='new')

	def __str__(self):
		return self.name

	# Age is calculated, because it'd be useful.
	def getAge(self):
		now = datetime.date.today()
		age = now.year - self.birthdate.year
		return age

	# Didn't end up storing these as JSON strings, so not using them
	# Getters for these because Django doesn't support
	#   any native list-like or dictionary-like storage
	#   in SQLite (for now)
	# def getEnvironmentalExposures(self):
	# 	return json.loads(self.environmental_exposures)
	# def getGeneticMustations(self):
	# 	return json.loads(self.genetic_mutations)