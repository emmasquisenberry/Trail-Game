import os
def display_inventory(player, wagon):
    print("\n--- Inventory ---")
    print(f"Money: ${player.money}")
    print(f"Food: {wagon.get_food()}")
    print(f"Wagon Parts: {wagon.parts}")
    print(f"Oxen: {wagon.ox}")
    print(f"Gun: {'Yes' if player.gun else 'No'}")
    print(f"Ammo: {player.ammo}")
    print(f"Bandages: {player.bandages}")
    print("-----------------")


from sprite import Wagon, Player
from eventchances import random_event
import time
import random


wagon = Wagon()
player = Player()

# Add new inventory attributes to player and wagon
player.money = 100  # Starting money
player.gun = False
player.ammo = 0
player.bandages = 0
wagon.ox = 1
wagon.parts = 0

##store interaction function
def store_interaction(player, wagon):
    print("\nYou have arrived at the General Store!, would you like to buy something?")
    print("1. Yes")
    print("2. No")
    choice = input("Choice: ").strip().lower()
    if choice not in ["1", "yes", "y"]:
        print("Leaving the store.")
        return
    store_items = [
        ("Food (per 10 units)", 5, "food"),
        ("Wagon Part", 20, "parts"),
        ("Ox", 40, "ox"),
        ("Gun", 50, "gun"),
        ("Ammo (per 10)", 10, "ammo"),
        ("Bandages", 8, "bandages")
    ]
    while True:
        print(f"\nYou have ${player.money} left.")
        print("What would you like to buy?")
        for idx, (name, price, _) in enumerate(store_items, 1):
            print(f"{idx}. {name} - ${price}")
        print(f"{len(store_items)+1}. Leave store")
        choice = input("Choose an item number: ")
        try:
            choice = int(choice)
        except ValueError:
            print("Invalid input.")
            continue
        if choice == len(store_items)+1:
            print("Leaving the store.")
            break
        if 1 <= choice <= len(store_items):
            name, price, key = store_items[choice-1]
            if player.money < price:
                print("Not enough money!")
                continue
            if key == "food":
                wagon.add_food(10)
            elif key == "parts":
                wagon.parts += 1
            elif key == "ox":
                wagon.ox += 1
            elif key == "gun":
                if player.gun:
                    print("You already have a gun.")
                    continue
                player.gun = True
            elif key == "ammo":
                player.ammo += 10
            elif key == "bandages":
                player.bandages += 1
            player.money -= price
            print(f"Purchased {name}!")
        else:
            print("Invalid choice.")
        if player.money <= 0:
            print("You have run out of money and cannot buy anything else.")
            break

print("Starting a new game...")
wagon = Wagon()
player = Player()


print("Please name your character:")
player.name = input("Name: ")
print(f"Welcome, {player.name}! Your journey begins now.")
print("You start with 50 food, 100 health, and a wagon capacity of 100.")

print("Please choose the pace you would like to take.")
print("1. Easy (1-2 miles per turn)")
print("2. Steady (3-5 miles per turn)")
print("3. Strenuous (4-6 miles per turn)")
print("4. Grueling (5-8 miles per turn)")
print("The faster you go, the more food you will consume and the more fatigue you will gain.")
while True:
    pace_choice = input("Please choose your pace (1, 2, 3, or 4): ")
    if pace_choice == "1":
        pace = (1, 2)
        break
    elif pace_choice == "2":
        pace = (3, 5)
        break
    elif pace_choice == "3":
        pace = (4, 6)
        break
    elif pace_choice == "4":
        pace = (5, 8)
        break
    else:
        print("Invalid choice, please try again.")

print("The more food you eat, the less hungry you will be and the less health you will lose.")
while True:
    print("Please choose your rations:")
    print("1. Filling (10 food per turn)")
    print("2. Meager (5 food per turn)")
    print("3. Bare Bones (2 food per turn)")
    rations_choice = input("Rations: ")
    if rations_choice == "1":
        rations = 10
        break
    elif rations_choice == "2":
        rations = 5
        break
    elif rations_choice == "3":
        rations = 2
        break
    else:
        print("Invalid choice, please try again.")
