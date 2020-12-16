from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm
from django.contrib import messages



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Witamy na portalu')
                else:
                    return HttpResponse('Konto jest zablokowane')
            else:
                return HttpResponse( 'Nieprawidłowe dane uwierzytelniające')
    else:
        form = LoginForm()
        return render(request, 'registration/login.html', {'form':form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'])
            new_user.save()
            message = messages.success(request, "Your account was succesfully created" )
            return render(request,
                            'register.html',
            {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                    'register.html',
                    {'user_form': user_form })

