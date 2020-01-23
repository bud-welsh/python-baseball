import baseball_model_v1
import unittest

class Test_GetProbability(unittest.TestCase):
    def test_single_probability(self):
        self.assertEqual(baseball_model_v1.single_probability(26, 187), 0.13903743315508021)

    def test_double_probability(self):
        self.assertEqual(baseball_model_v1.double_probability(8, 186), 0.043010752688172046)

    def test_triple_probability(self):
        self.assertEqual(baseball_model_v1.triple_probability(8, 1865), 0.004289544235924933)

if __name__ == '__main__':
    unittest.main()