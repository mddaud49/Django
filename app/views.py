from django.shortcuts import render
from .models import Student

# Create your views here.
def Stuinfo(request):
    stud=Student.objects.all()
    return render(request,'home.html', {'stu':stud})
