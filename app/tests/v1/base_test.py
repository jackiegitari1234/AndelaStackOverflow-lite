import unittest
from app import create_app

class BaseTest(unittest.TestCase):

    def setUp(self):
        """ Initialize test variables """

        self.app = create_app()
        self.client = self.app.test_client()

    def tearDown(self):
        """ Destroy the test client when done """
        
        self.app.testing = False
        self.app = None
    
    if __name__ == '__main__':
        unittest.main()