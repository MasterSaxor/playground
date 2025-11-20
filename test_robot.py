
import unittest
from robot import Robot

class RobotTests(unittest.TestCase):
    def test_charge(self):
        mega_man = Robot("Mega Man", battery=50)
        mega_man.charge()
        self.assertEqual(mega_man.battery, 100)

    def test_say_name(self):
        mega_man = Robot("Mega Man", battery=50)
        self.assertEqual(
            mega_man.say_name(), "BEEP BOOP BEEP BOOP.  I AM MEGA MAN")
        self.assertEqual(mega_man.battery, 49)

    
if __name__ == "__main__":
    unittest.main()