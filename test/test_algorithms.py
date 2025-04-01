import unittest

from pattern_matching import algorithms

strings = [
    'ABABABABABABAB',
    'XYZXYZXYZXYZXYZXYZ',
    '123123123123123123',
    'abcdefgabcdefgabcdefg',
    'QWERTYQWERTYQWERTY',
    'aabbccaabbcc',
    'fhg8dgh1jh4khs8dhs0wlh8',
    'lkjsdflkj7t2yiu32kfiwe32w',
    'sldfk27gds8fh8w7h98d7hf98sd',
    'aaabbbcccaaabbbcccaaabbbccc',
    'hellohellohellohellohello',
    '12a34b56c78d90',
    'abcdabcdabcdabcd',
    'pythonpythonpython',
    'abc123abc456abc789abc',
    'hello123worldhello456world',
    'test1test2test3test4test5',
    'random123random456random789',
    'abcxyz123abcxyz456abcxyz789',
    'pattern1pattern2pattern3'
]

patterns = [
    'AB',
    'XYZ',
    '123',
    'abcdefg',
    'QWERTY',
    'aabbcc',
    'gh1j',          
    'kjsd',
    'gds8f',
    'ccc',
    'hello',
    '56c78',         
    'abcd',
    'python',
    'abc123',
    '981247hfasklf',         
    'oiqweroipfdlkvmKVLJD',
    'JFDLFNVLKZojdsfaofjaosijf',
    'qoipweroijdflkasdjflk',
    'oiweruoipjfklsdjfldsa',      
    'jasdlkfljweoiquroifdjlkfjas'  
]


expected = [
    [0, 2, 4, 6, 8, 10, 12],
    [0, 3, 6, 9, 12, 15],
    [0, 3, 6, 9, 12, 15],
    [0, 7, 14],
    [0, 6, 12],
    [0, 6],
    [5],
    [1],
    [7],
    [6, 15, 24],
    [0, 5, 10, 15, 20],
    [6],
    [0, 4, 8, 12],
    [0, 6, 12],
    [0],
    [],
    [],
    [],
    [],
    []
]

class AlgorithmsTests(unittest.TestCase):
    def test_naive_approach(self):
        for i in range(len(strings)):
            string = strings[i]
            pattern = patterns[i]
            self.assertEqual(algorithms.naive_approach(string, pattern), expected[i])

    def test_rabin_karp(self):
        for i in range(len(strings)):
            string = strings[i]
            pattern = patterns[i]
            self.assertEqual(algorithms.rabin_karp(string, pattern), expected[i])

    def test_knuth_morris_pratt(self):
        for i in range(len(strings)):
            string = strings[i]
            pattern = patterns[i]
            self.assertEqual(algorithms.kmp(string, pattern), expected[i])

if __name__ == "__main__":
    unittest.main()
