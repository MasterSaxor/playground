import unittest
from activities import eat, nap, is_funny

class ActivitiesTests(unittest.TestCase):
    def test_eat(self):
        """eating with healthy should be vegetarian"""
        self.assertEqual(
            eat("brocolli", is_healthy=True),
            "I'm eating brocolli, because I'm a vegetarian"
        )

    def test_eat_unhealthy(self):
        """eating with unhealthy should be YOLO"""
        self.assertEqual(
            eat("fries", is_healthy=False),
            "I'm eating fries, because you only lived once"
        )

    def test_short_nap(self):
        """short naps with message of refresh"""
        self.assertEqual(
            nap(1),
            "I'm feeling refreshed"
        )

    def test_long_nap(self):
        """long naps withd discouraging message"""

        self.assertEqual(
            nap(3),
            "Uhg I overslept, I did'nt meant to sleep for 3 hours"
        )

    def test_is_funny(self):
        self.assertFalse(
            is_funny("me"), "Me is not funny"
        )
    
    def test_others_funny(self):
        self.assertTrue(
            is_funny("meo"), True
        )

        self.assertTrue(
            is_funny("calvin"), True
        )

        self.assertTrue(
            is_funny("harold"), True
        )


if __name__ == "__main__":
    unittest.main()