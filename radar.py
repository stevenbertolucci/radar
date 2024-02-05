# Author: Steven Bertolucci
# Course: CS469 - Real World Projects - Winter 2024
# File: radar.py
# Description:
#  -------------------------------------------------------------------
#
#       Radar is a personal project of mine for the CS469 course
#       at Oregon State University. Radar is a CLI software that
#       incorporates APIs for weather, Local News, Time Zone, Tax
#       Rates, and a Zip Code. The password generator is a bonus
#       feature that users can generate for personal use.
#
#  -------------------------------------------------------------------
import os
import sys
import time
import platform
import requests
import datetime

# Get operating system name
operating_system = sys.platform

# Get the current date and time
current_datetime = datetime.datetime.now()

# Extract the date and time components
current_date = current_datetime.date()

# Define ANSI escape codes for colors
red_color_profile = "\033[31m"       # Red text
green_color_profile = "\033[32m"     # Green text
yellow_color_profile = "\033[33m"    # Yellow text
blue_color_profile = "\033[34m"      # Blue text
purple_color_profile = "\033[35m"    # Purple text
reset_color_profile = "\033[0m"      # Default CLI text color (gray)

# Global Variables
has_displayed_intro = False

########################################################################################################################
#                                                                                                                      #
#                                         START OF FUNCTION DECLARATIONS                                               #
#                                                                                                                      #
########################################################################################################################


def display_intro():
    # Display intro banner and copyrighted statements
    print(
        f"{green_color_profile}-----------------------------------------------------------------------------------------"
        f"-------------------------------")
    radar_ascii = f"""{green_color_profile}
                                                                 dddddddd
              RRRRRRRRRRRRRRRRR                                  d::::::d
              R::::::::::::::::R                                 d::::::d
              R::::::RRRRRR:::::R                                d::::::d
              RR:::::R     R:::::R                               d::::::d
                R::::R     R:::::R    aaaaaaaaaaaaa        ddddddddd:::::d     aaaaaaaaaaaaa    rrrrr   rrrrrrrrr
                R::::R     R:::::R    a::::::::::::a     dd::::::::::::::d     a::::::::::::a   r::::rrr:::::::::r
                R::::RRRRRR:::::R     aaaaaaaaa:::::a   d::::::::::::::::d     aaaaaaaaa:::::a  r:::::::::::::::::r
                R:::::::::::::RR               a::::a  d:::::::ddddd:::::d              a::::a  rr::::::rrrrr::::::r
                R::::RRRRRR:::::R       aaaaaaa:::::a  d::::::d    d:::::d       aaaaaaa:::::a   r:::::r     r:::::r
                R::::R     R:::::R    aa::::::::::::a  d:::::d     d:::::d     aa::::::::::::a   r:::::r     rrrrrrr
                R::::R     R:::::R   a::::aaaa::::::a  d:::::d     d:::::d    a::::aaaa::::::a   r:::::r
                R::::R     R:::::R  a::::a    a:::::a  d:::::d     d:::::d   a::::a    a:::::a   r:::::r
              RR:::::R     R:::::R  a::::a    a:::::a  d::::::ddddd::::::dd  a::::a    a:::::a   r:::::r
              R::::::R     R:::::R  a:::::aaaa::::::a   d:::::::::::::::::d  a:::::aaaa::::::a   r:::::r
              R::::::R     R:::::R   a::::::::::aa:::a   d:::::::::ddd::::d   a::::::::::aa:::a  r:::::r
              RRRRRRRR     RRRRRRR    aaaaaaaaaa  aaaa    ddddddddd   ddddd    aaaaaaaaaa  aaaa  rrrrrrr   
    {reset_color_profile}"""

    print(radar_ascii)
    print(f"\t\t\t\t{purple_color_profile}    ASCII text was generated using a web-based generator: "
          f"\n\t\t\t{blue_color_profile}    https://patorjk.com/software/taag/#p=display&h=2&v=3&f=Doh&t=Radar")
    print(f"\t\t\t\t\t{purple_color_profile}    Retrieved from: Patrick Gillespie")
    print(f"\n\t\t\t\t\t{red_color_profile}    Copyrighted by Steven Bertolucci\u00A9")
    print(
        f"{green_color_profile}-----------------------------------------------------------------------------------------"
        f"-------------------------------{reset_color_profile}")


