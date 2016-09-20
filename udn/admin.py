from django.contrib import admin
from .models import Participant, EnvironmentalExposure, GeneticMutation

# Register your models here.
admin.site.register(Participant)
admin.site.register(EnvironmentalExposure)
admin.site.register(GeneticMutation)