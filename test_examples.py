import unittest
from examples import *


class Test(unittest.TestCase):
    def test_feadforward_moon(self):
        feadforward_moon()
    def test_bigram(self):
        bigram()
    def test_bigramV2(self):
        bigramV2()
    def test_bigramV3(self):
        bigramV3()
    def test_bigramV4(self):
        bigramV4()
        

if __name__ == '__main__':
    unittest.main() 