def farewell():
    """
    Function farewell that display a farewell message to user.
    Output will be in yellow with a hand-waving 'bye' emoji.
    """

    print(f"\n\t\t\t\t         \U0001F44B{yellow_color_profile} Thank you for using Radar! Bye! \U0001F44B "
          f"{reset_color_profile}\n\n")
    time.sleep(3)
    if operating_system == 'win32':
        os.system('cls')
    if operating_system == 'linux' or operating_system == 'darwin':
        os.system('clear')
    exit(0)


def authentication():
    """
        Function authentication generates am access token for
        verified Precisely users and then returns the token
        for API calls.
    """

    # Encode your API Key and Secret
    base64 = "NkIzVmFHSlF2RWg5em1sbmhaNXRBYVNGcGFzVnlEa0c6MEdXejUwQ3ZDYXdPbmNaeA=="

    # Set headers
    headers = {
        'Authorization': f'Basic {base64}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {
        'grant_type': 'client_credentials'
    }

    # Make POST request
    token_url = 'https://api.precisely.com/oauth/token'
    response = requests.post(token_url, headers=headers, data=data)

    if response.status_code == 200:
        token_data = response.json()
        access_token = token_data.get('access_token')
    else:
        print(f"Error: {response.status_code}")

    return access_token


def validate_input(usr_input):
    """
    Function validate_input that takes in user_input as a parameter
    and validates to see if User entered 'quit' or a legitimate zip code.
    """

    if usr_input.lower() == 'quit':
        if operating_system == 'win32':
            os.system('cls')
        if operating_system == 'linux' or operating_system == 'darwin':
            os.system('clear')
        farewell()
        time.sleep(3)
        exit(0)

    if len(usr_input) != 5:
        clear_selected_line()
        print("\033[31mInvalid zip code. Please enter a 5 digit zipcode.\033[0m")
        success = False
    else:
        success = True

    return success


def clear_selected_line():
    """
    Function clear_selected_line that removes a line in
    the output window.
    """

    sys.stdout.write("\033[F")       # Move cursor up one line
    sys.stdout.write("\033[K")       # Clear line from cursor position to the end


def get_location_details():
    """
    Function get_location_details gathers more details regarding
    the location of the zip code that the user inputted. This API
    sends the zip code to Google Geocoding API and receives the
    city name, longitude, and latitude for other API calls.
    This is needed to display city name in some of the options that
    the user selected. PreciselyAPI requires latitude and longitude
    to display tax rates. LocalNewsAPI requires city names to display
    local news.
    """

    global city_name
    global latitude
    global longitude

    google_api = "AIzaSyBLkIviPn0C-P7gK2civVkI4hoUXvfv3ck"
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={user_input}&key={google_api}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # print(data)
        if data['status'] == 'OK':
            city = None
            latitude = None
            longitude = None

            for result in data['results']:
                for component in result['address_components']:
                    if 'locality' in component['types']:
                        city = component['long_name']
                        city_name = component['long_name']
                    if 'geometry' in result and 'location' in result['geometry']:
                        latitude = result['geometry']['location']['lat']
                        longitude = result['geometry']['location']['lng']

                    if city and latitude is not None and longitude is not None:
                        break


def get_weather(city):
    """
    Function get_weather that requests weather info by calling
    WeatherAPI to retrieve weather information for that zip code.
    """

    print(f"\033[31mRetrieving Weather information for {city}. Please wait... \033[0m")
    time.sleep(0.5)
    api_key = 'dd86ae75f9b94cafb28195718241501'
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={user_input}&aqi=no'

    response = requests.get(url)

    if response.status_code == 200:
        clear_selected_line()
        data = response.json()
        print("\033[36mWeather information for", city + ":\033[0m")
        print("Name:", data["location"]["name"])
        print("Region:", data["location"]["region"])
        print("Temperature (F):", data["current"]["temp_f"])
        print("Condition:", data["current"]["condition"]["text"])
        print("Wind Speed (mph):", data["current"]["wind_mph"])
        print("Wind Direction:", data["current"]["wind_dir"])
        print("Humidity:", data["current"]["humidity"], "%")
        print("Feels Like (F):", data["current"]["feelslike_f"])
        print("UV Index:", data["current"]["uv"])
    else:
        clear_selected_line()
        print("Error retrieving weather")

    input("\n\033[32mPress Enter to Continue...\033[0m")
    if operating_system == 'win32':
        os.system('cls')
    if operating_system == 'linux' or operating_system == 'darwin':
        os.system('clear')


