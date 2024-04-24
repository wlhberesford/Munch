# asgi.py
1. The `os` module is imported to interact with the operating system.
2. The `get_asgi_application` function from Django's ASGI module is imported. This function is used to create an instance of the Django application.
3. The environment variable `DJANGO_SETTINGS_MODULE` is set to `munch_backend.settings`. This specifies the settings file for the Django project.
4. An instance of the Django application is created using `get_asgi_application()` and assigned to the variable `application`. This application can be served by an ASGI server.

- This setup allows the Django project to be served asynchronously, supporting high-performance operations and features like WebSockets and long-poll HTTP.

# settings.py
1. `BASE_DIR`: The base directory of the project.
2. `SECRET_KEY`: A secret key for this Django installation used for cryptographic signing.
3. `DEBUG`: A boolean that turns on/off debug mode.
4. `ALLOWED_HOSTS`: A list of host/domain names that this Django site can serve.
5. `INSTALLED_APPS`: A list of all Django applications activated in this instance of Django.
6. `MIDDLEWARE`: A list of middleware to be used in the order defined in this list.
7. `ROOT_URLCONF`: The Python import path to your root URL configuration.
8. `TEMPLATES`: A list of configurations for Django's template engine.
9. `WSGI_APPLICATION`: The Python import path to the WSGI application object.
10. `DATABASES`: The settings for all databases to be used with Django.
11. `AUTH_PASSWORD_VALIDATORS`: A list of validators used to check the strength of passwords.
12. `LANGUAGE_CODE` and `TIME_ZONE`: Settings for internationalization.
13. `USE_I18N` and `USE_TZ`: Boolean values specifying whether Django should use internationalization and timezone support.
14. `STATIC_URL`: The URL to use when referring to static files.
15. `DEFAULT_AUTO_FIELD`: The default primary key to use for models.

- This file contains configurations and settings for the Django project. Each setting has a specific purpose and altering these settings affects how the Django project works.

# urls.py
- The urls.py file in the munch_backend project is responsible for routing URLs to the appropriate views. It contains a list called urlpatterns which holds the paths for the application.

Currently, there are two paths defined:

- The admin path which leads to Django’s admin site.
- The root ('') path which includes all URLs from the munchapp application.
- This setup means that the admin interface can be accessed by appending /admin/ to the base URL, and the URLs defined in munchapp are included at the root URL (/).

# wsgi.py
- The provided script is the WSGI (Web Server Gateway Interface) configuration for the munch_backend Django project. Here’s a summary of what it does:

- It imports the os module and the get_wsgi_application function from django.core.wsgi.
- It sets the default Django settings module to 'munch_backend.settings' using the os.environ.setdefault method. This means that when this script is run, it will use the settings defined in the munch_backend.settings module.
- It creates an instance of a WSGI application using the get_wsgi_application function and assigns it to the application variable. This application can then be used by any WSGI-compatible web server to serve the Django application.
- This configuration is necessary for deploying the Django application to a production environment. For more information, you can refer to the official Django documentation on WSGI deployment.

# admin.py
- This code registers the Post model with the Django admin interface, allowing administrators to manage Post objects through the admin site. It enables functionalities such as viewing, adding, editing, and deleting Post instances.

# apps.py
- This code snippet defines a Django application configuration class named MunchappConfig for the app named 'munchapp'. It sets the default primary key field type for models in the app to BigAutoField.

# hours.py
This code is scrapes RPI dining website for information about dining locations and their hours of operation. This is what it does:

- The script imports the `requests` and `BeautifulSoup` libraries, which are used for making HTTP requests and parsing HTML content, respectively.
- The `URL` variable is set to the webpage that will be scraped.
- The `parse_information(soup)` function takes a BeautifulSoup object as an argument, which represents the parsed HTML content of the page. It finds all dining groups on the page, iterates through each group, and extracts the name and hours of each location within the group. The function returns a dictionary where the keys are location names and the values are lists of strings representing the hours for each location.
- The `get_hours(location_name, locations_hours)` function takes a location name and the dictionary of location hours as arguments. It returns a list of strings representing the hours for the specified location.
- The `get_locations(location_hours)` function takes the dictionary of location hours as an argument. It returns a list of all location names.

