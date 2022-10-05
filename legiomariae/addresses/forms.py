from django import forms
from django.contrib import admin
from .models import City, State


class AddressForm(forms.ModelForm):
    # Field used by javascript script
    fieldset_address_id = forms.CharField(widget=forms.HiddenInput, required=False)

    class Meta:
        pass

    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)

        # Force the insertion of the field fieldset_address_id to working in javascript
        if hasattr(self, 'fieldsets'):
            if self.fieldsets:
                if not self.fieldsets[0][1]['fields']['fieldset_address_id']:
                    self.fieldsets[0][1]['fields'] += ['fieldset_address_id']

        self.fields['fieldset_address_id'].initial = f'{self.prefix.split("-")[0]}_combobox'

        if self.instance:
            try:
                if self.fields.get('country', None):
                    self.fields['country'].initial = self.instance.country.id
                if self.fields.get('state', None):
                    self.fields['state'].initial = self.instance.state.id
                    self.fields['state'].widget.choices.queryset = State.objects.filter(country=self.instance.country.id)
                if self.fields.get('city', None):
                    self.fields['city'].initial = self.instance.city.id
                    self.fields['city'].widget.choices.queryset = City.objects.filter(state=self.instance.state.id)
            except:
                # pass
                country_id = 0
                state_id = 0
                city_id = 0
                if kwargs.get('data', None):
                    country_id = int(kwargs['data'][self.prefix+'-country'])
                    state_id = int(kwargs['data'][self.prefix+'-state'])
                    city_id = int(kwargs['data'][self.prefix+'-city'])

                if self.fields.get('state', None):
                    self.fields['state'].initial = state_id
                    self.fields['state'].widget.choices.queryset = State.objects.filter(country=country_id)
                if self.fields.get('city', None):
                    self.fields['city'].initial = city_id
                    self.fields['city'].widget.choices.queryset = City.objects.filter(state=state_id)

    class Media:
        # Alter these paths depending on where you put your media
        js = (
            'js/combobox_address.js',
        )


class StackedAddressForm(admin.StackedInline):
    form = AddressForm

    def __init__(self, *args, **kwargs):
        super(StackedAddressForm, self).__init__(*args, **kwargs)

        if hasattr(self, 'fieldsets'):
            if self.fieldsets:
                if not self.fieldsets[0][1]['fields']['fieldset_address_id']:
                    self.fieldsets[0][1]['fields'] += ['fieldset_address_id']

        if hasattr(self, 'fields'):
            if self.fields:
                if 'fieldset_address_id' not in self.fields:
                    self.fields += ['fieldset_address_id']