def get_local_news(city):
    """
    Function get_local_news sends a request to NewsAPI.org to
    retrieve local news of that zip code. NewsAPI uses keywords
    like city name, so this function retrieves city name from
    Google Geocoding API and then searches news for that city.
    """

    print("\033[31mRetrieving News. Please wait... \033[0m")
    time.sleep(0.5)
    page = 1
    articles_per_page = 10

    while True:
        url = (f"https://newsapi.org/v2/everything?q={city_name}&from=2024-01-05&to={current_date}&sortBy="
               f"publishedAt&apiKey=342d3256cc1c4b2cb71cfb4a00ba9a92&language=en")

        response = requests.get(url)

        if response.status_code == 200:
            clear_selected_line()
            data = response.json()
            # print(data)
            articles = data.get("articles", [])
            total_results = data.get("totalResults", [])

            if articles:
                start_index = (page - 1) * articles_per_page
                end_index = start_index + articles_per_page

                if page == 1:
                    print("\033[36mNews for", city + ":\033[0m")

                for index, article in enumerate(articles[start_index:end_index], start=start_index + 1):
                    source_name = article.get("source", {}).get("name")
                    author = article.get("author")
                    title = article.get("title")
                    url = article.get("url")
                    published_at = article.get("publishedAt")

                    # Check if any of the relevant fields contains [Removed]
                    if "[Removed]" not in source_name and title != "[Removed]" and url != "https://removed.com":
                        published_at = datetime.datetime.fromisoformat(published_at.replace("Z", "+00:00"))
                        formatted_published_at = published_at.strftime("%Y-%m-%d")

                        print(f"Article {index}:")
                        print("Published At:", formatted_published_at)
                        print("Source:", source_name)
                        print("Author:", author)
                        print("Title:", title)
                        print("URL:", url)
                        print("\n")
                print("\t\t\t\t\t\t\t\033[31mPage:", page, "\033[0m")
                print("\033[33m+---------------------------------------------------------------------------------------"
                      "-------------------------------+\033[0m")
                page += 1

                # Check if there are more pages or exit
                if end_index >= total_results or end_index >= 100:
                    print("\nNo more articles to display.")
                    input("\033[32mPress Enter to continue...\033[0m")
                    break

                else:
                    # Ask the user to press Enter to continue or exit
                    usr_keystroke = input("\n\033[32mPress Enter to continue or type 'exit' to exit...\033[0m")
                    if usr_keystroke.lower() == 'exit':
                        break

        else:
            print(f"Error: {response.status_code}")
            break

    if operating_system == 'win32':
        os.system('cls')
    if operating_system == 'linux' or operating_system == 'darwin':
        os.system('clear')


def get_time(city, latitude, longitude):
    """
    Function get_time retrieves the current time and time zone
    of the location that the user inputted. No API key was required,
    and it is free to use.
    """

    print(f"\033[31mRetrieving time information for {city}. Please wait... \033[0m")
    time.sleep(0.5)
    url = f"https://timeapi.io/api/Time/current/coordinate?latitude={latitude}&longitude={longitude}"

    parameters = {
        "format": "json",
    }

    response = requests.get(url, params=parameters)

    if response.status_code == 200:
        clear_selected_line()
        data = response.json()
        timezone = data.get("timeZone")
        current_time = data.get("time")
        print(f"\033[36mTime Info for {city}:\033[0m", "\nTime Zone: ", timezone, "\nTime: ", current_time)
    else:
        print(f"Error: {response.status_code}")

    input("\n\033[32mPress Enter to continue...\033[0m")
    if operating_system == 'win32':
        os.system('cls')
    if operating_system == 'linux' or operating_system == 'darwin':
        os.system('clear')


