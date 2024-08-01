import unittest
from hello_world import hello_world,bye_world

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello, World!")

    
class TestByeWorld(unittest.TestCase):
    def test_bye_world(self):
        self.assertEqual(bye_world(),"Bye,World!")

if __name__ == '__main__':
    unittest.main()
