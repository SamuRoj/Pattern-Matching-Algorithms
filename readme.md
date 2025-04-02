# About this repo

Simple Python project that demonstrates different algorithms of pattern matching. This repository compares three different approaches with a comparation betweeen them in execution time.

## Pattern Matching

### Problem statement
​
The pattern matching problem involves finding occurrences of a smaller string (the pattern) within a larger string (the text). The goal is to identify all positions in the text where the pattern appears. 

### Examples

* For the text "ababcababc" and the pattern "abc", the algorithms should determine that the pattern "abc" occurs at positions 2 and 7 in the text.

* For the text "hello world" and the pattern "world", the algorithms should determine that the pattern "world" occurs at position 6 in the text.

* For the text "ababababab" and the pattern "aba", the algorithms should determine that the pattern "aba" occurs at positions 0, 2, 4 and 6 in the text.

## Algorithms tested

### Naive Approach

This algorithm checks for a pattern in a given text by iterating over all possible starting positions in the text and comparing the substring with the pattern. It begins by aligning the pattern with the start of the text, and then checks each character of the text and pattern one by one. If a mismatch is found, it shifts the pattern by one position to the right and repeats the process until the pattern is found or all positions in the text are exhausted.

### Rabin Karp

This algorithm uses hashing to search for a pattern in the text. It computes the hash value of the pattern and compares it with the hash value of substrings of the text. If the hash values match, it then checks the characters one by one to confirm if the substring matches the pattern. The key advantage is the use of a rolling hash, which allows for efficient computation of the hash for consecutive substrings of the text by updating the previous hash value, rather than recomputing it from scratch.

### Knuth Morris Pratt

The KMP algorithm optimizes pattern matching by avoiding unnecessary re-evaluation of already matched characters. It uses a preprocessing step to create a partial match table, which helps determine how far to shift the pattern when a mismatch occurs. This table allows the algorithm to skip over sections of the text that have already been successfully matched, reducing the number of comparisons required during the matching process.

# Python version
Python 3.13.1
​
# Running locally and testing

* Note: This instructions are for mac. Windows or linux may require some changes. 
* A good idea for this project, is to use a virtual environment, you could set up one with: [virtualenv](https://virtualenv.pypa.io/en/latest/).
* To create the virtual environment: `virtualenv env`
* To activate it:`source env/bin/activate`
* To install dependencies: `pip3 install -r requirements.txt`
* To run unit testing: `./test.sh`
* To try a default example, run: `: ./run.sh`. In the file ./run.sh is just an example, you can modify it. Theck the `app.py` file to get to understand how it works.

# Current coverage

Make sure you have "coverage" in your requirements.txt file and run pip install. Then run `coverage run -m unittest discover` and after that run `coverage report` to get the following table:

```
Name                                 Stmts   Miss  Cover
--------------------------------------------------------
pattern_matching\__init__.py             0      0   100%
pattern_matching\algorithms.py          55      0   100%
pattern_matching\constants.py            2      0   100%
pattern_matching\data_generator.py      44      1    98%
test\__init__.py                         0      0   100%
test\test_algorithms.py                 23      1    96%
test\test_data_generator.py             47      1    98%
--------------------------------------------------------
TOTAL                                  171      3    98%
```

# Code beautifier
This code has been beautify using black: https://github.com/psf/black. 
The command to use is `black . -l 120`.
