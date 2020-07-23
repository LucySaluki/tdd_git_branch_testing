import unittest

from compound_interest import CompoundInterest

class CompoundInterestTest(unittest.TestCase):

    # Tests
    # Should return 732.81 given 100 principal, 10 percent, 20 years           
    def test_principle_of_100_10_20_returns_732(self):
        compound_interest = CompoundInterest(100,10,20)
        self.assertAlmostEqual(732.81,compound_interest.compound_interest(),2)
    

    # Should return 181.94 given 100 principal, 6 percent, 10 years
    def test_principle_of_100_6_10_returns_182(self):
        compound_interest = CompoundInterest(100,6,10)
        self.assertAlmostEqual(181.94,compound_interest.compound_interest(),2)

    # Should return 149,058.55 given 100000 principal, 5 percent, 8 years
    def test_principle_of_100000_5_8_returns_149058(self):
        compound_interest = CompoundInterest(100000,5,8)
        self.assertAlmostEqual(149058.55,compound_interest.compound_interest(),2)

    # Should return 0.00 given 0 principal, 10 percent, 1 year
    def test_principle_of_0_10_1_returns_0(self):
        compound_interest = CompoundInterest(0,10,1)
        self.assertAlmostEqual(0.00,compound_interest.compound_interest(),2)

    # Should return 100.00 given 100 principal, 0 percent, 10 years
    def test_principle_of_100_0_10_returns_100(self):
        compound_interest = CompoundInterest(100,0,10)
        self.assertAlmostEqual(100.00,compound_interest.compound_interest(),2)


    # Extention tests

    # Should return 118,380.16 given 100 principal, 5 percent, 8 years, 1000 per month

    # Should return 156,093.99 given 100 principal, 5 percent, 10 years, 1000 per month

    # Should return 475,442.59 given 116028.86, 7.5 percent, 8 years, 2006 per month

    # Should return 718,335.96 given 116028.86 principal, 9 percent, 12 years, 1456 per month


if __name__ == "__main__":
    unittest.main()
