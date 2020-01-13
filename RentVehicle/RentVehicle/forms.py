from Vehicle import models
from django import forms
from dropdowndb.models import ZipCode
from searchableselect.widgets import SearchableSelect

class CreateFilter(forms.ModelForm):
    class Meta:
        model = models.Filter
        fields = ['zipcode']
        widget ={
            'zipcode' : SearchableSelect(model=ZipCode,search_field='zipcode')
        }
