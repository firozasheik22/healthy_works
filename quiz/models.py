from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
 
# Create your models here.
class QuesModel(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=1000,null=True)
    
    def __str__(self):
        return self.question

class UserProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    prograph = ArrayField(ArrayField(models.IntegerField()))
    surveyno = ArrayField(ArrayField(models.IntegerField()))
    
    def __str__(self):
        return f'{self.user.username} UserProgress'