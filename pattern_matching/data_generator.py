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
    return "".join(random.choice(chars) for _ in range(size))

def get_random_substring(is_substring, string):
    if is_substring:
        n = len(string)
        l = random.randrange(0, n)
        r = random.randrange(l, n)
        return string[l: r+1]
    return "(("