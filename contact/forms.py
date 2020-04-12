from django import forms

from .models import contact

class contactform(forms.ModelForm):
    class Meta:
        model=contact
        fields=('first_name','last_name','email','message','resume','file')