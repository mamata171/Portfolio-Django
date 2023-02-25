from django.shortcuts import render
from django.http import HttpResponse
from Home.models import contact_me
# Create your views here.


def home(request):
     if request.method == 'POST':
        name = request.POST['name']
        city = request.POST['city']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']

        obj = contact_me(name = name,city = city,phone = phone,email = email,message = message)
        obj.save()
        print("the data has been return to the db")
     return render(request,'index.html')