This is used to provide users with up-to-date information about dining hall locations and their hours of operation.

# location.py
- The `find_student_location()` function retrieves the location of a student based on their IP address. It uses the geocoder library to get the geographical coordinates (latitude and longitude) of the user's IP address. If successful, it returns the latitude and longitude. If there's an error during the process, it raises a SystemError with an appropriate message.

- The `find_address_location()` function retrieves the geographical coordinates (latitude and longitude) of a given address using the geocoder library. It sends a request to the Google Maps Geocoding API, passing the address and an API key as parameters. If the location retrieval is successful, it returns the latitude and longitude of the address. If an error occurs during the process, it raises a SystemError with an appropriate message.

- The `calculate_walking_time()` function calculates the walking time and distance between an origin and a destination using the Google Maps Distance Matrix API. It sends a request to the API with the specified origin and destination, specifying the travel mode as walking. If the request is successful, it iterates through the steps of the directions and calculates the total distance and duration of the walk. If an error occurs during the process, it raises a SystemError with an appropriate message. Finally, it returns a tuple containing the total distance and duration of the walk.

- The `find_closest_locations()` function determines the closest dining hall to a student's location based on walking time. It retrieves the student's location and the locations of several dining halls. Then, it calculates the walking time from the student's location to each dining hall using the Google Maps Distance Matrix API. After sorting the walking times to find the shortest one, it returns the location of the dining hall corresponding to the shortest walking time, indicating the closest dining hall to the student's location.

- The `display_closest_dining_hall()` function generates a map showing the route from the student's location to the closest dining hall. It determines the closest dining hall using the find_closest_locations function and creates a map centered at the user's location. Then, it adds markers for the student's location and the nearest dining hall, retrieves walking directions between them, and adds a polyline to represent the route. Finally, it saves the map as an HTML file and provides feedback on the map generation process. If no dining halls are found, it prints a message indicating the absence of dining halls.

- The `get_walking_directions()` function sends a request to the Google Maps Directions API to obtain walking directions between two points. It specifies the origin and destination coordinates, travel mode as walking, and includes a Google Maps API key in the request parameters. After receiving a response, it extracts the polyline points representing the walking route from the JSON data and returns them.

- The `get_current_weather()` function retrieves and parses weather data for a given location from the OpenWeatherMap API. The functiopn begins by defining the API key and the base URL for the OpenWeatherMap API. It then makes a GET request to the API, passing the location and API key as parameters. If the request in unsuccessful, it rases an exception. If it is successful, it parses the weather data from the response. It then returns the main condition, a more detail description, and the current temperature in Fahrenehit and Celsius.

# models.py
This is a Django model for a `Post` object. This is what it does:

- `title`: This is a `CharField` which is a string field in Django. The `max_length` attribute is set to 100, meaning the title of the post can be up to 100 characters long.
- `content`: This is a `TextField`, which is a large text field in Django. There's no limit set on its size, allowing for long descriptions.
- `date_posted`: This is a `DateTimeField`. The `default` attribute is set to `timezone.now`, meaning that by default, the date and time the post was created will be set to the current date and time.
- `author`: This is a `ForeignKey` field which creates a many-to-one relationship. It links each post to a `User` object. The `on_delete=models.CASCADE` attribute means that if the user who authored a post is deleted, the post will also be deleted.
- `__str__`: This is a special method in Python classes which returns a string representation of the object. Here, it's set to return the `title` of the `Post` object.

If any changes are made to this model, migrations must be made by using the command `python manage.py makemigrations` to apply those changes to the database.

# tests.py
This is just a testing file to help catch errors and to ensure that code is working as expected.

# testLocations.py
This is a file that tests the location class in the follwing way: 

- The `calculate_distance()` function calculates the distance between two given locations using the Haversine Distance Formula
- The `display_closest_dining_hall()` function calls multiple mehtods from the location class and implements it to create a map. The map marks two locations, the user and the closest dining hall, and provides walking directions to the destination. A map with a line is displayed to the frontend in order to provide easy functionality to the user.

# urls.py
This Django URL configuration specifies the URL patterns for a web application. Here's a summary of what it does:

1. **`/menu/`**: Maps the URL path '/menu/' to the `home` view function defined in the `views` module. It assigns the name 'munch-home' to this URL pattern.

