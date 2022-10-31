from django.shortcuts import render
from django.http import JsonResponse

from .models import Meeting


def generate_minute_meeting(request, meeting_id):
    meeting_id = int(meeting_id)
    meeting = Meeting.objects.filter(id=meeting_id)[0]
    minute = meeting.minutemeeting

    data = {'meeting_text': minute.create_minute_meeting(meeting_id)}

    return JsonResponse(data, safe=False)



