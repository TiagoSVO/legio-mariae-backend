from django.forms import ModelForm

from members.models import Member
from .models import WelcomeGuest


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
