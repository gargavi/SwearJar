from django import forms
from .models import User, Jar, Log
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404

class AddPenalty(forms.Form):
    who_choices = ( (user.id, user.name) for user in User.objects.all())
    jar_choices = ( (jar.id, jar.name) for jar in Jar.objects.all())
    who = forms.ChoiceField(choices = who_choices, required= True, label = "Who")
    jar = forms.ChoiceField(choices = jar_choices, required = True, label = "Which Jar")
    amount = forms.IntegerField( required =True, min_value = 1, max_value = 20, label = "How much is the penalty?")
    what = forms.CharField( required = True, min_length= 5, label = "What did they do?")
    submitter = forms.CharField(label = "Submitter Name?", required = False)


    def clean_jar(self):
        jar = self.cleaned_data["jar"]
        who = self.cleaned_data["who"]
        user = get_object_or_404(User, pk = who)

        try:
            user.jar_set.get(pk = jar)
        except Jar.DoesNotExist:
            raise ValidationError("That jar does not belong to that user")

        return jar