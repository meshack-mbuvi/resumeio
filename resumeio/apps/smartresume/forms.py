from .models import PersonalDetails
from django import forms
from django.db import models

class PersonalDetailsForm(forms.ModelForm):
    class Meta:
        model = PersonalDetails
        fields = ('first_name', 'last_name', 'job_title', 'phone', 'user')

    def clean(self):
        """
        User is not selected in the rendered form and thus we override this
        method to add user id to the cleaned_data dictionary, and then pass the
        data to validation process
        """
        user = self.data.get('user')
        self.cleaned_data['user'] = int(user)
        return super(PersonalDetailsForm, self).clean()

