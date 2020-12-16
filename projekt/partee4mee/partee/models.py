from django.db.models import Model, CharField, DateTimeField, TextField, SmallIntegerField, ForeignKey, DO_NOTHING,CASCADE, ManyToManyField
from datetime import datetime
from django.contrib.auth.models import User

class PartyType(Model):
    type = CharField(max_length=50)

    def __str__(self):
        return f"{self.type}"


class Party(Model):

    date = DateTimeField(null=False, blank=False)
    name = TextField(max_length=75, null=True)
    city = CharField(max_length=50)
    party_type = ForeignKey(PartyType, on_delete = DO_NOTHING)
    free_space = SmallIntegerField(null = True)
    description = TextField(max_length=100)
    author = ForeignKey(User, on_delete= CASCADE)
    create_date = DateTimeField(auto_now_add=True)
    signed_users = ManyToManyField(User, related_name="signed_event", blank=True, null=True)
    # author will be add to party in form



    def __str__(self):
        # return f"{self.name} {self.date}" 
        return f"{self.signed_users}" 

