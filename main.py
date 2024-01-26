import unittest

class TestAddition(unittest.TestCase):
    # added two tests
    def test_add_positive_numbers(self):
        self.assertEqual(2 + 2, 4)

    def test_add_negative_numbers(self):
        self.assertEqual(-5 + -3, -8)

if __name__ == '__main__':
    unittest.main()
