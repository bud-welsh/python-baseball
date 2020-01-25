import baseball_model_v1
import unittest

class Test_GetProbability(unittest.TestCase):
    def test_single_probability(self):
        self.assertEqual(baseball_model_v1.single_probability(26, 187), 0.13903743315508021)

    def test_double_probability(self):
        self.assertEqual(baseball_model_v1.double_probability(8, 186), 0.043010752688172046)

    def test_triple_probability(self):
        self.assertEqual(baseball_model_v1.triple_probability(8, 1865), 0.004289544235924933)

    def test_home_run_probability(self):
        self.assertEqual(baseball_model_v1.home_run_probability(7, 187), 0.0374331550802139)

    def test_walk_probability(self):
        self.assertEqual(baseball_model_v1.walk_probability(16, 187), 0.0855614973262032)

    def test_strike_out_probability(self):
        self.assertEqual(baseball_model_v1.strike_out_probability(43, 187), 0.22994652406417113)

    def test_hit_by_pitch_probability(self):
        self.assertEqual(baseball_model_v1.hit_by_pitch_probability(20, 1865), 0.010723860589812333)

    def test_out_probability(self):
        self.assertEqual(baseball_model_v1.out_probability(111, 186), 0.5967741935483871)

class Test_RandomPlay(unittest.TestCase):
    def test_random_single(self):
        self.assertEqual(baseball_model_v1.random_play(0.13911), print())
    
if __name__ == '__main__':
    unittest.main()