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

# Define ANSI escape codes for colors
red_color_profile = "\033[31m"       # Red text
green_color_profile = "\033[32m"     # Green text
yellow_color_profile = "\033[33m"    # Yellow text
blue_color_profile = "\033[34m"      # Blue text
purple_color_profile = "\033[35m"    # Purple text
reset_color_profile = "\033[0m"      # Default CLI text color (gray)


def farewell():
    print(f"\n\t\t\t     \U0001F44B{yellow_color_profile} Thank you for using Radar! Bye! \U0001F44B "
          f"{reset_color_profile}\n\n")
    return


print(f"{green_color_profile}-----------------------------------------------------------------------------------------"
      f"---------------------")
radar_ascii = f"""{green_color_profile}
                                                         dddddddd
      RRRRRRRRRRRRRRRRR                                  d::::::d
      R::::::::::::::::R                                 d::::::d
      R::::::RRRRRR:::::R                                d::::::d
      RR:::::R     R:::::R                               d:::::d
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
print(f"\t\t\t{purple_color_profile}ASCII text was generated using a web-based generator: "
      f"\n\t\t{blue_color_profile}https://patorjk.com/software/taag/#p=display&h=2&v=3&f=Doh&t=Radar")
print(f"\t\t\t\t{purple_color_profile}Retrieved from: Patrick Gillespie")
print(f"\n\t\t\t\t{red_color_profile}Copyrighted by Steven Bertolucci\u00A9")
print(f"{green_color_profile}-----------------------------------------------------------------------------------------"
      f"---------------------{reset_color_profile}")

user_input = input(f"\n{yellow_color_profile}Enter a zip code: {reset_color_profile}")

if user_input.lower() == 'quit':
    farewell()
    exit(0)

while True:
    print("\n\t1. Weather\n")
    print("\t2. Local News\n")
    print("\t3. Time Zone\n")
    print("\t4. Tax Rates\n")
    print("\t5. Enter New Zip Code\n")
    print("\t6. Generate Password\n")
    print("\t7. Exit\n")

    user_choice = input(f"{yellow_color_profile}Pick an option: {reset_color_profile}")
    if user_choice.lower() == 'quit':
        farewell()
        break
    elif user_choice == '7':
        farewell()
        break
