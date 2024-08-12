
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .models import Event
from django.http import JsonResponse
from .form import EventForm

class CalendarView(TemplateView):
    template_name="calendar.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = EventForm()  # Pasar el formulario al contexto
        return context

def eventos_json(request):
    eventos=Event.objects.all()
    eventos_list=[]
    for e in eventos:
        eventos_list.append({
        'id':e.id,
        'title': e.title,
        'initial_date': e.initial_date.strftime('%Y-%m-%dT%H:%M:%S'),
        'final_date': e.final_date.strftime('%Y-%m-%dT%H:%M:%S'),
        'description': e.description
        })
    return JsonResponse(eventos_list,safe=False)  

def create_event(request):
    if request.method=="POST":
        form=EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("calendar")
        return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    return JsonResponse({'success': False}, status=400)

def edit_event(request,pk):
    event=get_object_or_404(Event, pk=pk)
    if request.method=="POST":
        form=EventForm(request.POST,instance=event)
        if form.is_valid():
            form.save()
            return redirect("calendar")
        return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    return JsonResponse({
        'title': event.title,
        'initial_date': event.initial_date.strftime('%Y-%m-%dT%H:%M:%S'),
        'final_date': event.final_date.strftime('%Y-%m-%dT%H:%M:%S'),
        'description': event.description
        },safe=False)

def delete_event(request,pk):
    event=get_object_or_404(Event, pk=pk)
    event.delete()
    return redirect("calendar")