from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from django.template import loader

import requests

from bs4 import BeautifulSoup

posts = [
    #testing, creating posts to show data
    #in the posts, we have blocks of info with each block containing text data ex. name, allergens, station
    {
    'author': 'Munch_Team',
    'title': 'Dining meal',
    'content': 'Grilled Mexican Vegetables',
    'diningHall': 'Commons'
    },


    {
    'author': 'Munch_Team',
    'title': 'Dining meal',
    'content': 'Spicy Tofu Stir-fry',
    'diningHall': 'Commons'
    }


]








def get_menu():

    #THIS DOES NOT WORK YET

    url = 'https://rpi.sodexomyway.com/dining-near-me/russell-sage'
    data = requests.get(url)
    soup = BeautifulSoup(data, "html.parser")

    content_element = soup.find("main", id="content")
    content_element = soup.find("div", id="bottom_half")
    content_element = soup.find("div", id="main_content")
    content_element = soup.find("div", id="bite_menu")

    print (content_element)

def get_hrs():
    
    #THIS DOES NOT WORK YET

    hrs = []

    url = 'https://menus.sodexomyway.com/BiteMenu/Menu?menuId=15285&locationId=76929002&whereami=http://rpi.sodexomyway.com/dining-near-me/commons-dining-hall'
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
    print(get_menu())
    print(get_hrs())
    return render(request, 'munchapp/menu.html')

def about(request):
    return HttpResponse('<h1>rcos munch dining hall project rpi</h1>')

def home(request):
    context = {
    #"(context) dictionary"
        'posts': posts,
        'title': 'Munch Home' 
        #'key': from above
    }
    return render(request, 'munchapp/home.html', context)

