from django.forms import ModelForm

from .models import BBoard

class BbForm(ModelForm):
    class Meta:
        model = BBoard
        fields = ( 'title', 'price', 'content', 'user', 'category' )