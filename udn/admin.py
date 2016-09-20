from django.contrib import admin
from .models import Participant, EnvironmentalExposure, GeneticMutation

# The models
admin.site.register(Participant)
admin.site.register(EnvironmentalExposure)
admin.site.register(GeneticMutation)