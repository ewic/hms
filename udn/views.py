from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from django.template import RequestContext

from .models import Participant
from .forms import ParticipantForm, EeForm, GmForm, ReviewForm

# Default view, probably just links to the form and list.
def index(request):
	participant_list = Participant.objects.order_by('name')
	return render(request, 'udn/index.html', {'list': participant_list, 'request': request})

# New model entry form
def form(request, form_type):
	if (request.method=="POST"):
		message = 'Added new participant'
		form = ParticipantForm(request.POST)
		title = 'New Participant'
		if form.is_valid():
			p = form.save()
			return participant(request, participant_id=p.id)
	else:
		message = ''
		if (form_type == 'p'):
			form = ParticipantForm
			title = 'New Participant'
		elif (form_type == 'gm'):
			form = GmForm
			title = 'New Genetic Mutation'
		elif (form_type == 'ee'):
			form = EeForm
			title = 'New Environmental Exposure'
		else:
			message = 'Invalid form type'
	return render(request, 'udn/form.html', {'title': title, 'form': form, 'message': message})

# List of all participants
def list(request):
	participant_list = Participant.objects.order_by('name')
	return render(request, 'udn/list.html', {'list': participant_list})

# Display a single participant for review
def participant(request, participant_id):
	participant = get_object_or_404(Participant, pk = participant_id)
	# Handle the form if saved
	if (request.method=="POST"):
		form = ReviewForm(request.POST)
		if form.is_valid():
			# Fill in the missing data, since the review form only knows about
			#   the reviewed and accepted status

			print(form)

			participant.reviewed = form.fields['reviewed']
			participant.accepted = form.fields['accepted']
			# Save the model
			participant.save()
	else:
		form = ReviewForm
	return render(request, 'udn/participant.html', {'participant': participant, 'form': ReviewForm})

## MAYBE THIS WILL BE USEFUL IF THIS WERE NOT JUST A CODE TEST BUT IDK I DON'T WANT TO JUST DELETE IT ALL
# Uhhhh, I don't think we need these but... for the future

# Display a single environmental exposure
def ee(request, environmentalexposure_id):
	environmentalexposure = get_object_or_404(environmentalexposure, pk = environmentalexposure_id)
	return render(request, 'udn/environmentalexposure.html', {'environmentalexposure': environmentalexposure})
 
# Display a single genetic mutation
def gm(request, geneticmutation_id):
	geneticmutation = get_object_or_404(geneticmutation, pk = geneticmutation_id)
	return render(request, 'udn/geneticmutation.html', {'geneticmutation': geneticmutation})
