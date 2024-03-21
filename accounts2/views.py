from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Event, Participant, Registration
from .serializers import EventSerializer, ParticipantSerializer, RegistrationSerializer
from django.utils import timezone

@api_view(['GET'])
def list_events(request):
    events = Event.objects.all()
    data = []
    for event in events:
        event_data = {
            'id': event.id, 
            'name': event.name,
            'description': event.description,
            'date': event.date,
            'time': event.time,
        }
        data.append(event_data)
    return Response(data)


@api_view(['GET'])
def event_detail(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = EventSerializer(event)
    return Response(serializer.data)

@api_view(['POST'])
def register_event(request):
    data = request.data
    event_id = data.get('event_id')
    participant_data = data.get('participant')

    try:
        event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        print("Event not found")
        return Response({"message": "Event not found"}, status=status.HTTP_404_NOT_FOUND)

    participant_serializer = ParticipantSerializer(data=participant_data)
    if participant_serializer.is_valid():
        participant = participant_serializer.save()
        print("Participant created:", participant) 
    else:
        print("Participant data is not valid:", participant_serializer.errors)
        return Response(participant_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if event.date < timezone.now().date():
        print("Event date has already passed")
        return Response({"message": "Event date has already passed"}, status=status.HTTP_400_BAD_REQUEST)

    registration = Registration(event=event, participant=participant)
    registration.save()

    print("Registration successful for event:", event) 
    print("Participant:", participant)  
    return Response({"message": "Registration successful"}, status=status.HTTP_201_CREATED)
