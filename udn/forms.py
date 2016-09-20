from django import forms

class ParticipantForm(forms.Form):
	nameField = forms.CharField(label='Name',max_length=200)
	birthdateField = forms.DateField(label='Birthdate')
	siblings = forms.BooleanField(label='siblings')

class ReviewForm(forms.Form):
	reviewedField = forms.BooleanField(label='Reviewed?')
	acceptedField = forms.BooleanField(label='Accepted?')

class EeForm(forms.Form):
	nameField = forms.CharField(label='Name', max_length=200)
	descriptionField = forms.MultiValueField()

class GmForm(forms.Form):
	nameField = forms.CharField(label='Name', max_length=200)
	descriptionField = forms.MultiValueField()