def get_tax_rates(lat, long):
    """
        Function get_tax_rate retrieves the tax rate of the zip code
        by using the longitudinal and latitudinal coordinates. This
        API call requires authorization using tokens. Documentation
        on how to generate token is found on PreciselyAPI website:
        https://docs.precisely.services/docs/sftw/precisely-apis/main/en-us/webhelp/apis/Getting%20Started/
        generating_an_oauth_token.html
    """
    print("\033[31mAuthentication connection... Please wait\033[0m")
    time.sleep(1.0)
    token = authentication()
    clear_selected_line()

    # Print status message
    print("\033[31mRetrieving tax rates...\033[0m")
    time.sleep(0.5)
    url = f"https://api.precisely.com/localtax/v1/taxrate/General/bylocation?latitude={lat}&longitude={long}"

    # Set the Authorization header with the access token
    headers = {
        'Authorization': f'Bearer {token}'
    }

    # Get response
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        clear_selected_line()
        data = response.json()
        print(data)

        # Access the "TotalTaxRate" from the "salesTax" object
        total_tax_rate = data.get("salesTax", {}).get("totalTaxRate", None)

        if total_tax_rate is not None:
            print("\033[36mTotal Tax Rate:\033[0m", total_tax_rate)
        else:
            print("Total Tax Rate information not found.")
    else:
        print(f"Error: {response.status_code}")

    input("\n\033[32mPress Enter to continue...\033[0m")
    if operating_system == 'win32':
        os.system('cls')
    if operating_system == 'linux' or operating_system == 'darwin':
        os.system('clear')

########################################################################################################################
#                                                                                                                      #
#                                          END OF FUNCTION DECLARATIONS                                                #
#                                                                                                                      #
########################################################################################################################


# Display Intro banner
display_intro()

# Display prompt to user and wait for them to hit 'Enter'
input("\n\n\n\n\t\t\t             \U0001F44B Welcome to Radar! Press 'enter' to continue...")
clear_selected_line()

while True:

    # Get User input
    user_input = input(f"\n{yellow_color_profile}Enter a zip code: {reset_color_profile}")

    # Validate User input
    result = validate_input(user_input)
    if not result:
        continue
    else:
        has_displayed_intro = True
        break

# Get more details regarding zip code (city name, latitude, and longitude)
get_location_details()

while True:
    if has_displayed_intro:
        if operating_system == 'win32':
            os.system('cls')
        if operating_system == 'linux' or operating_system == 'darwin':
            os.system('clear')
        display_intro()
    print("\n\t1. Weather\n")
    print(f"\t2. News for {city_name}\n")
    print("\t3. Time Zone\n")
    print("\t4. Tax Rates\n")
    print("\t5. Enter New Zip Code\n")
    print("\t6. Generate Password\n")
    print("\t7. Exit\n")

    while True:

        user_choice = input(f"{yellow_color_profile}Pick an option: {reset_color_profile}")

        if user_choice == 'quit':
            if operating_system == 'win32':
                os.system('cls')
            if operating_system == 'linux' or operating_system == 'darwin':
                os.system('clear')
            farewell()
        elif user_choice < '1' or user_choice > '7':
            clear_selected_line()
            print("\033[31mPlease pick a valid option.\033[0m")
            continue
        else:
            if operating_system == 'win32':
                os.system('cls')
            if operating_system == 'linux' or operating_system == 'darwin':
                os.system('clear')
            display_intro()
            break

    if user_choice.lower() == 'quit':
        if operating_system == 'win32':
            os.system('cls')
        if operating_system == 'linux' or operating_system == 'darwin':
            os.system('clear')
        farewell()

    elif user_choice == '1':
        get_weather(city_name)

    elif user_choice == '2':
        get_local_news(city_name)

    elif user_choice == '3':
        get_time(city_name, latitude, longitude)

    elif user_choice == '4':
        get_tax_rates(latitude, longitude)

    elif user_choice == '5':
        if operating_system == 'win32':
            os.system('cls')
        if operating_system == 'linux' or operating_system == 'darwin':
            os.system('clear')
        display_intro()
        while True:
            user_input = input("\033[33mEnter New Zip Code: \033[0m")
            result = validate_input(user_input)
            if not result:
                continue
            else:
                # Get more details regarding zip code (city name, latitude, and longitude)
                get_location_details()
                break

    elif user_choice == '6':
        input("Password Generator Coming soon... Press Enter to continue")
        if operating_system == 'win32':
            os.system('cls')
        if operating_system == 'linux' or operating_system == 'darwin':
            os.system('clear')

    elif user_choice == '7':
        if operating_system == 'win32':
            os.system('cls')
        if operating_system == 'linux' or operating_system == 'darwin':
            os.system('clear')
        farewell()
