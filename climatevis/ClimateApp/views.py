from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
import requests
from django import forms
# Create your views here.
def IndexView(request):
    return render(request,'index.html')

@login_required
def dashboardView(request):
    return render(request,'dashboard.html')    

def registerView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form':form})    

def geodata(request):
    if request.method == 'POST':
        lat=request.POST['lat']
        lon=request.POST['lon']
        lat2=request.POST['lat']
        lon2=request.POST['lon']
        #day_size="3"
        url2='http://api.openweathermap.org/data/2.5/weather?lat='+lat2+'&lon='+lon2+'&appid=5314e469616edf594366af6da702274c&units=metric'
        url='http://api.openweathermap.org/data/2.5/weather?lat='+lat+'&lon='+lon+'&appid=5314e469616edf594366af6da702274c&units=metric'
        
        res=requests.get(url)
        data=res.json()
        res2=requests.get(url2)
        data2=res2.json()
        data_exp={
            "temp":str(data['main']['temp']),
            "wind":str(data['wind']['speed']),
            "latitude":str(data['coord']['lat']),
            "longitude":str(data['coord']['lon']),
            "pressure":str(data['main']['pressure']),
            "humidity":str(data['main']['humidity']),
    
        }
        data_exp2={
            "temp":str(data2['main']['temp']),
            "wind":str(data2['wind']['speed']),
            "latitude":str(data2['coord']['lat']),
            "longitude":str(data2['coord']['lon']),
            "pressure":str(data2['main']['pressure']),
            "humidity":str(data2['main']['humidity']),
        


        }
        print(data_exp)
        print(data_exp2)
    else:
        lon=''
        lat=''
        data_exp={}
        data_exp2={}  
           
    return render(request,'dashboard.html',{'lon':lon,'lat':lat,'data_exp':data_exp,'lon2':lon2,'lat2':lat2,'data_exp2':data_exp2})





    