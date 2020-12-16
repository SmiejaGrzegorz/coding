"""sda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from partee.views import main, add, your_account, party_signed_up_by_user, user_signed_up_events, party_signed_off_by_user,\
    error_site_signed, edit_event, edit_event_2, delete_event_by_user,access_dismiss

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name="main"),
    path('add_party/', add, name="add_event"),
    path('delete_party/<int:pk>', delete_event_by_user, name="delete_event"),
    path('your_account/',your_account , name="your_account"),
    path('signed_up_events/<int:pk>', party_signed_up_by_user, name="party_signed_up_by_user"),
    path('user_signed_up_events/', user_signed_up_events, name="user_signed_up_events"),
    path('user_signed_off_events/<int:pk>', party_signed_off_by_user, name="party_signed_off_by_user"),
    path('error/', error_site_signed, name="error_site_signed"),
    path('access_dismiss/', access_dismiss, name="access_dismiss"),
    path('edit_event/<int:id>/', edit_event, name="edit"),
    path('edit_event_2/<int:id>/', edit_event_2, name="edit_2"),
    path ('accounts/', include('accounts.urls')),
    
]