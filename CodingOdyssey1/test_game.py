import unittest
from TheTrail.sprite import Wagon, Player

class TestWagon(unittest.TestCase):
    def setUp(self):
        self.wagon = Wagon()

    def test_initial_state(self):
        self.assertEqual(self.wagon.miles, 0)
        self.assertEqual(self.wagon.health, 100)
        self.assertEqual(self.wagon.capacity, 100)
        self.assertEqual(self.wagon.food, 50)
        self.assertEqual(self.wagon.parts, 0)
        self.assertEqual(self.wagon.ox, 1)

    def test_drive(self):
        self.wagon.drive(20)
        self.assertEqual(self.wagon.miles, 20)

    def test_lose_health_and_capacity(self):
        self.wagon.lose_health(25)
        self.assertEqual(self.wagon.health, 75)
        self.assertEqual(self.wagon.capacity, 75)

    def test_add_and_consume_food(self):
        self.wagon.add_food(15)
        self.assertEqual(self.wagon.get_food(), 65)
        self.wagon.consume_food(10)
        self.assertEqual(self.wagon.get_food(), 55)

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player()

    def test_initial_state(self):
        self.assertEqual(self.player.get_health(), 100)
        self.assertEqual(self.player.hunger, 0)
        self.assertEqual(self.player.fatigue, 0)
        self.assertEqual(self.player.money, 100)
        self.assertFalse(self.player.gun)
        self.assertEqual(self.player.ammo, 0)
        self.assertEqual(self.player.bandages, 0)

    def test_lose_health(self):
        self.player.lose_health(45)
        self.assertEqual(self.player.get_health(), 55)

    def test_increase_and_decrease_hunger(self):
        self.player.increase_hunger(60)
        self.assertEqual(self.player.hunger, 60)
        self.player.decrease_hunger(25)
        self.assertEqual(self.player.hunger, 35)

    def test_increase_and_decrease_fatigue(self):
        self.player.increase_fatigue(80)
        self.assertEqual(self.player.fatigue, 80)
        self.player.decrease_fatigue(30)
        self.assertEqual(self.player.fatigue, 50)

if __name__ == '__main__':
    unittest.main()
