from django import forms

from .models import Participant

class ParticipantForm(forms.ModelForm):
	class Meta:
		model = Participant
		fields = ('name', 'birthdate', 'siblings', 'environmental_exposures', 'genetic_mutations')

class ReviewForm(forms.ModelForm):
	class Meta:
		model=Participant
		fields = ('status',)
