from django.db.models.query import prefetch_related_objects
from django.shortcuts import render
from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from django.views.generic.edit import ProcessFormView
from .forms import *
from .models import *
from django.http import HttpResponse
from .utils import get_plot


# Create your views here.

arr=[]
percent=0
previous=0
length=0
progress=0
result=[]
prograph=[]
surveyno=[]
# Create your views here.
def quiz(request):
    if request.method == 'POST':
        print(request.POST)
        questions=QuesModel.objects.all()
        global arr,percent,previous
        if(arr!=[]):
            previous=percent
            print(previous)
            prograph.append(previous)


        
        tmp=[]
        for q in questions:
            tmp.append(request.POST.get(q.question))


        length=len(tmp)
        arr.insert(0,tmp)
        o1=0
        o2=0
        o3=0
        o4=0
        print(arr)
        for i in range(length):
            if(arr[0][i]=="option1"):
                o1+=1
            elif(arr[0][i]=="option2"):
                o2+=1
            elif(arr[0][i]=="option3"):
                o3+=1
            if(arr[0][i]=="option4"):
                o4+=1

        print(o1,o2,o3,o4)

        surveyno=[i for i in range(len(prograph))]
        print(surveyno)
        
        if((o1<=(length/4) and o2<=(length/4) and o3<=(length/4) and o4>=(3*(length/4))) or 
        ((o1<=(length/4) and o2<=(length/4) and o3<=(length/2) and o4>=(length/2)))):
            str="You need to badly improve your health.\n"
            percent=10

        elif((o1<=(length/4) and o2<=(length/4) and o3>=(3*(length/4)) and o4<=(length/4)) or 
        ((o1<=(length/4) and o2<=(length/2) and o3>=(length/2) and o4<=(length/4)))):
            str="You need to take care of your health.\n"
            percent=40

        elif((o1<=(length/4) and o2>=(3*(length/4) and o3<=(length/4) and o4<=(length/4))) or 
        ((o1<=(length/4) and o2>=(length/2) and o3<=(length/2) and o4<=(length/4)))):
            str="Your health is good.\n"
            percent=70

        elif((o1>=(3*(length/4)) and o2<=(length/4) and o3<=(length/4) and o4<=(length/4)) or 
        ((o1>=(length/2) and o2<=(length/2) and o3<=(length/4) and o4<=(length/4)))):
            str="Your health is perfectly fine.\n"
            print("best")
            percent=100
        else:
            str="you need to improve your health.\n"
            percent=50

        list=[]

        for q in questions:
            if((request.POST.get(q.question)!='option2') and (request.POST.get(q.question)!='option1')):
                print(request.POST.get(q.question))
                str+="\n"+q.ans
                print(q.ans)
        
        result=str
        progress=percent-previous
        chart=get_plot(surveyno,prograph)
        context = {
            'result':result,
            'percent':percent,
            'previous':previous,
            'progress':progress,
            'chart':chart

        }
        
        return render(request,'home.html',context)
    else:
        questions=QuesModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'home.html',context)
 
def addQuestion(request):    
    if request.user.is_staff:
        form=addQuestionform()
        if(request.method=='POST'):
            form=addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'addqs.html',context)
    else: 
        return redirect('home') 
 