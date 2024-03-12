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

import json

def get_day():
    current_date_time = datetime.now()
    return str(current_date_time.day)

def get_menu(url):
    #This parses the menu from the dining hall assuming its current website format, will not work if website changes

    data = requests.get(url)
    soup = BeautifulSoup(data.content, "html.parser")

    content_element = soup.find("main", id="content")
    if content_element is None:
        return {"Error":"No content found"}
    bottom_half = content_element.find_all("div", class_="bottom-half")
    if len(bottom_half) == 0:
        return {"Error":"No bottom half found"}
    main_content = bottom_half[0].find_all("div", class_="main-content")
    if len(main_content) == 0:
        return {"Error":"No main content found"}
    bite_menu = main_content[0].find_all("div", id="bite-menu")
    if len(bite_menu) == 0:
        return {"Error":"No bite menu found"}
    name = "menuid-"+get_day()+"-day"
    bite_menu2 = bite_menu[0].find_all("div", id=name)
    if len(bite_menu2) == 0:
        return {"Error":"No bite menu 2 found"}
    accordian = bite_menu2[0].find_all("div", class_="accordion")
    if len(accordian) == 0:
        return {"Error":"No accordian found"}
    breakfast = accordian[0].find_all("div", class_="accordion-block breakfast")
    if len(breakfast) == 0:
        return {"Error":"No breakfast found"}
    lunch = accordian[0].find_all("div", class_="accordion-block lunch")
    if len(lunch) == 0:
        return {"Error":"No lunch found"}
    dinner = accordian[0].find_all("div", class_="accordion-block dinner")
    if len(dinner) == 0:
        return {"Error":"No dinner found"}
    breakfast_items = breakfast[0].find_all("div", class_="accordion-panel rtf hide")
    if len(breakfast_items) == 0:
        return {"Error":"No breakfast items found"}
    lunch_items = lunch[0].find_all("div", class_="accordion-panel rtf hide")
    if len(lunch_items) == 0:
        return {"Error":"No lunch items found"}
    dinner_items = dinner[0].find_all("div", class_="accordion-panel rtf hide")
    if len(dinner_items) == 0:
        return {"Error":"No dinner items found"}
    
    breakfast_elements = dict()
    lunch_elements = dict()
    dinner_elements = dict()

    for div in breakfast_items[0]:
        associated_list = div.find_next_sibling("ul")
        if associated_list is None:
            continue
        else:
            li_elements = associated_list.find_all("li")
            for i in li_elements:
                if i is None:
                    continue
                else:
                    li_div1 = i.find_all("div", class_="col-xs-9")
                    text = ""
                    food_tags = []
                    if li_div1 is None:
                        continue
                    else:
                        li_div1 = li_div1[0]
                        a_tag = li_div1.find_all("a")
                        text = a_tag[0].get_text()
                        if text=="Have A Nice Day!":
                            continue
                        allergen_div = li_div1.find_all("div")
                        img_tags = allergen_div[0].find_all("img")
                        for img in img_tags:
                            if "alt" in img.attrs:
                                food_tags.append(img["alt"])
                    
                    calories = ""
                    li_div2 = i.find_all("div", class_="col-xs-3 text-right")
                    if li_div2 is None:
                        continue
                    else:
                        calories = (li_div2[0].get_text()).strip()
                        calories = calories[0:len(calories)-3]
                        calories = int(calories)
                    
                    temp = [calories, food_tags]
                    breakfast_elements[text] = temp

    for div in lunch_items[0]:
        associated_list = div.find_next_sibling("ul")
        if associated_list is None:
            continue
        else:
            li_elements = associated_list.find_all("li")
            for i in li_elements:
                if i is None:
                    continue
                else:
                    li_div1 = i.find_all("div", class_="col-xs-9")
                    text = ""
                    food_tags = []
                    if li_div1 is None:
                        continue
                    else:
                        li_div1 = li_div1[0]
                        a_tag = li_div1.find_all("a")
                        text = a_tag[0].get_text()
                        if text=="Have A Nice Day!":
                            continue
                        allergen_div = li_div1.find_all("div")
                        img_tags = allergen_div[0].find_all("img")
                        for img in img_tags:
                            if "alt" in img.attrs:
                                food_tags.append(img["alt"])
                    
                    calories = ""
                    li_div2 = i.find_all("div", class_="col-xs-3 text-right")
                    if li_div2 is None:
                        continue
                    else:
                        calories = (li_div2[0].get_text()).strip()
                        calories = calories[0:len(calories)-3]
                        calories = int(calories)
                    
                    temp = [calories, food_tags]
                    lunch_elements[text] = temp

    for div in dinner_items[0]:
        associated_list = div.find_next_sibling("ul")
        if associated_list is None:
            continue
        else:
            li_elements = associated_list.find_all("li")
            for i in li_elements:
                if i is None:
                    continue
                else:
                    li_div1 = i.find_all("div", class_="col-xs-9")
                    text = ""
                    food_tags = []
                    if li_div1 is None:
                        continue
                    else:
                        li_div1 = li_div1[0]
                        a_tag = li_div1.find_all("a")
                        text = a_tag[0].get_text()
                        if text=="Have A Nice Day!":
                            continue
                        allergen_div = li_div1.find_all("div")
                        img_tags = allergen_div[0].find_all("img")
                        for img in img_tags:
                            if "alt" in img.attrs:
                                food_tags.append(img["alt"])
                    
                    calories = ""
                    li_div2 = i.find_all("div", class_="col-xs-3 text-right")
                    if li_div2 is None:
                        continue
                    else:
                        calories = (li_div2[0].get_text()).strip()
                        calories = calories[0:len(calories)-3]
                        calories = int(calories)
                    
                    temp = [calories, food_
                            tags]
                    dinner_elements[text] = temp

    '''
    for i in breakfast_elements:
        print(i, breakfast_elements[i])

    for i in lunch_elements:
        print(i, lunch_elements[i])

    for i in dinner_elements:
        print(i, dinner_elements[i])
    '''

    return {"breakfast":breakfast_elements, "lunch":lunch_elements, "dinner":dinner_elements}
        
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
    get_menu('https://menus.sodexomyway.com/BiteMenu/Menu?menuId=15285&locationId=76929002&whereami=http://rpi.sodexomyway.com/dining-near-me/commons-dining-hall')
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

