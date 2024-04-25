from django.shortcuts import render, get_object_or_404
from .models import Event, Brochure

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def brochure_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    brochure = Brochure.objects.get(event=event)
    return render(request, 'events/brochure_detail.html', {'brochure': brochure})
