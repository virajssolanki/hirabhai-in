from django import forms
from .models import Uimg


class UimgForm(forms.Form):
    name = forms.CharField(required=True)
    village = forms.CharField(required=True)
    number = forms.CharField(required=True)
    img = forms.ImageField()
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super(UimgForm, self).__init__(*args, **kwargs)
        self.fields['img'].label = "Click here to choose photo"