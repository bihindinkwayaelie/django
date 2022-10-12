import africastalking
from django.shortcuts import render, redirect
from .models import *

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


username="bihindinkwayaelijah@gmail.com"
api_key="a1be464562cfb44a346acf93216c1d1052595153000d83f3cd18ed4f4d11212f"
africastalking.initialize(username,api_key)
# Create your views here.
def index(request):
    selectdata= Employee.objects.all()
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        insertdata= Employee(username=username,password=password)
        try:
            insertdata.save()
            return render(request, 'index.html',{'data':selectdata})
        except:
            return render(request, 'index.html')
    return render(request,'index.html',{'data':selectdata})

def about(request):
    return render(request, 'about.html')
def indiba(request):
    selectdata= Indibagallery.objects.all()
    return render(request, 'indiba.html',{'data':selectdata})
def more(request):
    selectdata= Indibagallery.objects.all()
    return render(request, 'more.html',{'data':selectdata})
def register(request):
    selectdata= Indibagallery.objects.all()
    if request.method=='POST':
        title=request.POST['title']
        body=request.POST['body']
        image=request.FILES['image']
        insertdata= Indibagallery(title=title,body=body,image=image)
        try:
            insertdata.save()
            return render(request, 'register.html',{'data':selectdata})
        except:
            return render(request, 'register.html')
    return render(request,'register.html',{'data':selectdata})
def deletedata(request,id):
    selectdata= Employee.objects.get(id=id)
    selectdata.delete()
    return redirect('welcome')
def deleteart(request,id):
    selectdata= Indibagallery.objects.get(id=id)
    selectdata.delete()
    return redirect('indiba')
def edit(request,id):
    selectdata= Employee.objects.get(id=id)
    if request.method == 'POST':
        selectdata.username = request.POST['username']
        selectdata.password = request.POST['password']
        msg = selectdata.save()
        if msg == True:
            redirect('welcome')
    return render(request,'edit.html',{"data":selectdata})
@csrf_exempt
def idaussd(request):
    if request.method == 'POST':

        session_id = request.POST.get("sessionId")
        service_code = request.POST.get("serviceCode")
        phone_number = request.POST.get("phoneNumber")
        text = request.POST.get("text")
        response = ""
        if text == '':
            response = "Welcome to DOPEMVNN Tech \n"
            response += "1. Iyandikishe \n"
            response += "2. Sura konte\n"
            response += "3. Gura ibicuruzwa"
        elif text == '1':
            response = "IYANDIKISHE \n"
            response += "1.Ukoresheje phone \n"
            response += "2. Ukoresheje ID"
        else:
            response = "no choice"
            return HttpResponse(response)
    return HttpResponse(response)