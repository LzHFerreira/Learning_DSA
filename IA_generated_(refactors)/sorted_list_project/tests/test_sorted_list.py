import unittest
from sorted_list.sorted_list import SortedList

class TestSortedList(unittest.TestCase):
    def test_add_single_element(self):
        sl = SortedList()
        sl.add(10)
        self.assertEqual(sl.to_list(), [10])

    def test_add_multiple_elements(self):
        sl = SortedList()
        sl.add(10)
        sl.add(5)
        sl.add(15)
        self.assertEqual(sl.to_list(), [5, 10, 15])

    def test_add_duplicate_elements(self):
        sl = SortedList()
        sl.add(10)
        sl.add(10)
        self.assertEqual(sl.to_list(), [10, 10])

    def test_add_elements_in_reverse_order(self):
        sl = SortedList()
        sl.add(15)
        sl.add(10)
        sl.add(5)
        self.assertEqual(sl.to_list(), [5, 10, 15])

if __name__ == '__main__':
    unittest.main()
