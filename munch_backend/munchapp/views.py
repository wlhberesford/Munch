from django.shortcuts import render

#Run the commented pip installs if you haven't installed

from django.http import HttpResponse

from django.template import loader

import requests
#pip install requests

from bs4 import BeautifulSoup
#pip install beautifulsoup4
from datetime import datetime

from .models import Post
#.models from models file in current directory
#posts = [
    #testing, creating posts to show data
    #in the posts, we have blocks of info with each block containing text data ex. name, allergens, station
#    {
    #'author': 'Munch_Team',
    #'title': 'Dining meal',
    #'content': 'Grilled Mexican Vegetables',
    #'diningHall': 'Commons'
#    },


#    {
    #'author': 'Munch_Team',
    #'title': 'Dining meal',
    #'content': 'Spicy Tofu Stir-fry',
    #'diningHall': 'Commons'
    #}
#]
#^ dummy data, testing data in the db.sqlite3 file
#to access, python manage.py shell
#type from munchapp.models import Post
#type from django.contrib.auth.models import User
#this allows developers to access posts and users

#User.objects.all()
#Post.objects.all()
#user = User.objects.get(id=1)
#OR user = User.objects.filter(username='').first()
#To create post post_# = Post(title = '', content = '', author = user)

def get_day():
    current_date_time = datetime.now()
    return str(current_date_time.day)

def get_menu():

    #THIS DOES NOT WORK YET but almost done

    url = 'https://menus.sodexomyway.com/BiteMenu/Menu?menuId=15285&locationId=76929002&whereami=http://rpi.sodexomyway.com/dining-near-me/commons-dining-hall'
    data = requests.get(url)
    soup = BeautifulSoup(data.content, "html.parser")

    content_element = soup.find("main", id="content")
    bottom_half = content_element.find_all("div", class_="bottom-half")
    main_content = bottom_half[0].find_all("div", class_="main-content")
    bite_menu = main_content[0].find_all("div", id="bite-menu")
    name = "menuid-"+get_day()+"-day"
    print("HI ", name)
    bite_menu2 = bite_menu[0].find_all("div", id=name)
    accordian = bite_menu2[0].find_all("div", class_="accordion")



    print("HI ", bite_menu2)

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
        'posts': Post.objects.all(),
        'title': 'Munch Home' 
        #'key': from above
    }
    return render(request, 'munchapp/home.html', context)

