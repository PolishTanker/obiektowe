import unittest
from trash import Trash

class TrashTest(unittest.TestCase):

    def setUp(self):
        self.testee = Trash(capacity=6)

    def test_can_add(self):
        self.testee[3] = 10
        self.assertTrue(10 in self.testee)  


    def test_can_delete(self):
        self.testee[3] = 10
        del self.testee[3]
        self.assertFalse(10 in self.testee)


# Zadanie A
    def test_len_method(self):

        self.assertEqual(len([val for val in self.testee if val != 0]), 0)
        
        self.testee[1] = 5
        self.assertEqual(len([val for val in self.testee if val != 0]), 1)

        self.testee[2] = 10
        self.testee[4] = 20
        self.assertEqual(len([val for val in self.testee if val != 0]), 3)


    def test_delitem_method(self):
        with self.assertRaises(IndexError):
            del self.testee[6]  # Trying to delete outside the capacity

        self.testee[2] = 10
        del self.testee[2]
        self.assertFalse(10 in self.testee)


# Zadanie B
    def test_can_override(self):
        self.testee[3] = 10
        self.testee[3] = 20
        self.assertEqual(self.testee[3], 20)

    def test_setitem_out_of_range(self):
        with self.assertRaises(IndexError):
            self.testee[10] = 5

# Zadanie C
    def test_can_iterate_empty_trash(self):
        vals = list(self.testee)
        self.assertEqual(vals, [])

    def test_can_iterate_non_empty_trash(self):
        self.testee[2] = 10
        self.testee[4] = 20

        vals = [val for val in self.testee]
        self.assertEqual(vals, [10, 20])

if __name__ == '__main__':
    unittest.main()
