import requests
from bs4 import BeautifulSoup

# Define the URL of the webpage to scrape
URL = "https://rpi.sodexomyway.com/dining-near-me/hours"

# Send an HTTP GET request to the URL and store the response
page = requests.get(URL)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(page.content, "html.parser")

# Find all div elements with class "dining-location"
dining_groups = soup.find_all("li", class_="dining-group")

# Print each dining group with a blank line between them
# for group in dining_groups:
#     print(group, end="\n"*2)

# Iterate through each dining group
for group in dining_groups:
    # Extract the group name from the h2 tag
    group_name = group.find('h2').text
    print(f"Group: {group_name}")

    # Find all dining locations within the group
    dining_locations = group.find_all("div", class_="dining-block")

    #check if dining group is resident dining
    resident = False;
    if(group_name == "Resident Dining"):
        resident = True
   
    # Iterate through each dining location
    for location in dining_locations:
        # Extract the location name from the h3 tag
        location_name = location.find('h3').text
        print(f"\nLocation: {location_name}")

        # Find the regular hours for the location
        regular_hours = location.find("div", class_="reghours")

        # Find special hours for the location, if any
        special_hours = location.find_all("div", class_="spechours")

        # If regular hours are found, print them
        if regular_hours:
            print("Regular Hours:")
            # Find all dt tags with the attribute "data-arrayregdays"
            regular_days_tag = regular_hours.find_all("dt", {"data-arrayregdays": True})
            #Find all dining-block-notes
            meal_time = regular_hours.find_all("span", class_="dining-block-note")
            # Find all span tags with class "dining-block-hours"
            regular_times = regular_hours.find_all("span", class_="dining-block-hours")

            #Chekc if it is resident dining so we can display whether it is breakfast, lunch, or dinner
            if(resident == False):
                # Iterate through each pair of days and corresponding hours
                for days_tag, time in zip(regular_days_tag, regular_times):
                    # Print the days and hours
                    print(f"{days_tag['data-arrayregdays']}: {time.text.strip()}")
            else:
                #same but with meal time
                for days_tag, meal, time in zip(regular_days_tag, meal_time, regular_times):
                    # Print the days and hours
                    print(f"{days_tag['data-arrayregdays']} {meal.text.strip()}: {time.text.strip()}")

        # If special hours are found, print them
        if special_hours:
            for special_hour in special_hours:
                print("\nSpecial Hours:")
                # Find all span tags with class "specweekstart"
                special_dates = special_hour.find_all("span", class_="specweekstart")
                # Iterate through each special date range
                for date in special_dates:
                    # Print the start and end dates of the special period
                    print(f"From {date.text.strip()}", end=" - ")
                    end_date = date.find_next("span", class_="specweekend")
                    print(f"{end_date.text.strip()}")
                # Find all p tags with class "dining-block-days" and "dining-block-hours"
                special_days = special_hour.find_all("p", class_="dining-block-days")
                special_times = special_hour.find_all("p", class_="dining-block-hours")
                # Iterate through each special day and corresponding hours
                for days, times in zip(special_days, special_times):
                    # Print the special days and hours
                    print(f"{days.text.strip()}: {times.text.strip()}")

        print()  # Add a blank line after each location's information
