from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Password again',
                               widget= forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

# ????????????????? @Ewa - errors

    # def clean_password(self):
    #     cd = self.cleaned_data
    #     if cd['password'] != cd['password2']:
    #         raise forms.ValidationError('Hasłą nie są identyczne.')
    #     return cd['password2']