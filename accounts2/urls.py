from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.list_events, name='list_events'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('register/', views.register_event, name='register_event'),
]
