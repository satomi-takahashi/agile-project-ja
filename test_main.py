from main import addition, check_choice, check_calculation_input, division, square_root

def test_addition():
    cases = [
        (1,2,3),
        (1.1,2,3.1),
    ]

    for case in cases:
        assert addition(case[0], case[1]) == case[2]

test_addition()

import unittest

class TestFunctions(unittest.TestCase):
    def test_division(self):
        self.assertAlmostEqual(division(10,2),5) #10 / 2 = 5と等しいかテスト
        self.assertAlmostEqual(division(5,2),2.5) #5 / 2 =2.5 と等しいかテスト

    def test_square_root(self):
        self.assertAlmostEqual(square_root(9),3) #9の平方根は３と等しいかテスト
        self.assertAlmostEqual(square_root(16),4) #16の平方根は４と等しいかテスト

if __name__ == '__main__':
    unittest.main()

