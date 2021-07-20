from django.shortcuts import render
from .models import Member
from django.http import HttpResponse

# Create your views here.


def index(request):
    members=Member.objects.all()   #fetching all from database


    context={
        'members':members
    }
    return render(request,'listings/index.html',context)

def about(request):
    return render(request,'listings/about.html')
