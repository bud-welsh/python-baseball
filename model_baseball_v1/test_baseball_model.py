import baseball_model_v1
import unittest

class Test_GetProbability(unittest.TestCase):
    def test_single_probability(self):
        self.assertEqual(baseball_model_v1.single_probability(1, 3), 0.3333333333333333)

if __name__ == '__main__':
    unittest.main()