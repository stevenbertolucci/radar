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
import random
import sys
import time
import platform
import requests
import datetime
import urllib.request
import webbrowser
import subprocess
from temperature import temperature_colors
from conditions import condition
from uv_index import uv_index
from blackjack import play_blackjack
from bs4 import BeautifulSoup
# Windows when using pycaw
from ctypes import cast, POINTER
try:
    from comtypes import CLSCTX_ALL
except ModuleNotFoundError:
    CLSCTX_ALL = None  # Define CLSCTX_ALL as None or handle the absence of comtypes accordingly
    # print("Warning: comtypes module not found. Some functionality may be limited.")

try:
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
except ModuleNotFoundError:
    print("Warning: pycaw module not found. Some functionality may be limited.")


# Get operating system name
operating_system = sys.platform

# Get the current date and time
current_datetime = datetime.datetime.now()
a_week_before_current_date = current_datetime - datetime.timedelta(days=7)

# Extract the date and time components
current_date = current_datetime.date()

# Define ANSI escape codes for colors
red_color_profile = "\033[31m"       # Red text
green_color_profile = "\033[32m"     # Green text
yellow_color_profile = "\033[33m"    # Yellow text
blue_color_profile = "\033[34m"      # Blue text
br_blue_color_profile = "\033[94m"   # Bright Blue text
purple_color_profile = "\033[35m"    # Purple text
cyan_color_profile = "\033[36m"      # Cyan text
reset_color_profile = "\033[0m"      # Default CLI text color (gray)

# Global Variables
has_displayed_intro = False

########################################################################################################################
#                                                                                                                      #
#                                         START OF FUNCTION DECLARATIONS                                               #
#                                                                                                                      #
########################################################################################################################


def display_intro():
    """
    Function display_intro displays a welcome message to user.
    Output will be in yellow with a hand-waving 'hi' emoji.
    """

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


def display_weather_intro():
    print(
        f"{cyan_color_profile}-------------------------------------------------------------")

    weather_ascii = f"""
                              _   _               
                             | | | |              
          __      _____  __ _| |_| |__   ___ _ __ 
          \ \ /\ / / _ \/ _` | __| '_ \ / _ \ '__|
           \ V  V /  __/ (_| | |_| | | |  __/ |   
            \_/\_/ \___|\__,_|\__|_| |_|\___|_|   
    {reset_color_profile}"""

    print(weather_ascii)

    print(
        f"{cyan_color_profile}-------------------------------------------------------------{reset_color_profile}")


def display_local_news_intro():
    print(
        f"{red_color_profile}-------------------------------------------------------------")

    local_news_ascii = f"""
        __                     __   _   __                 
       / /   ____  _________ _/ /  / | / /__ _      _______
      / /   / __ \/ ___/ __ `/ /  /  |/ / _ \ | /| / / ___/
     / /___/ /_/ / /__/ /_/ / /  / /|  /  __/ |/ |/ (__  ) 
    /_____/\____/\___/\__,_/_/  /_/ |_/\___/|__/|__/____/  
    {reset_color_profile}"""

    print(local_news_ascii)

    print(
        f"{red_color_profile}-------------------------------------------------------------{reset_color_profile}")


def display_news_intro():
    print(
        f"{yellow_color_profile}-----------------------------------------")

    news_ascii = f"""
         _   __                 
        / | / /__ _      _______
       /  |/ / _ \ | /| / / ___/
      / /|  /  __/ |/ |/ (__  ) 
     /_/ |_/\___/|__/|__/____/  
    {reset_color_profile}"""

    print(news_ascii)

    print(
        f"{yellow_color_profile}----------------------------------------{reset_color_profile}")