2. **`/menu/sage/`**: Maps the URL path '/menu/sage/' to the `menu_sage` view function defined in the `views` module. It assigns the name 'menu_sage' to this URL pattern.

3. **`/menu/commons/`**: Maps the URL path '/menu/commons/' to the `menu_commons` view function defined in the `views` module. It assigns the name 'menu_commons' to this URL pattern.

4. **`/menu/blitman/`**: Maps the URL path '/menu/blitman/' to the `menu_blitman` view function defined in the `views` module. It assigns the name 'menu_blitman' to this URL pattern.

5. **`/menu/barh/`**: Maps the URL path '/menu/barh/' to the `menu_barh` view function defined in the `views` module. It assigns the name 'menu_barh' to this URL pattern.

6. **`/about/`**: Maps the URL path '/about/' to the `about` view function defined in the `views` module. It assigns the name 'about' to this URL pattern.

In summary, this URL configuration defines routes for accessing various views within the web application, such as displaying menus for different dining halls and an about page. Each route corresponds to a specific view function defined in the `views` module.


# views.py
- The `get_day()` function returns the current day of the month as a string.
It retrieves the day from the current date and time using the `datetime.now()`
function and returns it as a string.

- The `savingJson()` function saves a given dictionary (saved_dict) to a
JSON file with a specified name (name). It creates a folder named
"menus" if it doesn't exist, constructs the file path within that folder,
and writes the dictionary content to the JSON file with an indentation of 4 for readability.

- The `get_menu()` function retrieves menu data from a specified URL, parses it, and organizes it into breakfast, brunch, lunch, and dinner categories. It then saves this data into a JSON file named dininghall_data.json and returns it in a structured format along with the timestamp of the last update. If cached data for the current date exists, it returns that data; otherwise, it retrieves new data and updates the cache.

- The `get_current_time()` function retrieves the current date and time, formats them, and returns them as a dictionary with keys "date" and "time".

- The `get_hrs()` function fetches and organizes the operating hours of a dining establishment based on its name. It constructs a URL, sends a request to the webpage, parses the content, extracts the operating hour details for each meal and day, and returns them as a list of formatted strings.

- The `menu_sage` function retrieves the menu and operating hours for the Russell Sage dining hall, constructs a context containing this data along with the dining hall name, and renders a template to display this information on a web page.

- The `menu_commons` function retrieves the menu and operating hours for the Commons dining hall, constructs a context containing this data along with the dining hall name, and renders a template to display this information on a web page.

- The `menu_blitman` function retrieves the menu and operating hours for the Blitman dining hall, constructs a context containing this data along with the dining hall name, and renders a template to display this information on a web page.

- The `menu_barh` function retrieves the menu and operating hours for the BARH dining hall, constructs a context containing this data along with the dining hall name, and renders a template to display this information on a web page.

- The `about` function is a view function that returns an HTTP response containing an HTML string. This HTML string includes a level-one heading displaying the title "RCOS Munch Dining Hall Project RPI". When a user accesses the corresponding URL in a web browser, they will see this heading displayed on the page.

- The `home` function retrieves all posts from the database, passes them along with a title to the 'index.html' template, renders the template with the provided context, and returns the rendered template as an HTTP response. It's likely used to display posts on the home page of a web application.

# manage.py
This Python script is a command-line utility for running administrative tasks in a Django application. Here's a summary of what it does:

- The script sets the environment variable `DJANGO_SETTINGS_MODULE` to `'munch_backend.settings'`. This variable tells Django to use the settings file at that path.
- It then attempts to import the `execute_from_command_line` function from `django.core.management`. This function is responsible for executing Django management commands from the command line.
- If the import fails, it raises an `ImportError` with a helpful message suggesting that Django might not be installed or the virtual environment might not be activated.
- If the import is successful, it calls `execute_from_command_line(sys.argv)`, which executes the Django command passed in the command line arguments.
- The script is intended to be run as a standalone program. The `if __name__ == '__main__':` line ensures that the `main()` function is called only when the script is executed directly, not when it is imported as a module.

This script is typically placed in the root directory of a Django project and is used to manage tasks such as running the server, running tests, creating migrations, and more. It's a crucial part of any Django project (run in command-line: python manage.py runserver).
