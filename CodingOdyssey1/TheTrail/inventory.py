# inventory.py
# Inventory display logic for Oregon Trail game

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
