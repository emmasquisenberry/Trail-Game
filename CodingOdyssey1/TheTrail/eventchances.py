import random
##imported random to help with random events
##this file contains all of the possible random events that can happen on the trail.

events = [
    {"name": "Wagon Breaks", "description": "Your wagon breaks down and you lose a day repairing it.", "wagon_damage": 1},
    {"name": "Dysentery", "description": "You catch dysentery and lose some health.", "health_loss": 20},
    {"name": "Snake Bite", "description": "A snake bites you. You lose some health.", "health_loss": 15},
    {"name": "River Crossing", "description": "You must cross a dangerous river.", "health_loss": 5, "food_loss": 10},
    {"name": "Food Spoilage", "description": "Some of your food spoils.", "food_loss": 25},
    {"name": "Bandit Attack", "description": "Bandits attack and steal some supplies.", "health_loss": 10, "food_loss": 20, "money_loss": 15}
]

def random_event(player=None, wagon=None, inventory=None):
    event = random.choice(events)
    print(f"Event: {event['name']}\nDescription: {event['description']}")
    if player and 'health_loss' in event:
        player.lose_health(event['health_loss'])
        print(f"You lost {event['health_loss']} health! Current health: {player.get_health()}")
    # Apply food loss
    if inventory and 'food_loss' in event:
        if hasattr(inventory, 'lose_food'):
            inventory.lose_food(event['food_loss'])
            print(f"You lost {event['food_loss']} food! Current food: {inventory.get_food()}")
        elif hasattr(player, 'lose_food'):
            player.lose_food(event['food_loss'])
            print(f"You lost {event['food_loss']} food! Current food: {player.get_food()}")
    # Apply money loss
    if player and 'money_loss' in event:
        if hasattr(player, 'lose_money'):
            player.lose_money(event['money_loss'])
            print(f"You lost ${event['money_loss']}! Current money: {player.get_money()}")
    # Apply wagon damage
    if wagon and 'wagon_damage' in event:
        if hasattr(wagon, 'damage'):
            wagon.damage(event['wagon_damage'])
            print(f"Your wagon took {event['wagon_damage']} damage!")

if __name__ == "__main__":
    try:
        from TheTrail.sprite import Player
        player = Player()
        random_event(player)
    except ImportError:
        print("Player class not found. Showing event only.")
        random_event()