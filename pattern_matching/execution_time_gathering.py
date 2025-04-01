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

def take_execution_time_choose(minimum_size, maximum_size, step, samples_by_size, algorithms):
    return_table = []

    for size in range(minimum_size, maximum_size + 1, step):
        print("Processing size: " + str(size))
        table_row = [size]
        times = take_times_choose(size, samples_by_size, algorithms)
        return_table.append(table_row + times)

    return return_table


"""
    It will return three values, one for each algorithm: The execution time for that size on each algorithm
"""


def take_times(size, samples_by_size):
    samples = data_generator.generate_sample_strings(size, samples_by_size)

    return [
        take_time_for_algorithm(samples, algorithms.naive_approach),
        take_time_for_algorithm(samples, algorithms.rabin_karp),
        take_time_for_algorithm(samples, algorithms.kmp),
    ]

def take_times_choose(size, samples_by_size, algorithmsChoosed):
    results = []
    samples = data_generator.generate_worst_case(size, samples_by_size)

    if 1 in algorithmsChoosed:
        results.append(take_time_for_algorithm(samples, algorithms.naive_approach))
    if 2 in algorithmsChoosed:
        results.append(take_time_for_algorithm(samples, algorithms.rabin_karp))
    if 3 in algorithmsChoosed:
        results.append(take_time_for_algorithm(samples, algorithms.kmp))

    return results

"""
    Returns the median of the execution time measures for a palindrome approach given in 
"""

def take_time_for_algorithm(samples_array, pattern_approach):
    times = []

    for i in range(len(samples_array)):
        start_time = time.time()
        pattern_approach(samples_array[0][i], samples_array[1][i])
        times.append(constants.TIME_MULTIPLIER * (time.time() - start_time))

    times.sort()
    return times[len(times) // 2]
