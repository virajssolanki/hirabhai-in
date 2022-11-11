from django import forms
from .models import Uimg
from django.core import validators


SITES = (
    ('  ', '    '),
    ('ડાભોર', 'ડાભોર'),
    ('તાંતિવેલા', 'તાંતિવેલા'),
    ('છાત્રોડા', 'છાત્રોડા'),
    ('ડારી', 'ડારી'),
    ('દેદા', 'દેદા'),
    ('પાલડી', 'પાલડી'),
    ('છાપરી', 'છાપરી'),
    ('હસ્નાવદર', 'હસ્નાવદર'),
    ('મલોંઢા', 'મલોંઢા'),
    ('ખેરાળી', 'ખેરાળી'),
    ('વાવડી', 'વાવડી'),
    ('ચમોડા ', 'ચમોડા'),
    ('સારસવા ', 'સારસવા'),
    ('કીંદરવા ', 'કીંદરવા'),
    )



class CustomIntegerField(forms.IntegerField):
    widget = NumberInput
    default_error_messages = {
        'invalid': _('Enter a whole number.'),
    }
    re_decimal = _lazy_re_compile(r'\.0*\s*$')

    def __init__(self, *, max_value=None, min_value=None, **kwargs):
        self.max_value, self.min_value = max_value, min_value
        if kwargs.get('localize') and self.widget == NumberInput:
            # Localized number input is not well supported on most browsers
            kwargs.setdefault('widget', super().widget)
        super().__init__(**kwargs)

        if max_value is not None:
            self.validators.append(validators.MaxValueValidator(max_value, "Enter valid 10 digit mobile number."))
        if min_value is not None:
            self.validators.append(validators.MinValueValidator(min_value, "Enter valid 10 digit mobile number."))


class UimgForm(forms.Form):
    name = forms.CharField(required=False)
    # village = forms.ChoiceField(choices = SITES) 
    village = forms.CharField(required=False) 
    # number = forms.CharField(required=False)
    number = CustomIntegerField(min_value=1000000000, max_value=9999999999)
    img = forms.ImageField()
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super(UimgForm, self).__init__(*args, **kwargs)
        self.fields['img'].label = "ફોટો પસંદ કરવા માટે નીચેનું બટન દબાવો"
        self.fields['name'].label = "તમારું નામ"
        self.fields['number'].label = "મોબાઇલ નંબર"
        self.fields['village'].label = "તમારું ગામ"