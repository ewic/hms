from django import forms

from .models import Participant

class ParticipantForm(forms.ModelForm):
	class Meta:
		model = Participant
		fields = ('name', 'birthdate', 'siblings', 'environmental_exposure', 'genetic_mutation')

class ReviewForm(forms.ModelForm):
	class Meta:
		model = Participant
		fields = ('reviewed', 'accepted')

class EeForm(forms.Form):
	nameField = forms.CharField(label='Name', max_length=200)
	descriptionField = forms.MultiValueField()

class GmForm(forms.Form):
	nameField = forms.CharField(label='Name', max_length=200)
	descriptionField = forms.MultiValueField()