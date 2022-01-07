from django.db.models.base import Model
from django.forms import ModelForm, widgets
from django import forms
from .models import Event, EventData


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['session_id', 'category', 'name',
                    'timestamp']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

        # self.fields['title'].widget.attrs.update(
        #     {'class': 'input'})

        # self.fields['description'].widget.attrs.update(
        #     {'class': 'input'})


class EventDataForm(ModelForm):
    class Meta:
        model = EventData
        fields = ['host', 'path']

    def __init__(self, *args, **kwargs):
        super(EventDataForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
