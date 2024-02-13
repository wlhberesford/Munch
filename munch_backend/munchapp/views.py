from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from django.template import loader

import requests

from bs4 import BeautifulSoup

def get_hrs():
    
    #THIS DOES NOT WORK YET

    hrs = []

    url = 'https://rpi.sodexomyway.com/dining-near-me/russell-sage'
    data = requests.get(url)
    html = BeautifulSoup(data.text, 'html.parser')
    times = html.select('todays-hrs-block')

    print(times)

    for time in times:
        start_time = time.select('start-hours').get_text()
        end_time = time.select('end-hours').get_text()

        hrs.append(start_time + end_time)

    return hrs

def menu_sage(request):
    print(get_hrs())
    return render(request, 'munchapp/menu.html')

def about(request):
    return HttpResponse('<h1>rcos munch dining hall project rpi</h1>')