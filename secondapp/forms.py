from .models import Course
from django import forms


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'cnt'] # id 속성은 PK 이므로 사용하지 않음