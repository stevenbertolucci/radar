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
import requests

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
    os.system('cls')
    exit(0)


def validate_input(usr_input):
    """
    Function validate_input that takes in user_input as a parameter
    and validates to see if User entered 'quit' or a legitimate zip code.
    """

    if usr_input.lower() == 'quit':
        os.system('cls')
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
                    if 'geometry' in result and 'location' in result['geometry']:
                        latitude = result['geometry']['location']['lat']
                        longitude = result['geometry']['location']['lng']

                    if city and latitude is not None and longitude is not None:
                        break

    # print(f"{city}")
    # print(f"{latitude}")
    # print(f"{longitude}")


def get_weather():
    """
    Function get_weather that requests weather info by calling
    WeatherAPI to retrieve weather information for that zip code.
    """

    print("\033[31mRetrieving Weather information. Please wait... \033[0m")
    time.sleep(0.5)
    api_key = 'dd86ae75f9b94cafb28195718241501'
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={user_input}&aqi=no'

    response = requests.get(url)

    if response.status_code == 200:
        clear_selected_line()
        data = response.json()
        print("\033[36mWeather:\033[0m", data)
    else:
        clear_selected_line()
        print("Error retrieving weather")

    input("\n\033[32mPress Enter to Continue...\033[0m")
    os.system('cls')


def get_local_news():
    """
    Function get_local_news sends a request to NewsAPI.org to
    retrieve local news of that zip code. NewsAPI uses keywords
    like city name, so this function retrieves city name from
    Google Geocoding API and then searches news for that city.
    """

    print("\033[31mRetrieving Local News. Please wait... \033[0m")
    time.sleep(0.5)
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=342d3256cc1c4b2cb71cfb4a00ba9a92"

    response = requests.get(url)

    if response.status_code == 200:
        clear_selected_line()
        data = response.json()
        print("\033[36mLocal News:\033[0m", data)
    else:
        print(f"Error: {response.status_code}")

    input("\n\033[32mPress Enter to continue...\033[0m")
    os.system('cls')


def get_time():
    """
    Function get_time retrieves the current time and time zone
    of the location that the user inputted. No API key was required,
    and it is free to use.
    """

    print("\033[31mRetrieving time information. Please wait... \033[0m")
    time.sleep(0.5)
    url = "https://timeapi.io/api/Time/current/zone"

    parameters = {
        "format": "json",
        "timeZone": "America/Los_Angeles"
    }

    response = requests.get(url, params=parameters)

    if response.status_code == 200:
        clear_selected_line()
        data = response.json()
        print("\033[36mTime Zone:\033[0m", data)
    else:
        print(f"Error: {response.status_code}")

    input("\n\033[32mPress Enter to continue...\033[0m")
    os.system('cls')


def get_tax_rates():
    print("\033[31mRetrieving tax rates. Please wait... \033[0m")
    time.sleep(0.5)
    url = "https://api.precisely.com/localtax/v1/taxrate/General/bylocation?latitude=32.7749487&longitude=-117.0146736"

    response = requests.get(url)

    if response.status_code == 200:
        clear_selected_line()
        data = response.json()
        print(data)

        # Access the "TotalTaxRate" from the "salesTax" object
        total_tax_rate = data.get("salesTax", {}).get("TotalTaxRate", None)

        if total_tax_rate is not None:
            print("\033[36mTotal Tax Rate:\033[0m", total_tax_rate)
        else:
            print("Total Tax Rate information not found.")
    else:
        print(f"Error: {response.status_code}")

    input("\n\033[32mPress Enter to continue...\033[0m")
    os.system('cls')

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
        os.system('cls')
        display_intro()
    print("\n\t1. Weather\n")
    print("\t2. Local News\n")
    print("\t3. Time Zone\n")
    print("\t4. Tax Rates\n")
    print("\t5. Enter New Zip Code\n")
    print("\t6. Generate Password\n")
    print("\t7. Exit\n")

    while True:

        user_choice = input(f"{yellow_color_profile}Pick an option: {reset_color_profile}")

        if user_choice == 'quit':
            os.system('cls')
            farewell()
        elif user_choice < '1' or user_choice > '7':
            clear_selected_line()
            print("\033[31mPlease pick a valid option.\033[0m")
            continue
        else:
            os.system('cls')
            display_intro()
            break

    if user_choice.lower() == 'quit':
        os.system('cls')
        farewell()

    elif user_choice == '1':
        get_weather()

    elif user_choice == '2':
        get_local_news()

    elif user_choice == '3':
        get_time()

    elif user_choice == '4':
        # get_tax_rates()
        input("Tax Rates Info Coming soon... Press Enter to continue")
        os.system('cls')

    elif user_choice == '5':
        os.system('cls')
        display_intro()
        while True:
            user_input = input("\033[33mEnter New Zip Code: \033[0m")
            result = validate_input(user_input)
            if not result:
                continue
            else:
                break

    elif user_choice == '6':
        input("Password Generator Coming soon... Press Enter to continue")
        os.system('cls')

    elif user_choice == '7':
        os.system('cls')
        farewell()
