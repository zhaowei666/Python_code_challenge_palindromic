import unittest


def minimum_palindromic_base(num):
    """
    :param num: int
    :return: base: int
    """
    if num < 0:
        raise ValueError('num must be positive')
    base = 2
    while True:
        digits = []
        temp_num = num
        num_digits = 0
        while temp_num:
            digits = [temp_num % base] + digits
            temp_num //= base
            num_digits += 1
        if len(digits) > 1000:
            digits = digits[0: 1000]
        if digits == digits[::-1]:
            return base
        base += 1


test_cases = [{'num': 0, 'base': 2},
              {'num': 1, 'base': 2},
              {'num': 2, 'base': 3},
              {'num': 3, 'base': 2},
              {'num': 4, 'base': 3},
              {'num': 5, 'base': 2},
              {'num': 6, 'base': 5},
              {'num': 7, 'base': 2},
              {'num': 8, 'base': 3},
              {'num': 9, 'base': 2},
              {'num': 10, 'base': 3},
              {'num': 11, 'base': 10},
              {'num': 12, 'base': 5},
              {'num': 13, 'base': 3},
              {'num': 14, 'base': 6},
              {'num': 15, 'base': 2},
              {'num': 16, 'base': 3},
              {'num': 17, 'base': 2},
              {'num': 18, 'base': 5},
              {'num': 19, 'base': 18},
              {'num': 20, 'base': 3},
              {'num': 2 * (pow(2, 1000) - 1), 'base': 2},
              {'num': 3 * (pow(3, 1000) - 1), 'base': 3}
              ]

class TestMethods(unittest.TestCase):

    def test_minimum_palindromic_base(self):
        self.assertRaises(ValueError, minimum_palindromic_base, -1)
        for case in test_cases:
            self.assertEqual(minimum_palindromic_base(case['num']), case['base'])


if __name__ == '__main__':
    unittest.main()