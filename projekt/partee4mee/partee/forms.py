from django.forms import ModelForm
from .models import Party
from django import forms

class PartyForm(forms.ModelForm): 
    
    class Meta:
        model = Party  
        fields = ["name","date", "city", "party_type", "free_space",
        "description","signed_users"]
    
        widgets = {
            'name': forms.TextInput(attrs= {'placeholder': 'Title of event'}),
            'date': forms.TextInput(attrs={'placeholder': 'rrrr-mm-dd'}),
            'city': forms.TextInput(attrs={'placeholder': 'Enter your city'}),
            'free_space': forms.TextInput(attrs={'placeholder': 'Enter free places..'}),
            'description': forms.Textarea(attrs={'placeholder': 'Write something about this event..',
            'rows':1, 'cols':15}),
        }

        labels = {
            'signed_users': 'Invite your friends'
        }

class SearchingForm(forms.Form):
    # date = forms.DateField(required=False, label= 'Date', widget= forms.SelectDateWidget)

    date = forms.DateField(required=False, label= 'Date', widget=forms.TextInput(attrs={
        'class':'form-control',
        'type': 'date'
    }))

    city = forms.CharField(max_length = 20, required = False, label='City', widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'Enter your city..',
        }))

    bolean_field = forms.BooleanField(required=False, label= 'Exact date',help_text='Search only this date')












