from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution

        dic = {1: 10, 4: 40, 2: 20, 3: 30}
        res = solution(dic)

        self.assertEqual(res[0], 1)
        self.assertEqual(res[1], 2)
        self.assertEqual(res[2], 3)
        self.assertEqual(res[3], 4)
