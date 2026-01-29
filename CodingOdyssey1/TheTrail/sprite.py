##this file contains the classes for the wagon and player. Sprite was just a random name I thought of.
##this defines the wagon class

class Wagon:
    def __init__(self):
        self.miles = 0
        self.health = 100
        self.capacity = 100
        self.food = 50
        self.parts = 0  
        self.ox = 1

    def drive(self, distance):
        self.miles += distance

    def lose_health(self, amount):
        self.health = max(0, self.health - amount)
        self.capacity = max(0, self.capacity - amount)

    def add_food(self, amount):
        self.food += amount

    def consume_food(self, amount):
        self.food = max(0, self.food - amount)

    def get_food(self):
        return self.food
    
##this defines the player class
class Player:
    def __init__(self):
        self.health = 100
        self.hunger = 0
        self.fatigue = 0
        self.money = 100  # Default starting money
        self.gun = False 
        self.ammo = 0
        self.bandages = 0
        

    def get_health(self):
        return self.health

    def lose_health(self, amount):
        self.health = max(0, self.health - amount)

    def increase_hunger(self, amount):
        self.hunger = min(100, self.hunger + amount)

    def decrease_hunger(self, amount):
        self.hunger = max(0, self.hunger - amount)

    def increase_fatigue(self, amount):
        self.fatigue = min(100, self.fatigue + amount)

    def decrease_fatigue(self, amount):
        self.fatigue = max(0, self.fatigue - amount)