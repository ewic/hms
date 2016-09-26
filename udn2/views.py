from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from django.template import RequestContext

from .models import Participant
from .forms import ParticipantForm, ReviewForm

# Default view, lists the participants
def index(request):
	participants = Participant.objects.order_by('name')

	if (request.method=="POST"):
		participant = get_object_or_404(Participant, pk = request.POST.get('participant_id'))
		participant.status = request.POST.get('status')
		participant.save()

	for participant in participants:
		review_form = ReviewForm(instance=participant) 
		participant.form = review_form

	return render(request, 'udn2/index.html', {"participants": participants, })

# Display a single participant for review
def participant(request, participant_id):
	participant = get_object_or_404(Participant, pk = participant_id)
	# Handle the form if saved, which is the review dropdown
	if (request.method=="POST"):
		participant.status = request.POST.get('status')
		participant.save()

	form = ReviewForm(instance=participant)
	return render(request, 'udn2/participant.html', {'participant': participant, 'form': form})

# New model entry form
def form(request):
	if (request.method=="POST"):
		form = ParticipantForm(request.POST)
		title = 'New Participant'
		if form.is_valid():
			p = form.save()
			return redirect('udn2:participant', participant_id=p.id)
	else:
		form = ParticipantForm
		title = 'New Participant'
	return render(request, 'udn2/form.html', {'title': title, 'form': form,})