import os
import sys
import time
import random

# Define ANSI escape codes for colors
red_color_profile = "\033[31m"       # Red text
green_color_profile = "\033[32m"     # Green text
yellow_color_profile = "\033[33m"    # Yellow text
blue_color_profile = "\033[34m"      # Blue text
purple_color_profile = "\033[35m"    # Purple text
reset_color_profile = "\033[0m"      # Default CLI text color (gray)

# Get operating system name
operating_system = sys.platform


def display_blackjack_intro():
    # Display intro banner and copyrighted statements
    print(
        f"{green_color_profile}------------------------------------------------------------------")
    blackjack_ascii = f"""{green_color_profile}

             _     _            _    _            _    _ 
            | |   | |          | |  (_)          | |  | |
            | |__ | | __ _  ___| | ___  __ _  ___| | _| |
            | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ / |
            | |_) | | (_| | (__|   <| | (_| | (__|   <|_|
            |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_(_)
                                   _/ |                  
                                  |__/                   

    {reset_color_profile}"""

    print(blackjack_ascii)

    print(
        f"{green_color_profile}------------------------------------------------------------------{reset_color_profile}")


def cards():

    if operating_system == 'win32':
        deck_of_cards = {
            f""" 
                --------
               |A       |
               |        |
               |   ♠️   |
               |        |
               |       A|
                -------- """: 1,
            f"""\033[31m 
                --------
               |A       |
               |        |
               |   ♥️   |
               |        |
               |       A|
                -------- \033[0m""": 1,
            f"""\033[31m 
                --------
               |A       |
               |        |
               |   ♦️   |
               |        |
               |       A|
                -------- \033[0m""": 1,
            f"""
                --------
               |A       |
               |        |
               |   ♣️   |
               |        |
               |       A|
                -------- """: 1,
            f"""
                --------
               |2       |
               |        |
               |   ♠️   |
               |        |
               |       2|
                -------- """: 2,
            f"""\033[31m
                --------
               |2       |
               |        |
               |   ♥️   |
               |        |
               |       2|
                -------- \033[0m""": 2,
            f"""\033[31m
                --------
               |2       |
               |        |
               |   ♦️   |
               |        |
               |       2|
                -------- \033[0m""": 2,
            f"""
                --------
               |2       |
               |        |
               |   ♣️   |
               |        |
               |       2|
                -------- """: 2,
            f"""
                --------
               |3       |
               |        |
               |   ♠️   |
               |        |
               |       3|
                -------- """: 3,
            f"""\033[31m
                --------
               |3       |
               |        |
               |   ♥️   |
               |        |
               |       3|
                -------- \033[0m""": 3,
            f"""\033[31m
                --------
               |3       |
               |        |
               |   ♦️   |
               |        |
               |       3|
                -------- \033[0m""": 3,
            f"""
                --------
               |3       |
               |        |
               |   ♣️   |
               |        |
               |       3|
                -------- """: 3,
            f"""
                --------
               |4       |
               |        |
               |   ♠️   |
               |        |
               |       4|
                -------- """: 4,
            f"""\033[31m
                --------
               |4       |
               |        |
               |   ♥️   |
               |        |
               |       4|
                -------- \033[0m""": 4,
            f"""\033[31m
                --------
               |4       |
               |        |
               |   ♦️   |
               |        |
               |       4|
                -------- \033[0m""": 4,
            f"""
                --------
               |4       |
               |        |
               |   ♣️   |
               |        |
               |       4|
                -------- """: 4,
            f"""
                --------
               |5       |
               |        |
               |   ♠️   |
               |        |
               |       5|
                -------- """: 5,
            f"""\033[31m
                --------
               |5       |
               |        |
               |   ♥️   |
               |        |
               |       5|
                -------- \033[0m""": 5,
            f"""\033[31m
                --------
               |5       |
               |        |
               |   ♦️   |
               |        |
               |       5|
                -------- \033[0m""": 5,
            f"""
                --------
               |5       |
               |        |
               |   ♣️   |
               |        |
               |       5|
                -------- """: 5,
            f"""
                --------
               |6       |
               |        |
               |   ♠️   |
               |        |
               |       6|
                -------- """: 6,
            f"""\033[31m
                --------
               |6       |
               |        |
               |   ♥️   |
               |        |
               |       6|
                -------- \033[0m""": 6,
            f"""\033[31m
                --------
               |6       |
               |        |
               |   ♦️   |
               |        |
               |       6|
                -------- \033[0m""": 6,
            f"""
                --------
               |6       |
               |        |
               |   ♣️   |
               |        |
               |       6|
                -------- """: 6,
            f"""
                --------
               |7       |
               |        |
               |   ♠️   |
               |        |
               |       7|
                -------- """: 7,
            f"""\033[31m
                --------
               |7       |
               |        |
               |   ♥️   |
               |        |
               |       7|
                -------- \033[0m""": 7,
            f"""\033[31m
                --------
               |7       |
               |        |
               |   ♦️   |
               |        |
               |       7|
                -------- \033[0m""": 7,
            f"""
                --------
               |7       |
               |        |
               |   ♣️   |
               |        |
               |       7|
                -------- """: 7,
            f"""
                --------
               |8       |
               |        |
               |   ♠️   |
               |        |
               |       8|
                -------- """: 8,
            f"""\033[31m
                --------
               |8       |
               |        |
               |   ♥️   |
               |        |
               |       8|
                -------- \033[0m""": 8,
            f"""\033[31m
                --------
               |8       |
               |        |
               |   ♦️   |
               |        |
               |       8|
                -------- \033[0m""": 8,
            f"""
                --------
               |8       |
               |        |
               |   ♣️   |
               |        |
               |       8|
                -------- """: 8,
            f"""
                --------
               |9       |
               |        |
               |   ♠️   |
               |        |
               |       9|
                -------- """: 9,
            f"""\033[31m
                --------
               |9       |
               |        |
               |   ♥️   |
               |        |
               |       9|
                -------- \033[0m""": 9,
            f"""\033[31m
                --------
               |9       |
               |        |
               |   ♦️   |
               |        |
               |       9|
                -------- \033[0m""": 9,
            f"""
                --------
               |9       |
               |        |
               |   ♣️   |
               |        |
               |       9|
                -------- """: 9,
            f"""
                --------
               |10      |
               |        |
               |   ♠️   |
               |        |
               |      10|
                -------- """: 10,
            f"""\033[31m
                --------
               |10      |
               |        |
               |   ♥️   |
               |        |
               |      10|
                -------- \033[0m""": 10,
            f"""\033[31m
                --------
               |10      |
               |        |
               |   ♦️   |
               |        |
               |      10|
                -------- \033[0m""": 10,
            f"""
                --------
               |10      |
               |        |
               |   ♣️   |
               |        |
               |      10|
                -------- """: 10,
            f"""
                --------
               |J       |
               |        |
               |   ♠️   |
               |        |
               |       J|
                -------- """: 10,
            f"""\033[31m
                --------
               |J       |
               |        |
               |   ♥️   |
               |        |
               |       J|
                -------- \033[0m""": 10,
            f"""\033[31m
                --------
               |J       |
               |        |
               |   ♦️   |
               |        |
               |       J|
                -------- \033[0m""": 10,
            f"""
                --------
               |J       |
               |        |
               |   ♣️   |
               |        |
               |       J|
                -------- """: 10,
            f"""
                --------
               |Q       |
               |        |
               |   ♠️   |
               |        |
               |       Q|
                -------- """: 10,
            f"""\033[31m
                --------
               |Q       |
               |        |
               |   ♥️   |
               |        |
               |       Q|
                -------- \033[0m""": 10,
            f"""\033[31m
                --------
               |Q       |
               |        |
               |   ♦️   |
               |        |
               |       Q|
                -------- \033[0m""": 10,
            f"""
                --------
               |Q       |
               |        |
               |   ♣️   |
               |        |
               |       Q|
                -------- """: 10,
            f"""
                --------
               |K       |
               |        |
               |   ♠️   |
               |        |
               |       K|
                -------- """: 10,
            f"""\033[31m
                --------
               |K       |
               |        |
               |   ♥️   |
               |        |
               |       K|
                -------- \033[0m""": 10,
            f"""\033[31m
                --------
               |K       |
               |        |
               |   ♦️   |
               |        |
               |       K|
                -------- \033[0m""": 10,
            f"""
                --------
               |K       |
               |        |
               |   ♣️   |
               |        |
               |       K|
                -------- """: 10
        }

        return deck_of_cards

    if operating_system == 'linux' or operating_system == 'darwin':
        deck_of_cards = {
            f""" 
                --------
               |A       |
               |        |
               |   ♠️    |
               |        |
               |       A|
                -------- """: 1,
            f"""\033[31m 
                --------
               |A       |
               |        |
               |   ♥️    |
               |        |
               |       A|
                -------- \033[0m""": 1,
            f"""\033[31m 
                --------
               |A       |
               |        |
               |   ♦️    |
               |        |
               |       A|
                -------- \033[0m""": 1,
            f"""
                --------
               |A       |
               |        |
               |   ♣️    |
               |        |
               |       A|
                -------- """: 1,
            f"""
                --------
               |2       |
               |        |
               |   ♠️    |
               |        |
               |       2|
                -------- """: 2,
            f"""\033[31m
                --------
               |2       |
               |        |
               |   ♥️    |
               |        |
               |       2|
                -------- \033[0m""": 2,
            f"""\033[31m
                --------
               |2       |
               |        |
               |   ♦️    |
               |        |
               |       2|
                -------- \033[0m""": 2,
            f"""
                --------
               |2       |
               |        |
               |   ♣️    |
               |        |
               |       2|
                -------- """: 2,
            f"""
                --------
               |3       |
               |        |
               |   ♠️    |
               |        |
               |       3|
                -------- """: 3,
            f"""\033[31m
                --------
               |3       |
               |        |
               |   ♥️    |
               |        |
               |       3|
                -------- \033[0m""": 3,
            f"""\033[31m
                --------
               |3       |
               |        |
               |   ♦️    |
               |        |
               |       3|
                -------- \033[0m""": 3,
            f"""
                --------
               |3       |
               |        |
               |   ♣️    |
               |        |
               |       3|
                -------- """: 3,
            f"""
                --------
               |4       |
               |        |
               |   ♠️    |
               |        |
               |       4|
                -------- """: 4,
            f"""\033[31m
                --------
               |4       |
               |        |
               |   ♥️    |
               |        |
               |       4|
                -------- \033[0m""": 4,
            f"""\033[31m
                --------
               |4       |
               |        |
               |   ♦️    |
               |        |
               |       4|
                -------- \033[0m""": 4,
            f"""
                --------
               |4       |
               |        |
               |   ♣️    |
               |        |
               |       4|
                -------- """: 4,
            f"""
                --------
               |5       |
               |        |
               |   ♠️    |
               |        |
               |       5|
                -------- """: 5,
            f"""\033[31m
                --------
               |5       |
               |        |
               |   ♥️    |
               |        |
               |       5|
                -------- \033[0m""": 5,
            f"""\033[31m
                --------
               |5       |
               |        |
               |   ♦️    |
               |        |
               |       5|
                -------- \033[0m""": 5,
            f"""
                --------
               |5       |
               |        |
               |   ♣️    |
               |        |
               |       5|
                -------- """: 5,
            f"""
                --------
               |6       |
               |        |
               |   ♠️    |
               |        |
               |       6|
                -------- """: 6,
            f"""\033[31m
                --------
               |6       |
               |        |
               |   ♥️    |
               |        |
               |       6|
                -------- \033[0m""": 6,
            f"""\033[31m
                --------
               |6       |
               |        |
               |   ♦️    |
               |        |
               |       6|
                -------- \033[0m""": 6,
            f"""
                --------
               |6       |
               |        |
               |   ♣️    |
               |        |
               |       6|
                -------- """: 6,
            f"""
                --------
               |7       |
               |        |
               |   ♠️    |
               |        |
               |       7|
                -------- """: 7,
            f"""\033[31m
                --------
               |7       |
               |        |
               |   ♥️    |
               |        |
               |       7|
                -------- \033[0m""": 7,
            f"""\033[31m
                --------
               |7       |
               |        |
               |   ♦️    |
               |        |
               |       7|
                -------- \033[0m""": 7,
            f"""
                --------
               |7       |
               |        |
               |   ♣️    |
               |        |
               |       7|
                -------- """: 7,
            f"""
                --------
               |8       |
               |        |
               |   ♠️    |
               |        |
               |       8|
                -------- """: 8,
            f"""\033[31m
                --------
               |8       |
               |        |
               |   ♥️    |
               |        |
               |       8|
                -------- \033[0m""": 8,
            f"""\033[31m
                --------
               |8       |
               |        |
               |   ♦️    |
               |        |
               |       8|
                -------- \033[0m""": 8,
            f"""
                --------
               |8       |
               |        |
               |   ♣️    |
               |        |
               |       8|
                -------- """: 8,
            f"""
                --------
               |9       |
               |        |
               |   ♠️    |
               |        |
               |       9|
                -------- """: 9,
            f"""\033[31m
                --------
               |9       |
               |        |
               |   ♥️    |
               |        |
               |       9|
                -------- \033[0m""": 9,
            f"""\033[31m
                --------
               |9       |
               |        |
               |   ♦️    |
               |        |
               |       9|
                -------- \033[0m""": 9,
            f"""
                --------
               |9       |
               |        |
               |   ♣️    |
               |        |
               |       9|
                -------- """: 9,
            f"""
                --------
               |10      |
               |        |
               |   ♠️    |
               |        |
               |      10|
                -------- """: 10,
            f"""\033[31m
                --------
               |10      |
               |        |
               |   ♥️    |
               |        |
               |      10|
                -------- \033[0m""": 10,
            f"""\033[31m
                --------
               |10      |
               |        |
               |   ♦️    |
               |        |
               |      10|
                -------- \033[0m""": 10,
            f"""
                --------
               |10      |
               |        |
               |   ♣️    |
               |        |
               |      10|
                -------- """: 10,
            f"""
                --------
               |J       |
               |        |
               |   ♠️    |
               |        |
               |       J|
                -------- """: 10,
            f"""\033[31m
                --------
               |J       |
               |        |
               |   ♥️    |
               |        |
               |       J|
                -------- \033[0m""": 10,
            f"""\033[31m
                --------
               |J       |
               |        |
               |   ♦️    |
               |        |
               |       J|
                -------- \033[0m""": 10,
            f"""
                --------
               |J       |
               |        |
               |   ♣️    |
               |        |
               |       J|
                -------- """: 10,
            f"""
                --------
               |Q       |
               |        |
               |   ♠️    |
               |        |
               |       Q|
                -------- """: 10,
            f"""\033[31m
                --------
               |Q       |
               |        |
               |   ♥️    |
               |        |
               |       Q|
                -------- \033[0m""": 10,
            f"""\033[31m
                --------
               |Q       |
               |        |
               |   ♦️    |
               |        |
               |       Q|
                -------- \033[0m""": 10,
            f"""
                --------
               |Q       |
               |        |
               |   ♣️    |
               |        |
               |       Q|
                -------- """: 10,
            f"""
                --------
               |K       |
               |        |
               |   ♠️    |
               |        |
               |       K|
                -------- """: 10,
            f"""\033[31m
                --------
               |K       |
               |        |
               |   ♥️    |
               |        |
               |       K|
                -------- \033[0m""": 10,
            f"""\033[31m
                --------
               |K       |
               |        |
               |   ♦️    |
               |        |
               |       K|
                -------- \033[0m""": 10,
            f"""
                --------
               |K       |
               |        |
               |   ♣️    |
               |        |
               |       K|
                -------- """: 10
        }

        return deck_of_cards


