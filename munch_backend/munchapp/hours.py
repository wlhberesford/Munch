import requests
from bs4 import BeautifulSoup

# Define the URL of the webpage to scrape
URL = "https://rpi.sodexomyway.com/dining-near-me/hours"

def parse_information(soup):
    """
    Parse the information from the BeautifulSoup object and save location and hours in a data structure.

    Args:
    soup: BeautifulSoup object representing the parsed HTML content of the page.

    Returns:
    A dictionary containing location names as keys and their corresponding hours as values.
    """
    locations_hours = {}
    dining_groups = soup.find_all("li", class_="dining-group")

    #prints the html
    for group in dining_groups:
        print(group, end="\n"*2)

    for group in dining_groups:
        group_name = group.find('h2').text
        dining_locations = group.find_all("div", class_="dining-block")
        for location in dining_locations:
            location_name = location.find('h3').text
            regular_hours = location.find("div", class_="reghours")
            special_hours = location.find_all("div", class_="spechours")
            location_hours = []
            if regular_hours:
                regular_days_tag = regular_hours.find_all("dt", {"data-arrayregdays": True})
                meal_time = regular_hours.find_all("span", class_="dining-block-note")
                regular_times = regular_hours.find_all("span", class_="dining-block-hours")
                for days_tag, time in zip(regular_days_tag, regular_times):
                    if meal_time:
                        for meal, time in zip(meal_time, regular_times):
                            location_hours.append(f"{days_tag['data-arrayregdays']} {meal.text.strip()}: {time.text.strip()}")
                    else:
                        location_hours.append(f"{days_tag['data-arrayregdays']}: {time.text.strip()}")
            if special_hours:
                for special_hour in special_hours:
                    special_dates = special_hour.find_all("span", class_="specweekstart")
                    for date in special_dates:
                        end_date = date.find_next("span", class_="specweekend")
                        location_hours.append(f"From {date.text.strip()} - {end_date.text.strip()}")
                    special_days = special_hour.find_all("p", class_="dining-block-days")
                    special_times = special_hour.find_all("p", class_="dining-block-hours")
                    for days, times in zip(special_days, special_times):
                        location_hours.append(f"{days.text.strip()}: {times.text.strip()}")
            locations_hours[location_name] = location_hours
    return locations_hours

def get_hours(location_name, locations_hours):
    """
    Get the hours for a specific location.

    Args:
    location_name: Name of the location for which hours are to be retrieved.
    locations_hours: Dictionary containing location names as keys and their corresponding hours as values.

    Returns:
    A list of strings representing the hours for the specified location.
    """
    return locations_hours.get(location_name, [])

def main():
    # Send an HTTP GET request to the URL and store the response
    page = requests.get(URL)
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page.content, "html.parser")
    # Parse information and save location and hours in a data structure
    locations_hours = parse_information(soup)
    # Get hours for a specific location
    location_name = "The Commons Dining Hall"  # Replace "Location Name" with the desired location
    hours = get_hours(location_name, locations_hours)
    if hours:
        print(f"Hours for {location_name}:")
        for hour in hours:
            print(hour)
    else:
        print(f"No hours found for {location_name}.")

if __name__ == "__main__":
    main()
