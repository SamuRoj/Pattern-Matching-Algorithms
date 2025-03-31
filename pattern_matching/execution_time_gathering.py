import time

from pattern_matching import algorithms
from pattern_matching import constants
from pattern_matching import data_generator


def take_execution_time(minimum_size, maximum_size, step, samples_by_size):
    return_table = []

    for size in range(minimum_size, maximum_size + 1, step):
        print("Processing size: " + str(size))
        table_row = [size]
        times = take_times(size, samples_by_size)
        return_table.append(table_row + times)

    return return_table

def take_execution_time_choose(minimum_size, maximum_size, step, samples_by_size, algorithms, isPalindrome):
    return_table = []

    for size in range(minimum_size, maximum_size + 1, step):
        print("Processing size: " + str(size))
        table_row = [size]
        times = take_times_choose(size, samples_by_size, algorithms, isPalindrome)
        return_table.append(table_row + times)

    return return_table


"""
    It will return three values, one for each algorithm: The execution time for that size on each algorithm
"""


def take_times(size, samples_by_size):
    samples = data_generator.generate_palindromes(size, samples_by_size, True)

    return [
        take_time_for_algorithm(samples, algorithms.two_pointers),
        take_time_for_algorithm(samples, algorithms.reverse_string),
        take_time_for_algorithm(samples, algorithms.recursive),
        take_time_for_algorithm(samples, algorithms.stack),
    ]

def take_times_choose(size, samples_by_size, algorithmsChoosed):
    results = []
    # samples = data_generator.generate_palindromes(size, samples_by_size)
    samples = []

    if 1 in algorithmsChoosed:
        results.append(take_time_for_algorithm(samples, algorithms.two_pointers))
    if 2 in algorithmsChoosed:
        results.append(take_time_for_algorithm(samples, algorithms.reverse_string))
    if 3 in algorithmsChoosed:
        results.append(take_time_for_algorithm(samples, algorithms.recursive))
    if 4 in algorithmsChoosed:
        results.append(take_time_for_algorithm(samples, algorithms.stack))

    return results

"""
    Returns the median of the execution time measures for a palindrome approach given in 
"""

def take_time_for_algorithm(samples_array, pattern_approach):
    times = []

    for sample in samples_array:
        start_time = time.time()
        pattern_approach(sample)
        times.append(constants.TIME_MULTIPLIER * (time.time() - start_time))

    times.sort()
    return times[len(times) // 2]
