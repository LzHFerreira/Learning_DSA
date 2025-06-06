import unittest
from core.hotel_message_system import HotelMessageSystem

class TestHotelMessageSystem(unittest.TestCase):
    def setUp(self):
        self.system = HotelMessageSystem()

    def test_add_message(self):
        self.system.add_message('Smith', 'John Smith', 'Welcome!')
        self.assertEqual(len(self.system.get_messages('Smith', 'John Smith')), 1)

    def test_get_messages(self):
        self.system.add_message('Smith', 'John Smith', 'Welcome!')
        messages = self.system.get_messages('Smith', 'John Smith')
        self.assertEqual(messages, ['Welcome!'])

    def test_remove_messages(self):
        self.system.add_message('Smith', 'John Smith', 'Welcome!')
        self.system.remove_messages('Smith', 'John Smith')
        messages = self.system.get_messages('Smith', 'John Smith')
        self.assertEqual(messages, [])

if __name__ == '__main__':
    unittest.main()
