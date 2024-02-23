import requests
from bs4 import BeautifulSoup

URL = "https://rpi.sodexomyway.com/dining-near-me/hours"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# Find all div elements with class "dining-location"
dining_groups = soup.find_all("li", class_="dining-group")

for group in dining_groups:
    print(group, end="\n"*2)

for group in dining_groups:
    group_name = group.find('h2').text
    print(f"Group: {group_name}")
    dining_locations = group.find_all("div", class_="dining-block")
    for location in dining_locations:
        location_name = location.find('h3').text
        print(f"\nLocation: {location_name}")
        regular_hours = location.find("div", class_="reghours")
        special_hours = location.find_all("div", class_="spechours")
        if regular_hours:
            print("Regular Hours:")
            regular_days_tag = regular_hours.find_all("dt", {"data-arrayregdays": True})
            regular_times = regular_hours.find_all("span", class_="dining-block-hours")
            # Show days of the week
            for days_tag, time in zip(regular_days_tag, regular_times):
                print(f"{days_tag['data-arrayregdays']}: {time.text.strip()}")
        if special_hours:
            for special_hour in special_hours:
                print("\nSpecial Hours:")
                special_dates = special_hour.find_all("span", class_="specweekstart")
                for date in special_dates:
                    print(f"From {date.text.strip()}", end=" - ")
                    end_date = date.find_next("span", class_="specweekend")
                    print(f"{end_date.text.strip()}")
                special_days = special_hour.find_all("p", class_="dining-block-days")
                special_times = special_hour.find_all("p", class_="dining-block-hours")
                for days, times in zip(special_days, special_times):
                    print(f"{days.text.strip()}: {times.text.strip()}")
        print()
