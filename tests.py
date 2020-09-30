import unittest
import main


class Tests(unittest.TestCase):
    def test_00_exists(self):
        self.assertTrue(True)

    def test_01_reach_main(self):
        main.hello_world()

    def test_02_reach_api(self):
        pass