def display_time_intro():
    print(
        f"{purple_color_profile}---------------------------------------------------------------------------------------"
        f"---------")

    time_ascii = f"""
         .----------------.  .----------------.  .----------------.  .----------------. 
        | .--------------. || .--------------. || .--------------. || .--------------. |
        | |  _________   | || |     _____    | || | ____    ____ | || |  _________   | |
        | | |  _   _  |  | || |    |_   _|   | || ||_   \  /   _|| || | |_   ___  |  | |
        | | |_/ | | \_|  | || |      | |     | || |  |   \/   |  | || |   | |_  \_|  | |
        | |     | |      | || |      | |     | || |  | |\  /| |  | || |   |  _|  _   | |
        | |    _| |_     | || |     _| |_    | || | _| |_\/_| |_ | || |  _| |___/ |  | |
        | |   |_____|    | || |    |_____|   | || ||_____||_____|| || | |_________|  | |
        | |              | || |              | || |              | || |              | |
        | '--------------' || '--------------' || '--------------' || '--------------' |
         '----------------'  '----------------'  '----------------'  '----------------' 
    {reset_color_profile}"""

    print(time_ascii)
    print(
        f"{purple_color_profile}---------------------------------------------------------------------------------------"
        f"---------{reset_color_profile}")


def display_tax_intro():
    print(
        f"{red_color_profile}-----------------------------------------------------------------------"
        f"---------")

    tax_ascii = """
          _____                             ___             _             
         |_   _|  __ _    __ __     o O O  | _ \   __ _    | |_     ___   
           | |   / _` |   \ \ /    o       |   /  / _` |   |  _|   / -_)  
          _|_|_  \__,_|   /_\_\   TS__[O]  |_|_\  \__,_|   _\__|   \___|  
        _|\"\"\"\"\"|_|\"\"\"\"\"|_|\"\"\"\"\"| {======|_|\"\"\"\"\"|_|\"\"\"\"\"|_|\"\"\"\"\"|_|\"\"\"\"\"|
        "`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
    """ + reset_color_profile

    print(tax_ascii)
    print(
        f"{red_color_profile}-----------------------------------------------------------------------"
        f"---------{reset_color_profile}")


def display_password_intro():
    print(
        f"{br_blue_color_profile}-----------------------------------------------------------------------"
        f"--------------------------------")

    password_ascii = f"""
         __        __   __        __   __   __      __   ___       ___  __       ___  __   __  
        |__)  /\  /__` /__` |  | /  \ |__) |  \    / _` |__  |\ | |__  |__)  /\   |  /  \ |__) 
        |    /~~\ .__/ .__/ |/\| \__/ |  \ |__/    \__> |___ | \| |___ |  \ /~~\  |  \__/ |  \ 
    {reset_color_profile}"""



    print(password_ascii)
    print(
        f"{br_blue_color_profile}-----------------------------------------------------------------------"
        f"--------------------------------{reset_color_profile}")


def display_top_secret_intro():
    print(
        f"{green_color_profile}-----------------------------------------------------------------------"
        f"-----------------------------------------------")

    top_secret_ascii = f"""
      ___ ___ ___   _____ ___  ___   ___ ___ ___ ___ ___ _____   ___   ___   ___ _   _ __  __ ___ _  _ _____ ___ 
     | __| _ )_ _| |_   _/ _ \| _ \ / __| __/ __| _ \ __|_   _| |   \ / _ \ / __| | | |  \/  | __| \| |_   _/ __|
     | _|| _ \| |    | || (_) |  _/ \__ \ _| (__|   / _|  | |   | |) | (_) | (__| |_| | |\/| | _|| .` | | | \__ \\
     |_| |___/___|   |_| \___/|_|   |___/___\___|_|_\___| |_|   |___/ \___/ \___|\___/|_|  |_|___|_|\_| |_| |___/
    {reset_color_profile}"""

    print(top_secret_ascii)
    print(
        f"{green_color_profile}-----------------------------------------------------------------------"
        f"-----------------------------------------------{reset_color_profile}")


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

    if usr_input.lower() == 'quit' or usr_input.lower() == 'exit':
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
        print(f"Temperature (F): {temperature_colors(data['current']['temp_f'])}{data['current']['temp_f']}\033[0m")
        print("Condition:", condition(data["current"]["condition"]["text"]), data["current"]["condition"]["text"], "\033[0m")
        print("Wind Speed (mph):", data["current"]["wind_mph"])
        print("Wind Direction:", data["current"]["wind_dir"])
        print("Humidity:", data["current"]["humidity"], "%")
        print("Feels Like (F):", data["current"]["feelslike_f"])
        print("UV Index:", uv_index(data["current"]["uv"]), data["current"]["uv"], "\033[0m")
    else:
        clear_selected_line()
        print("Error retrieving weather")

    input("\n\033[32mPress Enter to Continue...\033[0m")
    if operating_system == 'win32':
        os.system('cls')
    if operating_system == 'linux' or operating_system == 'darwin':
        os.system('clear')


