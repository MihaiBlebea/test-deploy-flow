import unittest
from app import People

class TestApp(unittest.TestCase):

    def test_name_is(self):
        self.people = People("Mihai", "Blebea")
        self.assertEqual(self.people.name_is(), "Mihai Blebea")

if __name__ == '__main__':
    unittest.main()
