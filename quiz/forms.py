from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
 
class addQuestionform(ModelForm):
    class Meta:
        model=QuesModel
        fields="__all__"