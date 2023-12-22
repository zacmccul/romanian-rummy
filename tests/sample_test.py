import unittest
import setup
import sample

setup.init()


class Test(unittest.TestCase):
    def test1(self):
        self.assertTrue(sample.test_func())
