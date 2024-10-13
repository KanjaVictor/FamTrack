from django import forms
from .models import Family, FamilyMember

class FamilyForm(forms.ModelForm):
    class Meta:
        model = Family
        fields = ['family_name', 'address']