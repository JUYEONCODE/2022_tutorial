from .models import Owner
from django import forms


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['name'] # id 속성은 PK 이므로 사용하지 않음