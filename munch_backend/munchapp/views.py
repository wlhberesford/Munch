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

import os

import shutil

def get_day():
    current_date_time = datetime.now()
    return str(current_date_time.day)


def savingJson(saved_dict, name):

    '''
    if nums==0:
        with open('breakfast.json', 'w') as json_file:
            json.dump(dictionarytest, json_file, indent=4)
    if (nums == 1):
        with open('lunch.json', 'w') as json_file:
            json.dump(dictionarytest, json_file, indent=4)
    if (nums ==2):
        with open('dinner.json', 'w') as json_file:
            json.dump(dictionarytest, json_file, indent=4)
    '''

    folder = "menus"
    if not os.path.exists(folder):
        os.makedirs(folder)

    name = os.path.join(folder, name)

    with open(name, 'w') as json_file:
        json.dump(saved_dict, json_file, indent=4)



def get_menu(url, name):
    #This parses the menu from the dining hall assuming its current website format, will not work if website changes

    if os.path.exists(os.path.join("menus",(name+"_data.json"))):
        path = os.path.join("menus",(name+"_data.json"))
        with open(path, 'r') as json_file:
            current = json.load(json_file)
            last_date = current["last_updated"]["date"]
            today = get_current_time()["date"]
            if (last_date == today):
                return current
            else:
                archive_folder = os.path.join("menus", "archive", last_date)
                os.makedirs(archive_folder, exist_ok=True)
                new_path = os.path.join(archive_folder, name + "_data.json")
                shutil.move(path, new_path)

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
    
    day = get_day()
    id_name = "menuid-"+day+"-day"
    bite_menu2 = bite_menu[0].find_all("div", id=id_name)

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

    final_dict = dict()

    if bf_avail != 1:
        final_dict["breakfast"] = breakfast_elements
    if brunch_avail != 1:
        final_dict["brunch"] = brunch_elements
    if lunch_avail != 1:
        final_dict["lunch"] = lunch_elements
    if dinner_avail != 1:
        final_dict["dinner"] = dinner_elements

    final_dict["last_updated"]=get_current_time()

    savingJson(final_dict, name+"_data.json")

    return final_dict
        
def get_current_time():
    # Get the current date and time
    current_datetime = datetime.now()
    current_date = str(current_datetime.date())
    current_time = current_datetime.time()
    current_time = current_time.strftime("%H:%M")
    return {"date": current_date, "time": current_time}

def get_hrs():
    
    #THIS DOES NOT WORK YET

    hrs = []

    url = 'https://menus.sodexomyway.com/BiteMenu/Menu?menuId=15285&locationId=76929002&whereami=http://rpi.sodexomyway.com/dining-near-me/commons-dining-hall'
    data = requests.get(url)
    html = BeautifulSoup(data.text, 'html.parser')
    times = html.select('.todays-hrs-block')

    for time in times:
        start_time = time.select_one('.start-hours').get_text(strip=True)
        end_time = time.select_one('.end-hours').get_text(strip=True)

        hrs.append(start_time + ' - ' + end_time)

    return hrs

'''
^^^
dining_hours = get_hrs()
for i, hour in enumerate(dining_hours, start=1):
    print(f"Day {i}: {hour}")
'''

def menu_sage(request):
    menu = get_menu('https://menus.sodexomyway.com/BiteMenu/Menu?menuId=15285&locationId=76929002&whereami=http://rpi.sodexomyway.com/dining-near-me/commons-dining-hall','sage')
    context = {
        'menu': menu
    }
    return render(request, 'munchapp/russel_sage.html', context)

def menu_commons(request):
    menu = get_menu('https://menus.sodexomyway.com/BiteMenu/Menu?menuId=15465&locationId=76929001&whereami=http://rpi.sodexomyway.com/dining-near-me/commons-dining-hall','commons')
    context = {
        'menu': menu
    }
    return render(request, 'munchapp/commons.html', context)

def menu_blitman(request):
    menu = get_menu('https://menus.sodexomyway.com/BiteMenu/Menu?menuId=15288&locationId=76929015&whereami=http://rpi.sodexomyway.com/dining-near-me/commons-dining-hall','blitman')
    context = {
        'menu': menu
    }
    return render(request, 'munchapp/blitman.html', context)

def menu_barh(request):
    menu = get_menu('https://menus.sodexomyway.com/BiteMenu/Menu?menuId=15286&locationId=76929003&whereami=http://rpi.sodexomyway.com/dining-near-me/commons-dining-hall', 'barh')
    context = {
        'menu': menu
    }
    return render(request, 'munchapp/barh.html', context)

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
