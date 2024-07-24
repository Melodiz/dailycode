import unittest
def max_wins(n, k, data):
    pivot = data[k-1]
    data = [pivot] + sorted([x for x in data if x != pivot])

    def iter(pivot, data):
        result = []
        for i in range(0, len(data)//2, 2):
            prev, cur = data[i], data[i+1]
            if prev > cur:
                result.append(prev)
                continue
            result.append(cur)
        if pivot not in result:
            return []
        return result

    def iter_odd(pivot, data):
        result = [data[0]]
        for i in range(1, len(data)//2 + 1, 2):
            prev, cur = data[i], data[i+1]
            if prev > cur:
                result.append(prev)
                continue
            result.append(cur)
        return result

    i = 0
    while len(data) > 1:
        if len(data) % 2 == 0:
            data = iter(pivot, data)
        else:
            data = iter_odd(pivot, data)
        i += 1
    return i


class TestMaxWins(unittest.TestCase):
    def test_example_case(self):
        n = 7
        k = 3
        skills = [4, 7, 1, 3, 6, 2, 5]
        self.assertEqual(max_wins(n, k, skills), 2)

    def test_single_robot(self):
        n = 1
        k = 1
        skills = [5]
        self.assertEqual(max_wins(n, k, skills), 0)

    def test_all_robots_same_skill(self):
        n = 4
        k = 2
        skills = [3, 3, 3, 3]
        self.assertEqual(max_wins(n, k, skills), 0)

    def test_k_robot_highest_skill(self):
        n = 5
        k = 1
        skills = [10, 1, 2, 3, 4]
        self.assertEqual(max_wins(n, k, skills), 2)

    def test_k_robot_lowest_skill(self):
        n = 5
        k = 5
        skills = [10, 9, 8, 7, 1]
        self.assertEqual(max_wins(n, k, skills), 0)

    def test_large_number_of_robots(self):
        n = 16
        k = 8
        skills = [i for i in range(1, 17)]
        self.assertEqual(max_wins(n, k, skills), 3)


if __name__ == '__main__':
    unittest.main()
