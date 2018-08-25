import unittest
from app import fizzbuzz

class TestFizzbuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(1),1)
        self.assertEqual(fizzbuzz(3),'fizz')
        self.assertEqual(fizzbuzz(5),'buzz')
        self.assertEqual(fizzbuzz(15),'fizzbuzz')
        self.assertEqual(fizzbuzz(30),'fizzbuzz')
        self.assertEqual(fizzbuzz(99),'fizz')
        self.assertEqual(fizzbuzz(100),'buzz')
    

if __name__== '__main__':
    unittest.main()
            
        