def format_paragraph_with_max_words_per_line(paragraph, max_words_per_line=12):
    """
    Function to format a paragraph with a maximum number of 12 words per line.
    """

    words = paragraph.split()
    lines = []
    current_line = []

    for word in words:
        current_line.append(word)
        if len(current_line) >= max_words_per_line:
            lines.append(" ".join(current_line))
            current_line = []

    if current_line:
        lines.append(" ".join(current_line))

    return "\n".join(lines)


def get_article_content(url):
    """
    Function to fetch and parse the content of an article given its URL.
    """

    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            paragraphs = [p.get_text() for p in soup.find_all('p') if p.get_text()]

            # Filter out paragraphs with 3 words or less
            filtered_paragraphs = [p for p in paragraphs if len(p.split()) > 3]

            short_lines = [format_paragraph_with_max_words_per_line(p, max_words_per_line=12) for p in
                           filtered_paragraphs]
            formatted_text = "\n\n".join(short_lines)
            return formatted_text
    except Exception as e:
        print(f"Error fetching article content: {str(e)}")
        return ""


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
        url = (f"https://newsapi.org/v2/everything?q={city_name}&from={a_week_before_current_date}&to={current_date}&sortBy="
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
                    print("\033[36mNews for", city + ":\033[0m\n")

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

                        print(f"\033[33mArticle {index}:\033[0m")
                        print("Published At:", formatted_published_at)
                        print("Source:", source_name)
                        print("Author:", author)
                        print("Title:", title, "\n")

                        # Fetch and display the article content
                        article_content = get_article_content(url)
                        print("Content:")
                        print(article_content)

                        print("\033[36mURL:", url)
                        print("\n\033[0m")
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


def get_news():
    """
    Function get_news sends a request to NewsAPI.org to
    retrieve news of the user inputted term. NewsAPI uses keywords
    from search terms, so this function retrieves anything from
    the user and then searches news for that search term.
    """

    search_result = input("What would you like to read about? ")
    clear_selected_line()
    print("\033[31mRetrieving News. Please wait... \033[0m")
    time.sleep(0.5)
    page = 1
    articles_per_page = 10

    while True:
        url = (
            f"https://newsapi.org/v2/everything?q={search_result}&from={a_week_before_current_date}&to={current_date}"
            f"&sortBy=publishedAt&apiKey=342d3256cc1c4b2cb71cfb4a00ba9a92&language=en")

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
                    print("\033[36mNews about", search_result + ":\033[0m\n")

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

                        print(f"\033[33mArticle {index}:\033[0m")
                        print("Published At:", formatted_published_at)
                        print("Source:", source_name)
                        print("Author:", author)
                        print("Title:", title, "\n")

                        # Fetch and display the article content
                        article_content = get_article_content(url)
                        print("Content:")
                        print(article_content)

                        print("\033[36mURL:", url)
                        print("\n\033[0m")
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
        #print(data)

        # Extract and display relevant information
        city_info = data.get("jurisdiction", {}).get("place", {})
        city_info = city_info.get("name", "N/A")
        county_info = data.get("jurisdiction", {}).get("county", {})
        county_info = county_info.get("name", "N/A")
        state_info = data.get("jurisdiction", {}).get("state", {})
        state_info = state_info.get("name", "N/A")
        sales_tax = data.get("salesTax", {})
        total_tax_rate = sales_tax.get("totalTaxRate", "N/A")
        state_tax_rate = sales_tax.get("stateTaxRate", "N/A")
        county_tax_rate = sales_tax.get("countyTaxRate", "N/A")
        municipal_tax_rate = sales_tax.get("municipalTaxRate", "N/A")

        print("\033[36mCity:\033[0m", city_info)
        print("\033[36mCounty:\033[0m", county_info)
        print("\033[36mState:\033[0m", state_info)
        print("\033[36mTotal Tax Rate:\033[0m", total_tax_rate)
        print("\033[36mState Tax Rate:\033[0m", state_tax_rate)
        print("\033[36mCounty Tax Rate:\033[0m", county_tax_rate)
        print("\033[36mMunicipal Tax Rate:\033[0m", municipal_tax_rate)

    else:
        print(f"Error: {response.status_code}")

    input("\n\033[32mPress Enter to continue...\033[0m")
    if operating_system == 'win32':
        os.system('cls')
    if operating_system == 'linux' or operating_system == 'darwin':
        os.system('clear')


def generate_password():
    """
        Function generate_password is used to generate password
        with length of 8 to 32 characters. Users will be given
        an option to add special characters, uppercase letters,
        and numbers.
    """

    # Arrays that will contain special data
    lower_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']

    special_chars = ['/', '*', '.', '$', '~', '`', '!', '@', '#', '%', '^', '&', '(', ')', '_', '-', '+', '=',
                     '{', '[', '}', ']', '|', '\\', ':', ';', '"', "'", '<', '>', '?', '/']

    upper_chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                   'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # Start of Prompt
    passwd_length = int(input("How long would you like the password to be? (Minimum: 8 characters. Maximum: "
                        "32 characters): "))

    while True:
        if passwd_length < 8 or passwd_length > 32:
            passwd_length = int(input("Please enter a valid password length: "))
        else:
            break

    special_char_input = input("Would you like to include special characters? (Y/N): ")
    if special_char_input.lower() != 'y' and special_char_input.lower() != 'n':
        while True:
            special_char_input = input("Please enter 'Y' for yes and 'N' for no: ")
            if special_char_input.lower() == 'y' or special_char_input.lower() == 'n':
                break

    if special_char_input.lower() == 'y':
        special_char_input = True

    elif special_char_input.lower() == 'n':
        special_char_input = False

    uppercase_input = input("Would you like to include uppercase letters? (Y/N): ")
    if uppercase_input.lower() != 'y' and uppercase_input.lower() != 'n':
        while True:
            uppercase_input = input("Please enter 'Y' for yes and 'N' for no: ")
            if uppercase_input.lower() == 'y' or uppercase_input.lower() == 'n':
                break

    if uppercase_input.lower() == 'y':
        uppercase_input = True

    elif uppercase_input.lower() == 'n':
        uppercase_input = False

    numbers_input = input("Would you like to include numbers? (Y/N): ")
    if numbers_input.lower() != 'y' and numbers_input.lower() != 'n':
        while True:
            numbers_input = input("Please enter 'Y' for yes and 'N' for no: ")
            if numbers_input.lower() == 'y' or numbers_input.lower() == 'n':
                break

    if numbers_input.lower() == 'y':
        numbers_input = True

    elif numbers_input.lower() == 'n':
        numbers_input = False

    # Let user know that I am generating password
    print("\033[31mGenerating password...\033[0m")
    time.sleep(1.5)
    clear_selected_line()

    # If users do not want special characters, uppercase letters, and numbers,
    # generate a password that contains only lowercase numbers.
    if not special_char_input and not uppercase_input and not numbers_input:
        password = ''.join(random.choice(lower_chars) for _ in range(passwd_length))

    # If user wants upper case letters, generate a password with both lowercase
    # and uppercase letters
    elif not special_char_input and not numbers_input:
        characters = lower_chars + upper_chars
        password = ''.join(random.choice(characters) for _ in range(passwd_length))

    # If user wants numbers, generate a password with lowercase letters and
    # numbers.
    elif not special_char_input and not uppercase_input:
        characters = lower_chars + numbers
        password = ''.join(random.choice(characters) for _ in range(passwd_length))

    # If user wants special characters, generate a password with lowercase and
    # special characters.
    elif not numbers_input and not uppercase_input:
        characters = lower_chars + special_chars
        password = ''.join(random.choice(characters) for _ in range(passwd_length))

    # If user wants no special characters, generate a password with lowercase and
    # uppercase letters and numbers.
    elif not special_char_input:
        characters = lower_chars + upper_chars + numbers
        password = ''.join(random.choice(characters) for _ in range(passwd_length))

    # If user wants special characters and numbers, generate a password with lowercase letters,
    # special characters and numbers.
    elif not uppercase_input:
        characters = lower_chars + special_chars + numbers
        password = ''.join(random.choice(characters) for _ in range(passwd_length))

    # If user wants special characters and numbers, generate a password with lowercase letters,
    # special characters and numbers.
    elif not numbers_input:
        characters = lower_chars + special_chars + upper_chars
        password = ''.join(random.choice(characters) for _ in range(passwd_length))

    # Else generate a password with lowercase and uppercase letters, special
    # characters and numbers
    else:
        characters = lower_chars + upper_chars + special_chars + numbers
        password = ''.join(random.choice(characters) for _ in range(passwd_length))

    print("\nGenerated Password: ", password)

    save_password = input("\nWould you like to save the password? (Y/N) ")

    while True:
        if save_password.lower() != 'y' and save_password.lower() != 'n':
            save_password = input("Please choose 'Y' for yes or 'N' for no? (Y/N) ")
            continue
        elif save_password.lower() == 'y':
            save_password = True
            break
        else:
            save_password = False
            break

    if save_password:

        # Get Downloads folder
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

        # Append the file name to the Downloads path
        file_path = os.path.join(downloads_path, "password.txt")

        # Check if the file already exists
        if os.path.exists(file_path):
            # File already exists, prompt the user to confirm overwrite
            usr_input = input("The file already exists. Do you want to overwrite it? (yes/no): ").lower()
            if usr_input != 'yes':
                new_file_name = input("What would you like to name this file: ")
                # Append the file name to the Downloads path
                file_path = os.path.join(downloads_path, new_file_name)
                # Check if the file name includes .txt extension, if not, append it
                if not file_path.endswith('.txt'):
                    file_path += '.txt'

        # Write the password to the file
        with open(file_path, "w") as file:
            # Write the content of the text variable to the file
            file.write(password)

        # Display file path
        print("\033[31mPassword saved to:\033[0m", file_path)
        input("\n\033[32mPress Enter to continue...\033[0m")

    if not save_password:
        print("\n\033[33mThank you for using password generator!\033[0m")
        time.sleep(2.5)

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
input("\n\n\n\n\t\t\t            \U0001F44B Welcome to Radar! Press 'enter' to continue...")
clear_selected_line()

if operating_system == 'win32':
    os.system('cls')
if operating_system == 'linux' or operating_system == 'darwin':
    os.system('clear')

display_intro()

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

    print("\n\t[1] Weather\n")
    print(f"\t[2] News for {city_name}\n")
    print("\t[3] Search the News\n")
    print("\t[4] Time Zone\n")
    print("\t[5] Tax Rates\n")
    print("\t[6] Enter New Zip Code\n")
    print("\t[7] Generate Password\n")
    print("\t[8] Blackjack!\n")
    print("\t[9] FBI Top Secret Documents\n")
    print("\t[10] Exit\n")

    while True:

        user_choice = input(f"{yellow_color_profile}Pick an option: {reset_color_profile}")

        if user_choice.lower() == 'quit' or user_choice.lower() == 'exit':
            if operating_system == 'win32':
                os.system('cls')
            if operating_system == 'linux' or operating_system == 'darwin':
                os.system('clear')
            farewell()
        elif int(user_choice) < 1 or int(user_choice) > 10:
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

    if user_choice.lower() == 'quit' or user_choice.lower() == 'exit':
        if operating_system == 'win32':
            os.system('cls')
        if operating_system == 'linux' or operating_system == 'darwin':
            os.system('clear')

        farewell()

    elif user_choice == '1':
        if operating_system == 'win32':
            os.system('cls')
        if operating_system == 'linux' or operating_system == 'darwin':
            os.system('clear')

        display_weather_intro()
        get_weather(city_name)

    elif user_choice == '2':
        if operating_system == 'win32':
            os.system('cls')
        if operating_system == 'linux' or operating_system == 'darwin':
            os.system('clear')

        display_local_news_intro()
        get_local_news(city_name)

    elif user_choice == '3':
        if operating_system == 'win32':
            os.system('cls')
        if operating_system == 'linux' or operating_system == 'darwin':
            os.system('clear')

        display_news_intro()
        get_news()

    elif user_choice == '4':
        if operating_system == 'win32':
            os.system('cls')
        if operating_system == 'linux' or operating_system == 'darwin':
            os.system('clear')

        display_time_intro()
        get_time(city_name, latitude, longitude)

    elif user_choice == '5':
        if operating_system == 'win32':
            os.system('cls')
        if operating_system == 'linux' or operating_system == 'darwin':
            os.system('clear')

        display_tax_intro()
        get_tax_rates(latitude, longitude)

    elif user_choice == '6':
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

    elif user_choice == '7':
        if operating_system == 'win32':
            os.system('cls')
        if operating_system == 'linux' or operating_system == 'darwin':
            os.system('clear')

        display_password_intro()
        generate_password()

    elif user_choice == '8':
        if operating_system == 'win32':
            os.system('cls')
        if operating_system == 'linux' or operating_system == 'darwin':
            os.system('clear')
        play_blackjack()

    elif user_choice == '9':
        if operating_system == 'win32':
            os.system('cls')
        if operating_system == 'linux' or operating_system == 'darwin':
            os.system('clear')

        display_top_secret_intro()

        if operating_system == 'win32':
            # Get the default audio device
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

            # Control volume
            volume = cast(interface, POINTER(IAudioEndpointVolume))

            # Check if the volume is muted
            is_muted = volume.GetMute()

            # Unmute the audio if it's muted
            if is_muted:
                volume.SetMute(0, None)

            # Set volume to 30% of max volume
            volume.SetMasterVolumeLevelScalar(1.0, None)

        if operating_system == 'linux':
            # Unmute the volume
            subprocess.call(["amixer", "-D", "pulse", "sset", "Master", "unmute"])

            # Increase volume by 10%
            subprocess.call(["amixer", "-D", "pulse", "sset", "Master", "100%+"])

        if operating_system == 'darwin':
            # Unmute the volume
            subprocess.call(["osascript", "-e", "set volume without output muted"])

            # Increase volume by 10%
            subprocess.call(
                ["osascript", "-e", "set volume output volume (output volume of (get volume settings) + 100)"])

        print("\033[31mWHAT YOU ARE ABOUT TO SEE IS TOP SECRET....")
        time.sleep(3)
        print("DO NOT SHARE THIS WITH ANYONE....")
        time.sleep(3)
        input("BY HITTING ENTER, YOU CONSIDERED YOURSELF WARNED....")

        # URL of the "Never Gonna Give You Up" YouTube video
        video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

        # Open the default web browser and play the video
        webbrowser.open(video_url)

        time.sleep(5)

        print(f"""
⡀⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⣀⣀⠀⣀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⡀⠀⠀⠀
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣛⣿⣿⣷⣿⣿⣯⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣏⠉⣿⠉⢹⠟⢉⠉⢻⣿⠉⢻⠋⠙⡏⣿⠋⢻⡏⠉⣿⠉⣉⣻⠀
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⡀⠈⢀⣿⠀⢸⠀⠀⣿⠀⢸⠀⠰⣿⣿⠀⢸⠁⢀⡟⠀⢹⣿⠀
⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⡿⠿⠿⢿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠀⣼⣿⠀⢸⡀⠀⣏⠀⢸⠀⠀⣿⣿⡄⠘⠀⢸⡇⠀⢰⣾⠀
⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡿⠋⠀⠀⠀⠀⠀⠈⠉⠉⠁⠀⠀⠈⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣀⣿⣿⣆⡈⢁⣰⣿⣄⠘⢀⣼⣿⣿⣇⣀⣀⣼⣧⣀⣈⣹⡇
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⣿⣿⣿⣿⣿⣿⠟⠿⢿⣿⠿⠛⠛⠻⠿⠿⠻⠛⠉⠉⠉⠀
⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⣄⠀⠀⠀⠀⠀⠀⣴⠶⡶⠿⣿⣿⠿⠿⢿⡿⠿⠿⣿⠿⢿⡿⢿⡿⠀⠀⠀⠀⠀⠀⠀
⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣿⣿⠀⠀⢨⣭⣽⣿⡇⠀⢠⣾⣿⣿⣷⣆⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⣿⠀⢱⡆⠈⣿⠀⢴⣾⡇⠀⣶⣿⠀⠘⡇⠀⡇⠀⠀⠀⠀⠀⠀⠀
⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠉⠛⠀⠀⠀⠀⠉⠁⠀⠀⠘⡏⠉⠉⠛⠋⠀⣠⣼⣿⠀⠀⠀⠀⠀⠀⣿⠀⢨⡁⠺⣿⠀⣈⣹⡇⠀⣉⣿⠀⡀⠁⠀⡇⠀⠀⠀⠀⠀⠀⠀
⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⢹⡄⠀⠀⠀⠀⣿⣿⡿⠀⠀⠀⠀⠀⠀⣿⠀⠸⠇⠀⣿⠀⠹⢿⡇⠀⠿⢿⠀⢸⡀⠀⡇⠀⠀⠀⠀⠀⠀⠀
⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢷⣄⡀⠀⢠⡾⠋⠀⠛⢶⣶⣾⡇⠀⣠⠄ ⢰⣿⠟⠀⠀⠀⠀⠀⠀⠀⠻⢶⣶⡶⠚⠓⠶⠶⠾⠷⠶⠶⠾⠶⠾⠳⠾⠟⠀⠀⠀⠀⠀⠀⠀
⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣹⡷⣠⠏⠙⢷⣶⠲⠶⠶⣷⣶⡿⠋⢀ ⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣹⣧⡀⢀⠀⠀⣀⣀⣀⡀⢀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⣫⣽⠃⠀⠀⠀⠉⠉⠙⠛⠋⠀⠀⢀⣾⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠉⢉⡉⠻⡏⠉⣿⠟⢉⡉⠙⣿⠉⢹⡏⢉⡿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠛⠁⠀⣼⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡏⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠸⠇⣰⡇⠀⣿⠀⢸⣧⣀⣿⠀⠈⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⠏⠀⠀⠀⢸⣿⣿⡀⠀⠀⠰⣦⣄⡀⣀⣤⡾⣿⣿⣧⠀⠻⢦⣄⡀⠀⠀⠀⠀⠀⣿⠀⢸⠀⠈⡇⠀⣿⠀⢸⡟⠛⣿⠀⢠⠀⢹⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⠁⠀⠀⠀⠀⣾⣿⣿⣷⣄⡀⠀⠙⠿⣿⣏⣽⣿⣿⣿⣿⠄⢸⣧⠈⠙⠶⣤⣀⠀⠀⣿⣀⣸⣄⣠⣷⣀⣿⣦⣀⣁⣠⣿⣀⣸⣧⣀⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⠀⠀⠹⣆⠀⠀⠀⠉⠳⣦⡀⠉⠉⠙⠻⣿⠉⠁⠀⠉⠉⠀⠀⠈⠉⠀⠉⠹⠇⠀⠀⠀⠀⠀⠀
⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⢿⡆⠀⠀⠀⠀⠻⣿⠓⠒⠲⢦⣹⠷⠒⠲⣶⡖⠒⣶⣶⠒⢶⣾⠗⠒⠲⡶⠒⡖⠶⣄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⡞⣿⠀⠀⠀⠀⠀⢹⠀⢹⡀⢈⡏⠀⣿⠀⢸⡇⠀⣿⡟⠀⢸⣿⠀⢸⣶⡇⠀⢳⠀⢸
⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⢀⣰⠃⢹⡆⠀⠀⠀⠀⢸⠀⢠⠀⠛⡇⠀⣿⠀⢸⡇⠀⣿⡇⠀⢸⣿⠀⢠⣬⡇⠀⢸⠀⢸
⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠋⠉⠀⠺⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠶⠞⠋⠀⠀⠀⢿⠀⠀⠀⠀⣸⠀⢸⠀⢰⣧⠀⠛⠀⣸⡇⠀⠛⣧⠀⠘⢻⠀⠘⠛⡇⠀⠚⠀⢸
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠆⠀⠀⠀⠿⠓⠛⠓⠛⠉⠙⠒⠚⠉⠛⣛⡚⠛⠛⠛⠛⠛⠓⡚⠛⠛⠓⠛⠉
""")
        print("\033[36m\nDid you really think I would share those kind of documents? LOL")
        input("\033[32mPress Enter to continue...\033[0m")

    elif user_choice == '10':
        if operating_system == 'win32':
            os.system('cls')
        if operating_system == 'linux' or operating_system == 'darwin':
            os.system('clear')
        farewell()
