import unittest
from pattern_matching import data_generator
from pattern_matching import constants


class DataGeneratorTest(unittest.TestCase):
    def test_data_generator_with_empty_list(self):
        N = 0
        random_list = data_generator.get_random_list(N)
        self.assertTrue(N == len(random_list))
        pass

    def test_data_generator_with_1(self):
        N = 1
        random_list = data_generator.get_random_list(N)
        self.assertTrue(N == len(random_list))
        pass

    def test_data_generator_with_2(self):
        N = 2
        random_list = data_generator.get_random_list(N)
        self.assertTrue(N == len(random_list))
        pass

    def test_data_generator_with_1000(self):
        N = 1000
        random_list = data_generator.get_random_list(N)
        self.assertTrue(N == len(random_list))
        for number in random_list:
            self.assertTrue(number <= constants.MAX_VALUE)
            self.assertTrue(number > 0)
        pass

    def test_data_generator_random_string(self):
        self.assertIsNotNone(data_generator.get_random_string(100))

    def test_data_generator_worst_case(self):
        N = 1000
        samples = 15
        strings, patterns = data_generator.generate_worst_case(N, samples)
        for i in strings: 
            self.assertEqual(len(i), N)
        self.assertEqual(len(strings), samples)

        for i in patterns: 
            self.assertEqual(len(i), N/2)
        self.assertEqual(len(patterns), samples)

    def test_data_generator_average_case(self):
        N = 1000
        samples = 15
        strings, patterns = data_generator.generate_sample_strings(N, samples)
        self.assertEqual(len(strings), samples)
        self.assertEqual(len(patterns), samples)

if __name__ == "__main__":
    unittest.main()
