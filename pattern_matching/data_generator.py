import random
import string
from pattern_matching import constants

def get_random_list(size, limit=constants.MAX_VALUE):
    answer = []
    while len(answer) < size:
        answer.append(random.randint(0, limit))
    return answer

def get_random_x(limit=constants.MAX_VALUE):
    return random.randint(1, limit)

def get_random_string(size):
    chars = string.ascii_letters + string.digits
    result = "".join(random.choice(chars) for _ in range(size))

    n = len(result)
    l = random.randint(0, n // 2)
    pattern = result[l : l + 10]
    
    m = len(pattern)
    pos = 0
    while pos < n:
        num = random.randint(0, 100)
        
        if num <= 35: 
            altered_pattern = pattern[:]
            altered_pattern = altered_pattern[:random.randint(1, m)] + random.choice(chars)
            result = result[:pos] + altered_pattern + result[pos + m:]
            pos += m
        else:
            pos += 1

    return (result, pattern)

def generate_worst_case(size, samples_by_size):
    strings = []
    patterns = []
    for _ in range(samples_by_size):
        text = "a" * size 
        pattern = "a" * (size // 2) 
        strings.append(text)
        patterns.append(pattern)
    return (strings, patterns)

def generate_sample_strings(size, samples_by_size):
    strings = []
    patterns = []
    for _ in range(samples_by_size):
        ans = get_random_string(size)
        strings.append(ans[0])
        patterns.append(ans[1])
    return (strings, patterns)