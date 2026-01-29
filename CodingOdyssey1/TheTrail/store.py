# store.py
# Store logic for Oregon Trail game

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
