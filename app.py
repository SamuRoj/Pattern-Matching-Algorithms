import sys
import random
from pattern_matching import algorithms
from pattern_matching import data_generator
from pattern_matching import execution_time_gathering

if __name__ == "__main__":
    minimum_size = 1000
    maximum_size = 5000
    step = 1000
    samples_by_size = 100
    
    # strings = []
    # substrings = []
    # for _ in range(20):
    #     string = data_generator.get_random_string(random.randint(1, 30))
    #     strings.append(string)
    #     substrings.append(data_generator.get_random_substring(True, string))

    # print("Strings: ", strings)
    # print("Substrings: ", substrings)
    
    table = execution_time_gathering.take_execution_time(minimum_size, maximum_size, step, samples_by_size)

    print("Size | Two Pointers | Reverse String | Recursive | Stack ")
    for row in table:
        print(row)
