import problem_001
import unittest


class TestProblemOne(unittest.TestCase):
    def test_sum_multiples(self):
        self.assertEqual(problem_001.sum_multiples(10), 23)
        self.assertEqual(problem_001.sum_multiples(20), 78)

    def test_is_multiple(self):
        self.assertEqual(problem_001.is_multiple([3], 9), True)
        self.assertEqual(problem_001.is_multiple([9], 27), True)
        self.assertEqual(problem_001.is_multiple([7], 14), True)