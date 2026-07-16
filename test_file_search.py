import unittest
from file_search import search


class TestKeyword(unittest.TestCase):

    def test_search(self):
        result=search("poem.txt")
        self.assertIn("poem.txt",result)

if __name__ == "__main__":
    unittest.main()