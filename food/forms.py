from dataclasses import field, fields
from django import forms
from.models import item

class itemform(forms.ModelForm):
    class Meta:
        model=item
        fields=['itemname','itemdesc','itemprice','itemimage']