def draw_card(deck):
    card = random.choice(list(deck.keys()))
    return card, deck[card]


def play_blackjack():
    counter = 0

    while True:

        if counter > 0:
            # Refresh screen
            if operating_system == 'win32':
                os.system('cls')
            if operating_system == 'linux' or operating_system == 'darwin':
                os.system('clear')

        # Display intro banner
        display_blackjack_intro()

        # Initialize arrays
        dealer_cards = []
        dealer_values = []
        player_cards = []
        player_values = []

        # Get cards
        deck_of_cards = cards()

        # Dealer Cards
        i = 0               # Dealer Card #1
        dealer_total = 0
        card, values = draw_card(deck_of_cards)
        dealer_cards.append(card)
        dealer_values.append(values)

        i += 1              # Dealer Card #2
        card, values = draw_card(deck_of_cards)
        dealer_cards.append(card)
        dealer_values.append(values)
        dealer_total += sum(dealer_values)

        dealer_hand = dealer_cards[0] + " " + dealer_cards[1]

        # Player Cards
        j = 0               # Player Card #1
        player_total = 0
        card, values = draw_card(deck_of_cards)
        player_cards.append(card)
        player_values.append(values)

        j += 1              # Player Card #2
        card, values = draw_card(deck_of_cards)
        player_cards.append(card)
        player_values.append(values)
        player_total += sum(player_values)

        # Add the cards to the player's hand
        player_hand = player_cards[0] + " " + player_cards[1]

        # Display the cards from both players
        print("Dealer's hand: \n", dealer_hand)
        print("Dealer's Total: ", dealer_total)
        print("\nYour hand: \n", player_hand)
        print("Player's Total: ", player_total)


        # Check to see if either hand got a blackjack. If so, display message
        # and exit
        if dealer_total == 21 and player_total == 21:
            print("\033[36mBOTH OF YOU GOT A BLACKJACK! GAME'S TIED!\033[0m")
            choice = input("\nNew game? (Y/N) ")
            if choice.lower() == 'y':
                counter += 1
                continue
            else:
                break
        elif dealer_total == 21:
            print("\033[31mDealer got a BLACKJACK!\033[0m")
            choice = input("\nNew game? (Y/N) ")
            if choice.lower() == 'y':
                counter += 1
                continue
            else:
                break
        elif player_total == 21:
            print("\033[32mYou got a BLACKJACK!\033[0m")
            choice = input("\nNew game? (Y/N) ")
            if choice.lower() == 'y':
                counter += 1
                continue
            else:
                break

        # Ask user (YOU) if they want to hit or stay
        usr_input = input("Hit (1) or Stay (2)? ")

        # Players Turn
        if usr_input == '1':

            # Refresh screen
            if operating_system == 'win32':
                os.system('cls')
            if operating_system == 'linux' or operating_system == 'darwin':
                os.system('clear')

            display_blackjack_intro()
            j += 1
            player_total2 = 0
            card, values = draw_card(deck_of_cards)
            player_cards.append(card)
            player_values.append(values)

            # Player now has 3 cards
            player_hand = player_cards[0] + " " + player_cards[1] + " " + player_cards[2]

            # Count the cards
            player_total2 += sum(player_values)

            # Display the cards from both players
            print("Dealer's hand: \n", dealer_hand)
            print("Dealer's Total: ", dealer_total)

            print("\nYour hand: \n", player_hand)
            print("Player's Total: ", player_total2)

            # Determine whether the player has a blackjack or over the limit
            if player_total2 == 21:
                print("\033[32mBLACKJACK! YOU WIN!\033[0m")
                choice = input("\nNew game? (Y/N) ")
                if choice.lower() == 'y':
                    counter += 1
                    continue
                else:
                    break
            elif player_total2 > 21:
                print("\033[31mBUSTED! YOU LOSE!\033[0m")
                choice = input("\nNew game? (Y/N) ")
                if choice.lower() == 'y':
                    counter += 1
                    continue
                else:
                    break
            elif player_total2 < 21:
                # Ask user if they want to hit or stay
                usr_input = input("Hit (1) or Stay (2)? ")
                if usr_input == '1':

                    # Refresh screen
                    if operating_system == 'win32':
                        os.system('cls')
                    if operating_system == 'linux' or operating_system == 'darwin':
                        os.system('clear')

                    display_blackjack_intro()
                    j += 1
                    player_total3 = 0
                    card, values = draw_card(deck_of_cards)
                    player_cards.append(card)
                    player_values.append(values)

                    # Player has 4 cards
                    player_hand = player_cards[0] + " " + player_cards[1] + " " + player_cards[2] + " " + player_cards[3]

                    # Count the cards
                    player_total3 += sum(player_values)

                    # Display the cards from both players
                    print("Dealer's hand: \n", dealer_hand)
                    print("Dealer's Total: ", dealer_total)

                    print("\nYour hand: \n", player_hand)
                    print("Player's Total: ", player_total3)

                    # Determine whether the player has a blackjack or over the limit
                    if player_total3 == 21:
                        print("\033[32mBLACKJACK! YOU WIN!\033[0m")
                        choice = input("\nNew game? (Y/N) ")
                        if choice.lower() == 'y':
                            counter += 1
                            continue
                        else:
                            break
                    elif player_total3 > 21:
                        print("\033[31mBUSTED! YOU LOSE!\033[0m")
                        choice = input("\nNew game? (Y/N) ")
                        if choice.lower() == 'y':
                            counter += 1
                            continue
                        else:
                            break
                    elif player_total3 == dealer_total:
                        print("\033[36mDRAW!\033[0m")
                        choice = input("\nNew game? (Y/N) ")
                        if choice.lower() == 'y':
                            counter += 1
                            continue
                        else:
                            break

                    elif player_total3 < dealer_total:
                        print("\033[31mYOU LOSE!\033[0m")
                        choice = input("\nNew game? (Y/N) ")
                        if choice.lower() == 'y':
                            counter += 1
                            continue
                        else:
                            break

                    elif player_total3 > dealer_total:
                        time.sleep(2)
                        # Refresh screen
                        if operating_system == 'win32':
                            os.system('cls')
                        if operating_system == 'linux' or operating_system == 'darwin':
                            os.system('clear')

                        display_blackjack_intro()
                        i += 1
                        dealer_total2 = 0
                        card, values = draw_card(deck_of_cards)
                        dealer_cards.append(card)
                        dealer_values.append(values)

                        # Dealer has 3 cards
                        dealer_hand = dealer_cards[0] + " " + dealer_cards[1] + " " + dealer_cards[2]

                        # Count the cards
                        dealer_total2 += sum(dealer_values)

                        # Display the cards from both players
                        print("Dealer's hand: \n", dealer_hand)
                        print("Dealer's Total: ", dealer_total2)

                        print("\nYour hand: \n", player_hand)
                        print("Player's Total: ", player_total3)

                        time.sleep(2.0)
                        if dealer_total2 == 21:
                            print("\033[31mDEALER BLACKJACK! YOU LOSE!\033[0m")
                            choice = input("\nNew game? (Y/N) ")
                            if choice.lower() == 'y':
                                counter += 1
                                continue
                            else:
                                break
                        elif dealer_total2 > 21:
                            print("\033[32mDEALER BUSTED! YOU WIN!\033[0m")
                            choice = input("\nNew game? (Y/N) ")
                            if choice.lower() == 'y':
                                counter += 1
                                continue
                            else:
                                break
                        elif player_total3 == dealer_total2:
                            print("\033[36mDRAW!\033[0m")
                            choice = input("\nNew game? (Y/N) ")
                            if choice.lower() == 'y':
                                counter += 1
                                continue
                            else:
                                break
                        elif player_total3 < dealer_total2:
                            print("\033[31mYOU LOSE!\033[0m")
                            choice = input("\nNew game? (Y/N) ")
                            if choice.lower() == 'y':
                                counter += 1
                                continue
                            else:
                                break

                        if player_total3 > dealer_total2:

                            # Refresh screen
                            if operating_system == 'win32':
                                os.system('cls')
                            if operating_system == 'linux' or operating_system == 'darwin':
                                os.system('clear')

                            display_blackjack_intro()
                            i += 1
                            dealer_total3 = 0
                            card, values = draw_card(deck_of_cards)
                            dealer_cards.append(card)
                            dealer_values.append(values)

                            # Dealer has 4 cards
                            dealer_hand = dealer_cards[0] + " " + dealer_cards[1] + " " + dealer_cards[2] + " " + \
                                          dealer_cards[3]

                            # Count the cards
                            dealer_total3 += sum(dealer_values)

                            # Display the cards from both players
                            print("Dealer's hand: \n", dealer_hand)
                            print("Dealer's Total: ", dealer_total3)

                            print("\nYour hand: \n", player_hand)
                            print("Player's Total: ", player_total3)

                            if dealer_total3 > 21:
                                print("\033[32mDEALER BUSTED! YOU WIN!\033[0m")
                                choice = input("\nNew game? (Y/N) ")
                                if choice.lower() == 'y':
                                    counter += 1
                                    continue
                                else:
                                    break
                            elif player_total3 > dealer_total3:
                                print("\033[32mYOU WIN!\033[0m")
                                choice = input("\nNew game? (Y/N) ")
                                if choice.lower() == 'y':
                                    counter += 1
                                    continue
                                else:
                                    break
                            elif player_total3 == dealer_total3:
                                print("\033[36mDRAW!\033[0m")
                                choice = input("\nNew game? (Y/N) ")
                                if choice.lower() == 'y':
                                    counter += 1
                                    continue
                                else:
                                    break
                            elif player_total3 < dealer_total3 <= 21:
                                print("\033[31mYOU LOST!\033[0m")
                                choice = input("\nNew game? (Y/N) ")
                                if choice.lower() == 'y':
                                    counter += 1
                                    continue
                                else:
                                    break

                else:
                    if player_total2 > dealer_total:
                        time.sleep(1)
                        # Refresh screen
                        if operating_system == 'win32':
                            os.system('cls')
                        if operating_system == 'linux' or operating_system == 'darwin':
                            os.system('clear')

                        display_blackjack_intro()
                        i += 1
                        dealer_total2 = 0
                        card, values = draw_card(deck_of_cards)
                        dealer_cards.append(card)
                        dealer_values.append(values)

                        # Dealer has 3 cards
                        dealer_hand = dealer_cards[0] + " " + dealer_cards[1] + " " + dealer_cards[2]

                        # Count the cards
                        dealer_total2 += sum(dealer_values)

                        # Display the cards from both players
                        print("Dealer's hand: \n", dealer_hand)
                        print("Dealer's Total: ", dealer_total2)

                        print("\nYour hand: \n", player_hand)
                        print("Player's Total: ", player_total2)

                        time.sleep(2.0)

                        if dealer_total2 == 21:
                            print("\033[31mDEALER BLACKJACK! YOU LOST!\033[0m")
                            choice = input("\nNew game? (Y/N) ")
                            if choice.lower() == 'y':
                                counter += 1
                                continue
                            else:
                                break
                        if dealer_total2 > 21:
                            print("\033[32mDEALER BUSTED! YOU WIN!\033[0m")
                            choice = input("\nNew game? (Y/N) ")
                            if choice.lower() == 'y':
                                counter += 1
                                continue
                            else:
                                break
                        elif player_total2 == dealer_total2:
                            print("\033[36mDRAW!\033[0m")
                            choice = input("\nNew game? (Y/N) ")
                            if choice.lower() == 'y':
                                counter += 1
                                continue
                            else:
                                break

                        if player_total2 > dealer_total2:

                            # Refresh screen
                            if operating_system == 'win32':
                                os.system('cls')
                            if operating_system == 'linux' or operating_system == 'darwin':
                                os.system('clear')

                            display_blackjack_intro()
                            i += 1
                            dealer_total3 = 0
                            card, values = draw_card(deck_of_cards)
                            dealer_cards.append(card)
                            dealer_values.append(values)

                            # Dealer has 4 cards
                            dealer_hand = dealer_cards[0] + " " + dealer_cards[1] + " " + dealer_cards[2] + " " + \
                                          dealer_cards[3]

                            # Count the cards
                            dealer_total3 += sum(dealer_values)

                            # Display the cards from both players
                            print("Dealer's hand: \n", dealer_hand)
                            print("Dealer's Total: ", dealer_total3)

                            print("\nYour hand: \n", player_hand)
                            print("Player's Total: ", player_total2)

                            if dealer_total3 > 21:
                                print("\033[32mDEALER BUSTED! YOU WIN!\033[0m")
                                choice = input("\nNew game? (Y/N) ")
                                if choice.lower() == 'y':
                                    counter += 1
                                    continue
                                else:
                                    break
                            elif player_total2 > dealer_total3:
                                print("\033[32mYOU WIN!\033[0m")
                                choice = input("\nNew game? (Y/N) ")
                                if choice.lower() == 'y':
                                    counter += 1
                                    continue
                                else:
                                    break
                            elif player_total2 == dealer_total3:
                                print("\033[36mDRAW!\033[0m")
                                choice = input("\nNew game? (Y/N) ")
                                if choice.lower() == 'y':
                                    counter += 1
                                    continue
                                else:
                                    break
                            elif player_total2 < dealer_total3 <= 21:
                                print("\033[31mYOU LOST!\033[0m")
                                choice = input("\nNew game? (Y/N) ")
                                if choice.lower() == 'y':
                                    counter += 1
                                    continue
                                else:
                                    break
                    elif player_total2 == dealer_total:
                        print("\033[36mDRAW!\033[0m")
                        choice = input("\nNew game? (Y/N) ")
                        if choice.lower() == 'y':
                            counter += 1
                            continue
                        else:
                            break

                    else:
                        print("\033[31mYOU LOSE!\033[0m")
                        choice = input("\nNew game? (Y/N) ")
                        if choice.lower() == 'y':
                            counter += 1
                            continue
                        else:
                            break

        # Dealers Turn
        else:
            if player_total > dealer_total:

                # Refresh screen
                if operating_system == 'win32':
                    os.system('cls')
                if operating_system == 'linux' or operating_system == 'darwin':
                    os.system('clear')

                display_blackjack_intro()
                i += 1
                dealer_total2 = 0
                card, values = draw_card(deck_of_cards)
                dealer_cards.append(card)
                dealer_values.append(values)

                # Dealer has 3 cards
                dealer_hand = dealer_cards[0] + " " + dealer_cards[1] + " " + dealer_cards[2]

                # Count the cards
                dealer_total2 += sum(dealer_values)

                # Display the cards from both players
                print("Dealer's hand: \n", dealer_hand)
                print("Dealer's Total: ", dealer_total2)

                print("\nYour hand: \n", player_hand)
                print("Player's Total: ", player_total)

                time.sleep(2.0)
                if dealer_total2 == 21:
                    print("\033[31mDEALER BLACKJACK! YOU LOST!\033[0m")
                    choice = input("\nNew game? (Y/N) ")
                    if choice.lower() == 'y':
                        counter += 1
                        continue
                    else:
                        break
                if dealer_total2 > 21:
                    print("\033[32mDEALER BUSTED! YOU WIN!\033[0m")
                    choice = input("\nNew game? (Y/N) ")
                    if choice.lower() == 'y':
                        counter += 1
                        continue
                    else:
                        break
                elif player_total == dealer_total2:
                    print("\033[36mDRAW!\033[0m")
                    choice = input("\nNew game? (Y/N) ")
                    if choice.lower() == 'y':
                        counter += 1
                        continue
                    else:
                        break
                elif player_total < dealer_total2 <= 21:
                    print("\033[31mYOU LOST!\033[0m")
                    choice = input("\nNew game? (Y/N) ")
                    if choice.lower() == 'y':
                        counter += 1
                        continue
                    else:
                        break

                if player_total > dealer_total2:

                    # Refresh screen
                    if operating_system == 'win32':
                        os.system('cls')
                    if operating_system == 'linux' or operating_system == 'darwin':
                        os.system('clear')

                    display_blackjack_intro()
                    i += 1
                    dealer_total3 = 0
                    card, values = draw_card(deck_of_cards)
                    dealer_cards.append(card)
                    dealer_values.append(values)

                    # Dealer has 4 cards
                    dealer_hand = dealer_cards[0] + " " + dealer_cards[1] + " " + dealer_cards[2] + " " + dealer_cards[3]

                    # Count the cards
                    dealer_total3 += sum(dealer_values)

                    # Display the cards from both players
                    print("Dealer's hand: \n", dealer_hand)
                    print("Dealer's Total: ", dealer_total3)

                    print("\nYour hand: \n", player_hand)
                    print("Player's Total: ", player_total)

                    if dealer_total3 == 21:
                        print("\033[31mDEALER BLACKJACK! YOU LOSE!\033[0m")
                        choice = input("\nNew game? (Y/N) ")
                        if choice.lower() == 'y':
                            counter += 1
                            continue
                        else:
                            break
                    elif dealer_total3 > 21:
                        print("\033[32mDEALER BUSTED! YOU WIN!\033[0m")
                        choice = input("\nNew game? (Y/N) ")
                        if choice.lower() == 'y':
                            counter += 1
                            continue
                        else:
                            break
                    elif player_total > dealer_total3:
                        print("\033[32mYOU WIN!\033[0m")
                        choice = input("\nNew game? (Y/N) ")
                        if choice.lower() == 'y':
                            counter += 1
                            continue
                        else:
                            break
                    elif player_total == dealer_total3:
                        print("\033[36mDRAW!\033[0m")
                        choice = input("\nNew game? (Y/N) ")
                        if choice.lower() == 'y':
                            counter += 1
                            continue
                        else:
                            break
                    elif player_total < dealer_total3 <= 21:
                        print("\033[31mYOU LOST!\033[0m")
                        choice = input("\nNew game? (Y/N) ")
                        if choice.lower() == 'y':
                            counter += 1
                            continue
                        else:
                            break

                elif player_total == dealer_total:
                    print("\033[36mDRAW!\033[0m")
                    choice = input("\nNew game? (Y/N) ")
                    if choice.lower() == 'y':
                        counter += 1
                        continue
                    else:
                        break
                else:
                    print("\033[31mYOU LOSE!\033[0m")
                    choice = input("\nNew game? (Y/N) ")
                    if choice.lower() == 'y':
                        counter += 1
                        continue
                    else:
                        break

            elif player_total == dealer_total:
                print("\033[36mDRAW!\033[0m")
                choice = input("\nNew game? (Y/N) ")
                if choice.lower() == 'y':
                    counter += 1
                    continue
                else:
                    break
            else:
                print("\033[31mYOU LOSE!\033[0m")
                choice = input("\nNew game? (Y/N) ")
                if choice.lower() == 'y':
                    counter += 1
                    continue
                else:
                    break
