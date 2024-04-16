# asgi.py
- fill in below

# settings.py
- fill in below

# urls.py
- fill in below

# wsgi.py
- fill in below

# admin.py
- This code registers the Post model with the Django admin interface, allowing administrators to manage Post objects through the admin site. It enables functionalities such as viewing, adding, editing, and deleting Post instances.

# apps.py
- This code snippet defines a Django application configuration class named MunchappConfig for the app named 'munchapp'. It sets the default primary key field type for models in the app to BigAutoField.

# hours.py
- fill in below

# location.py
- The `find_student_location()` function retrieves the location of a student based on their IP address. It uses the geocoder library to get the geographical coordinates (latitude and longitude) of the user's IP address. If successful, it returns the latitude and longitude. If there's an error during the process, it raises a SystemError with an appropriate message.

- The `find_address_location()` function retrieves the geographical coordinates (latitude and longitude) of a given address using the geocoder library. It sends a request to the Google Maps Geocoding API, passing the address and an API key as parameters. If the location retrieval is successful, it returns the latitude and longitude of the address. If an error occurs during the process, it raises a SystemError with an appropriate message.

- The `calculate_walking_time()` function calculates the walking time and distance between an origin and a destination using the Google Maps Distance Matrix API. It sends a request to the API with the specified origin and destination, specifying the travel mode as walking. If the request is successful, it iterates through the steps of the directions and calculates the total distance and duration of the walk. If an error occurs during the process, it raises a SystemError with an appropriate message. Finally, it returns a tuple containing the total distance and duration of the walk.

- The `find_closest_locations()` function determines the closest dining hall to a student's location based on walking time. It retrieves the student's location and the locations of several dining halls. Then, it calculates the walking time from the student's location to each dining hall using the Google Maps Distance Matrix API. After sorting the walking times to find the shortest one, it returns the location of the dining hall corresponding to the shortest walking time, indicating the closest dining hall to the student's location.

- The `display_closest_dining_hall()` function generates a map showing the route from the student's location to the closest dining hall. It determines the closest dining hall using the find_closest_locations function and creates a map centered at the user's location. Then, it adds markers for the student's location and the nearest dining hall, retrieves walking directions between them, and adds a polyline to represent the route. Finally, it saves the map as an HTML file and provides feedback on the map generation process. If no dining halls are found, it prints a message indicating the absence of dining halls.

- The `get_walking_directions()` function sends a request to the Google Maps Directions API to obtain walking directions between two points. It specifies the origin and destination coordinates, travel mode as walking, and includes a Google Maps API key in the request parameters. After receiving a response, it extracts the polyline points representing the walking route from the JSON data and returns them.

# models.py
- fill in below

# tasks.py
- fill in below

# tests.py
- fill in below



# urls.py
- This Django URL configuration specifies the URL patterns for a web application. Here's a summary of what it does:

1. **`/menu/`**: Maps the URL path '/menu/' to the `home` view function defined in the `views` module. It assigns the name 'munch-home' to this URL pattern.

2. **`/menu/sage/`**: Maps the URL path '/menu/sage/' to the `menu_sage` view function defined in the `views` module. It assigns the name 'menu_sage' to this URL pattern.

3. **`/menu/commons/`**: Maps the URL path '/menu/commons/' to the `menu_commons` view function defined in the `views` module. It assigns the name 'menu_commons' to this URL pattern.

4. **`/menu/blitman/`**: Maps the URL path '/menu/blitman/' to the `menu_blitman` view function defined in the `views` module. It assigns the name 'menu_blitman' to this URL pattern.

5. **`/menu/barh/`**: Maps the URL path '/menu/barh/' to the `menu_barh` view function defined in the `views` module. It assigns the name 'menu_barh' to this URL pattern.

6. **`/about/`**: Maps the URL path '/about/' to the `about` view function defined in the `views` module. It assigns the name 'about' to this URL pattern.

- In summary, this URL configuration defines routes for accessing various views within the web application, such as displaying menus for different dining halls and an about page. Each route corresponds to a specific view function defined in the `views` module.


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
- fill in below