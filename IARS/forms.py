from django import forms
from .models import Accident, Casualty, Driver, User, location

class LocationForm(forms.ModelForm):
    class Meta:
        model = location
        fields = ['name', 'latitude', 'longitude']

class AccidentForm(forms.ModelForm):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])

    class Meta:
        model = Accident
        fields = [
            'date',
            'location',
            'narration',
            'photo',
            'reason',
            'severity',
            'weather_conditions',
            'road_conditions',
            'VIN',
            'make',
            'model',
            'license_plate',
            'insurance_info',
            'num_casualties',
            'death_count',
            'major_injuries',
            'minor_injuries',
        ]

class CasualtyForm(forms.ModelForm):
    age_group = forms.ChoiceField(choices=Casualty.age_group)
    gender = forms.ChoiceField(choices=Casualty.gender)

    class Meta:
        model = Casualty
        fields = ['age_group', 'gender']

class DriverForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all())
    age_group = forms.ChoiceField(choices=Driver.age_group)
    gender = forms.ChoiceField(choices=Driver.gender)

    def clean(self):
        cleaned_data = super().clean()
        user = cleaned_data.get('user')
        age_group = cleaned_data.get('age_group')
        gender = cleaned_data.get('gender')

        if user and age_group and gender:
            try:
                Driver.objects.get(user=user)
                raise forms.ValidationError('This user already has a driver profile.')
            except Driver.DoesNotExist:
                pass

