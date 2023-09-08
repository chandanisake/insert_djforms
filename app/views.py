from django.shortcuts import render


# Create your views here:
from app.forms import *
from app.models import *


def insert_student(request):

    SFEO=StudentForm()
    d={'SFEO':SFEO}
    if request.method=='POST':
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            Sname=SFD.cleaned_data['Sname']
            Sid=SFD.cleaned_data['Sid']
            Semail=SFD.cleaned_data['Semail']

            SO=Student.objects.get_or_create(Sname=Sname,Sid=Sid,Semail=Semail)[0]
            SO.save()
            QSO=Student.objects.all()
            d1={'QSO':QSO}
           

        
       
        return render(request,'display_student.html',d1)
    
    

    return render(request,'insert_student.html',d)
