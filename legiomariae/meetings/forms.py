from django.forms import ModelForm

from members.models import Member
from .models import WelcomeGuest, MinuteMeetingReaded, MinuteMeeting


class WelcomeGuestForm(ModelForm):
    class Meta:
        model = WelcomeGuest
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(WelcomeGuestForm, self).__init__(*args, **kwargs)
        welcome_member_field = self.fields['welcome_member']
        meeting = self.fields['meeting'].queryset.first()
        organization_from_meeting = meeting.organization
        welcome_member_queryset = Member.objects.filter(memberfiliation__organization=organization_from_meeting.id)

        welcome_member_field.queryset = welcome_member_queryset


class MinuteMeetingReadedForm(ModelForm):
    class Meta:
        model = MinuteMeetingReaded
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MinuteMeetingReadedForm, self).__init__(*args, **kwargs)
        minute_field = self.fields['minute']
        meeting = self.fields['meeting'].queryset.first()
        organization_from_meeting = meeting.organization
        minute_queryset = MinuteMeeting.objects.filter(meeting__organization=organization_from_meeting.id)

        minute_field.queryset = minute_queryset
