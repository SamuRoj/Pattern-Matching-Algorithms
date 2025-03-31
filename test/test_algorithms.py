import unittest

from pattern_matching import algorithms

strings = ['X9eB6uL7pQUDbXj', 'haRRYAuK', 'J0ZRFI8OJ3tr2knexGytHByqCh1', 'NKTo6SI7uZaFiMc', 'xJBy', 'ZDe', 
           'ZsxpzdccGG', '8vSRaKyWP8SQOzCSkTADY', 'wf0qGhU1qMZVxZYLgGgYAOu24N', 'xx61MD2FSX3OtOLU1xfdH58Zr', 
           'plnJ5r', 'ckYsIDB8n', 'kdfiZRpdCE5', 'OwogSocG64WXmWCfaL', 'U2A24lG8nOrkDn', 'jrxzUEQ25kaE9a2', 
           'S0hwfnwX9HMFeC97i', 'br12L3eUna1DXVmhsZG0Vs', '9iHiqXIW1hwuGa760kDEkmF8OW', 
           'nPSJEMzRKB0UaxNwYiLqbAkilS94j']

patterns = ['j', 'RR', '0ZRFI8OJ3tr2', '7', 'y', 'e', 'GG', '8vSRaKyWP8SQOzCS', 'u24', 'FSX3OtOLU1x', 'nJ5r', 
              'DB8n', 'R', '6', '4lG8n', '25', 'Fe', 's', '9', 'JEMzR']

class AlgorithmsTests(unittest.TestCase):
    def test_naive_approach(self):
        for i in range(len(strings)):
            string = strings[i]
            pattern = patterns[i]
            self.assertTrue(algorithms.naive_approach(string, pattern))

    def test_rabin_karp(self):
        for i in range(len(strings)):
            string = strings[i]
            pattern = patterns[i]
            self.assertTrue(algorithms.rabin_karp(string, pattern))

    def test_knuth_morris_pratt(self):
        for i in range(len(strings)):
            string = strings[i]
            pattern = patterns[i]
            self.assertTrue(algorithms.kmp(string, pattern))

if __name__ == "__main__":
    unittest.main()