print(f"You have chosen {rations_choice} rations.")

print("Your journey begins now!")
store_mile_interval = 10
next_store_mile = store_mile_interval
while wagon.miles < 2000 and player.get_health() > 0:
    if wagon.miles >= next_store_mile:
        store_interaction(player, wagon)
        next_store_mile += store_mile_interval
    print("-------------------------------")
    print("Miles traveled:", wagon.miles)
    print("Health:", player.get_health())
    print("Food left:", wagon.get_food())
    print("Hunger level:", player.hunger)
    print("Fatigue level:", player.fatigue)
    print("-------------------------------")    
    for _ in range(8):
        print()
    print("---------------------------")
    print("New turn!")
    print("Please choose an option:")
    print("1. Continue on the trail")
    print("2. Change your pace.")
    print("3. Change your rations.")
    print("4. Rest for the day.")
    print("5. Check status.")
    print("6. Search for money on the trail")
    option = input("Option: ")

    if option == "1":  # Continue on the trail
        miles_driven = random.randint(pace[0], pace[1])
        wagon.drive(miles_driven)
        food_consumed = rations
        wagon.consume_food(food_consumed)
        # Hunger increases more with less rations
        if rations == 10:
            hunger_increase = 2
        elif rations == 5:
            hunger_increase = 7
        else:  # rations == 2
            hunger_increase = 12
        player.increase_hunger(hunger_increase)
        # Fatigue increases more with higher pace
        if pace == (1, 2):
            fatigue_increase = 5
        elif pace == (3, 5):
            fatigue_increase = 10
        elif pace == (4, 6):
            fatigue_increase = 15
        else:  # pace == (5, 8)
            fatigue_increase = 20
        player.increase_fatigue(fatigue_increase)
        if wagon.get_food() <= 0:
            player.lose_health(10)
            print("You have run out of food and are losing health!")
        if player.hunger >= 100:
            player.lose_health(20)
            print("You are starving and losing health!")
            player.hunger = 100
        if player.fatigue >= 100:
            player.lose_health(15)
            print("You are exhausted and losing health!")
            player.fatigue = 100
        if random.random() < 0.3:
            random_event(player)
    elif option == "2":  # Change pace
        while True:
            print("Choose your new pace:")
            print("1. Easy (1-2 miles per turn)")
            print("2. Steady (3-5 miles per turn)")
            print("3. Strenuous (4-6 miles per turn)")
            print("4. Grueling (5-8 miles per turn)")
            new_pace = input("New pace: ")
            if new_pace == "1":
                pace = (1, 2)
                break
            elif new_pace == "2":
                pace = (3, 5)
                break
            elif new_pace == "3":
                pace = (4, 6)
                break
            elif new_pace == "4":
                pace = (5, 8)
                break
            else:
                print("Invalid choice, please try again.")
    elif option == "3":  # Change rations
        while True:
            print("Choose your new rations:")
            print("1. Filling (10 food per turn)")
            print("2. Meager (5 food per turn)")
            print("3. Bare Bones (2 food per turn)")
            new_rations = input("New rations: ")
            if new_rations == "1":
                rations = 10
                break
            elif new_rations == "2":
                rations = 5
                break
            elif new_rations == "3":
                rations = 2
                break
            else:
                print("Invalid choice, please try again.")
    elif option == "4":  # Rest for the day
        player.fatigue = 0
        player.decrease_hunger(5)
        print("You rest for the day. Fatigue is fully restored and hunger decreases.")
    elif option == "5":  # Check status
        print(f"Status: Miles: {wagon.miles}, Health: {player.get_health()}, Food: {wagon.get_food()}, Hunger: {player.hunger}, Fatigue: {player.fatigue}, Money: ${player.money}")
    elif option == "6":  # Find money
        found = random.randint(5, 30)
        player.money += found
        print(f"You found ${found} on the trail!")
    else:
        print("Invalid option. Please choose again.")


if player.get_health() <= 0:
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print("---------------------------")
    print("You have died on the trail. Game over.")
    print("Total miles traveled:", wagon.miles)
    print("Thank you for playing!")