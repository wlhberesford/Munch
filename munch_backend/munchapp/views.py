from django.shortcuts import render

#Run the commented pip installs if you haven't installed

from django.http import HttpResponse

from django.template import loader

import requests
#pip install requests

from bs4 import BeautifulSoup
#pip install beautifulsoup4
from datetime import datetime

#from .models import Post

import json

def get_day():
    current_date_time = datetime.now()
    return str(current_date_time.day)


def testingjson(dictionarytest, nums):

    if nums==0:
        with open('breakfast.json', 'w') as json_file:
            json.dump(dictionarytest, json_file, indent=4)
    if (nums == 1):
        with open('lunch.json', 'w') as json_file:
            json.dump(dictionarytest, json_file, indent=4)

    if (nums ==2):
        with open('dinner.json', 'w') as json_file:
            json.dump(dictionarytest, json_file, indent=4)


def get_menu(url):
    #This parses the menu from the dining hall assuming its current website format, will not work if website changes

    data = requests.get(url)
    soup = BeautifulSoup(data.content, "html.parser")

    content_element = soup.find("main", id="content")
    if content_element is None:
        return {"error":"no content found"}
    bottom_half = content_element.find_all("div", class_="bottom-half")
    if len(bottom_half) == 0:
        return {"error":"no bottom half found"}
    main_content = bottom_half[0].find_all("div", class_="main-content")
    if len(main_content) == 0:
        return {"error":"no main content found"}
    bite_menu = main_content[0].find_all("div", id="bite-menu")
    if len(bite_menu) == 0:
        return {"error":"no bite menu found"}
    name = "menuid-"+get_day()+"-day"
    bite_menu2 = bite_menu[0].find_all("div", id=name)
    if len(bite_menu2) == 0:
        return {"error":"no bite menu 2 found"}
    accordian = bite_menu2[0].find_all("div", class_="accordion")
    if len(accordian) == 0:
        return {"error":"no accordian found"}
    

    bf_avail = 0
    brunch_avail = 0
    lunch_avail = 0
    dinner_avail = 0


    breakfast = accordian[0].find_all("div", class_="accordion-block breakfast")
    if len(breakfast) == 0:
        bf_avail = 1
    else:        
        breakfast_items = breakfast[0].find_all("div", class_="accordion-panel rtf hide")

    brunch = accordian[0].find_all("div", class_="accordion-block brunch")
    if len(brunch) == 0:
        brunch_avail = 1
    else:
        brunch_items = brunch[0].find_all("div", class_="accordion-panel rtf hide")

    lunch = accordian[0].find_all("div", class_="accordion-block lunch")
    if len(lunch) == 0:
        lunch_avail = 1
    else:
        lunch_items = lunch[0].find_all("div", class_="accordion-panel rtf hide")

    dinner = accordian[0].find_all("div", class_="accordion-block dinner")
    if len(dinner) == 0:
        dinner_avail = 1
    else:
        dinner_items = dinner[0].find_all("div", class_="accordion-panel rtf hide")
    
    breakfast_elements = dict()
    lunch_elements = dict()
    dinner_elements = dict()
    brunch_elements = dict()

    if bf_avail == 0:
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

    if lunch_avail == 0:
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

    if dinner_avail == 0:
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
                        
                        temp = [calories, food_tags]
                        dinner_elements[text] = temp

    if brunch_avail == 0:
        for div in brunch_items[0]:
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
                        brunch[text] = temp

    
    '''
    for i in breakfast_elements:
        print(i, breakfast_elements[i])

    for i in lunch_elements:
        print(i, lunch_elements[i])

    for i in dinner_elements:
        print(i, dinner_elements[i])

    for i in brunch_elements:
        print(i, brunch[i])
    '''

    if bf_avail == 1:
        breakfast_elements = {"none":"no breakfast available"}
    if brunch_avail == 1:
        brunch = {"none":"no brunch available"}
    if lunch_avail == 1:
        lunch_elements = {"none":"no lunch available"}
    if dinner_avail == 1:
        dinner_elements = {"none":"no dinner available"}

    final_dict = {"breakfast":breakfast_elements, "lunch":lunch_elements, "dinner":dinner_elements, "brunch:":brunch_elements, "error":"none"}


    return final_dict

def get_hrs(dining_name):
   
   hours_list = []
  
   url = 'https://rpi.sodexomyway.com/dining-near-me/' + dining_name
   result = requests.get(url)
   content = result.text
   soup = BeautifulSoup(content, 'lxml')
   blocks = soup.find_all('div', class_='ca-operation-hours-block')

   hours_list = []

   for block in blocks:
       meal = block['data-reghourstitle']
       start_time = block['data-formatreghoursstart']
       end_time = block['data-formatreghoursend']
       days = block['data-regdays']
       hours = f"{meal} ({days}): {start_time} - {end_time}"
       hours_list.append(hours)


   return hours_list




dining_hours = get_hrs("russell-sage")
print(dining_hours)


def menu_sage(request):
    get_menu('https://menus.sodexomyway.com/BiteMenu/Menu?menuId=15285&locationId=76929002&whereami=http://rpi.sodexomyway.com/dining-near-me/commons-dining-hall')
    return render(request, 'munchapp/menu.html')

def about(request):
    return HttpResponse('<h1>RCOS Munch Dining Hall Project RPI</h1>')

def home(request):
    context = {
    #"(context) dictionary"
        'posts': Post.objects.all(),
        'title': 'Munch Home' 
        #'key': from above
    }
    return render(request, 'munchapp/home.html', context)
