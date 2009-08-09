from django import forms
from django.utils.translation import ugettext as _

class CreateLinkForm(forms.Form):
    title = forms.CharField(label=_("Title"), max_length=100)
    url  = forms.CharField(label=_("Url"), max_length=255)
    description = forms.CharField(label=_("Description"), required=False,widget=forms.Textarea(attrs={'rows':8, 'cols':50}))
    
    

