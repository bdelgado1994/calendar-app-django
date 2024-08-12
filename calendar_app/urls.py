from django.urls import path
from .views import CalendarView,eventos_json,create_event,edit_event,delete_event

urlpatterns=[path("",CalendarView.as_view(),name="calendar"),
            path("eventos_json/",view=eventos_json,name="eventos_json"),
            path('create-event/', view=create_event, name='create_event'),
            path('edit-event/<int:pk>/', edit_event ,name='edit_event'),
            path("delete-event/<int:pk>",delete_event,name="delete_event")
            ]