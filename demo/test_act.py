import unittest
from activities import eat, nap, is_funny

class Activity_Tests(unittest.TestCase):
    def test_eat_healthy(self):
        """Eating healthy with good message"""
        self.assertEqual(
            eat("broccoli", is_healthy=True),
            "I'm eating broccoli because my body requires it"
        )
        
    def test_eat_unhealthy(self):
        """Eating healthy with encouraging message"""
        self.assertEqual(
            eat("fries", is_healthy=False),
            "I'm eating fries because you only lived once"
        )

    def test_long_nap(self):
        """long naps should be discouraging"""
        self.assertEqual(
            nap(3), 
            "Oh no, I overslept, did'nt meant to sleept for 3 hours"
        )

    def test_short_nap(self):
        """short nap with refresh mesasge"""
        self.assertEqual(
            nap(1), 
            "Feels good, I'm feeling refreshed"
        )
        
    def test_is_funny_me(self):
        self.assertEqual(is_funny("Me"), False)

    def test_is_funny_others(self):
        self.assertTrue(is_funny("Calvin"), True)
        self.assertTrue(is_funny("Yno"), True)


if __name__ == "__main__":
    unittest.main()