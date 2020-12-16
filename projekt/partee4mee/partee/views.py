from django.shortcuts import render,redirect, get_object_or_404
from .models import Party
from .forms import PartyForm,SearchingForm
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages




def main(request):
    form = SearchingForm(request.GET)
    total_advertisement = Party.objects.all()
    all_party = Party.objects.all().order_by('date')
    # searching by form
    city = request.GET.get('city', False)
    date = request.GET.get('date', False)
    bfield = request.GET.get('bolean_field', False)
    # city_contains_query,date_query are a var in form in main.html.

    if city and not date:
        all_party = all_party.filter(city =city).order_by('date')
    if city and date:
        all_party = all_party.filter(city =city).filter(date__gte=date).order_by('date')
    if city and date and bfield:
        all_party = all_party.filter(city =city).filter(date__icontains=date).order_by('date')
    if date and bfield:
        all_party = all_party.filter(date__icontains=date).order_by('date')
    if date and not bfield:
        all_party = all_party.filter(date__gt=date).order_by('date')
    

    context = {
        'all':all_party,
        'total':total_advertisement,
        'form':form

    }

    return render(request, "main.html",context)



# requirements to add form: only for logged in users.
@login_required
def add(request):
    form = PartyForm(request.POST or None)
    
    if form.is_valid():
        temporary_form = form.save(commit=False)
        temporary_form.author = request.user
        temporary_form.save()
        return redirect(main)

    return render(request, 'add_party.html', {"form":form}) 


@login_required
def your_account(request):
    user_party_advert = Party.objects.filter(author= request.user)
    user = request.user
    context={
        'user':user,
        'user_party_advert' : user_party_advert,
    }
    return render(request,'accounts.html',context)


def error_site_signed(request):
    context = {
        'message': "This party don't have free places"
    }

    return render(request,'error_signed.html',context)

def access_dismiss(request):
    context = {
        'message': "You don't have access to this data. "
    }

    return render(request,'access_dismiss.html',context)


# zmienic nazwe
def party_signed_up_by_user(request, pk):
    user = request.user
    event = Party.objects.get(pk = pk)

    if user not in event.signed_users.all():
        if event.free_space > 0:
            try:
                event.signed_users.add(user)
                event.free_space -= 1
                event.save()
            except:
                return redirect('login')
        else:
            message = messages.error(request, f'No free spaces available for {event.name} in {event.city}.', extra_tags=str(pk) )
            return redirect(main)

    else:
        print("You were signed up to event")
        return redirect(user_signed_up_events)

    return redirect(user_signed_up_events)


def user_signed_up_events(request):
    user = request.user
    context={
        'signed_up_events' : user.signed_event.all(),
    }

    return render(request, 'signed_up_events.html', context)


# events edit logic
def edit_event(request, id):
    try:
        event = get_object_or_404(Party, pk=id, author=request.user)
    except:
        message = messages.error(request, f"You are not authorized to edit this event.")
        return redirect(user_signed_up_events)
    
    form = PartyForm(request.POST or None, instance=event)

    if form.is_valid():
        form.save()
        return redirect(user_signed_up_events)

    return render(request, 'edit_event.html', {"form": form,'message': 'Ok'})


# edit event from My Event site a redirect to the same site after click Edit button in edit template
def edit_event_2(request, id):
    try:
        event = get_object_or_404(Party, pk=id, author=request.user)
    except:
        return redirect(access_dismiss)
    form = PartyForm(request.POST or None, instance=event)


    if form.is_valid():
        form.save()
        return redirect(your_account)


    return render(request, 'edit_event.html', {"form": form, 'message': 'Ok'})


# user unsubscribe event when click on Sign Off button
def party_signed_off_by_user(request, pk):
    user = request.user
    event = Party.objects.get(pk = pk)

    if user in event.signed_users.all():
            event.signed_users.remove(user)
            event.free_space += 1
            event.save()
            # stworzyc nowy widok na blad jak nie ma miejsc + kolor buttona uzaleznic od ilosci miejsc
    else:
        return redirect(user_signed_up_events)
    
    message = messages.error(request, f"You have been successfully unsubscribed from {event.name} in {event.city}.", extra_tags = str(pk))
    # message = messages.error(request, f"You have been successfully unsubscribed from {event.name} in {date(event.date)}.", extra_tags = str(pk))
    return redirect(user_signed_up_events)


def delete_event_by_user(request, pk):
    event = get_object_or_404(Party, pk=pk, author=request.user)

    if request.method == "POST":
        event.delete()
        return redirect(your_account)

    return render(request, 'delete_event.html', {"event": event})