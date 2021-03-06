import unittest
import game


class TestFunc(unittest.TestCase):
    def setUp(self):
        self._c1 = game.Character(health=10, armor=5)
        self._c2 = game.Character(health=50, armor=50)

        self._eventList = [
            {"character": self._c1, "type" : "damage", "size": 50},
            {"character": self._c2, "type" : "damage", "size": 50},
            {"character": self._c2, "type" : "heal", "size": 50}
        ]

    def test_should_handle_the_damage_event(self):
        game.handleEvents(self._eventList)
        self.assertFalse(self._c1.isAlive())
        self.assertTrue(self._c2.isAlive())

    def test_should_heal_a_character(self):
        game.handleHealthEvents(self._eventList)
        self.assertEqual(self._c2.getHealth(), 100)

unittest.main()
