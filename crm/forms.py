from django.forms import ModelForm
from .models import *

class Orderform(ModelForm):
    class Meta:
        model =Order
        fields ='__all__'