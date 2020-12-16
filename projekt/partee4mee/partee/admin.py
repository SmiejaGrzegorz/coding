from django.contrib import admin
from .models import PartyType, Party

admin.site.register(PartyType)
# admin.site.register(Party)

@admin.register(Party)
class AdminParty(admin.ModelAdmin):
    list_display = ['description','author', 'id']
    ordering = ['author','id']