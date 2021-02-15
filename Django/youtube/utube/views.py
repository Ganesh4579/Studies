from django.shortcuts import render
import requests
from django.conf import settings

# Create your views here.

def home(request):
    s_url='https://www.googleapis.com/youtube/v3/search'
    
    d={
        'part':'snippet',
        'q':'parithabangal',
        'key':settings.YOUTUBE_DATA_API_KEY ,
        'maxResults':9
    }
    
    r=requests.get(s_url,params=d)
    print(r.json())
    return render(request,'index.html')