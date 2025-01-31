import unittest
import app

class unittest_key(unittest.TestCase):
    def test_match(self):
        result=app.sum_func(4)
        self.assertEqual(result, 16)
        
unittest.main()  
        
