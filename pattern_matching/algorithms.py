def naive_approach(text, pattern):
    index = []
    n = len(text)
    m = len(pattern)
    for s in range(n - m + 1):
        if pattern == text[s : s + m]:
            index.append(s)
    return index

# O((n - m  + 1) * m) 

def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    d = 62
    prime = 1000000007
    hashP = 0
    hashT = 0
    index = []
    h = (d ** (m-1)) % prime
    for i in range(m):
        hashP = (d * hashP + ord(pattern[i])) % prime
        hashT = (d * hashT + ord(text[i])) % prime
    for s in range(n - m + 1):
        if hashP == hashT:
            if pattern == text[s : s + m]:
                index.append(s)
        if s < n - m:
            hashT = (d*(hashT - ord(text[s])*h) + ord(text[s + m])) % prime
    return index

# O(n * m)
# Best O(n + m)

def kmp_lps(pattern):
    l = 0
    i = 1
    lps = [0 for _ in range(len(pattern))]
    while i < len(pattern):
        if pattern[i] == pattern[l]:
            l += 1
            lps[i] = l
            i += 1
        else:
            if l != 0:
                l = lps[l - 1]
            else:
                i += 1
    return lps

def kmp(text, pattern):
    i = j = 0
    lps = kmp_lps(pattern)
    index = []
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
        if j == len(pattern):
            index.append(abs(len(pattern) - i))
            j = lps[j-1]
    return index

# O(m + n)