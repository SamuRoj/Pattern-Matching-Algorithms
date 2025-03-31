# About this repo

Simple Python project that demonstrates different algorithms to determine if a string is a palindrome. The repository compares four different approaches with a comparation betweeen them in execution time.

## Palindrome Decision

First even then odd sorting algorithms.

### Problem statement
​
The problem is to check if a given string is a palindrome, meaning it reads the same forward and backward

### Examples

* For the string "racecar", the algorithms should determine it is a palindrome.

* For the string "hello", the algorithms should determine it is not a palindrome.

## Algorithms tested

### Two Pointers

This algorithm uses two pointers, one at the start of the string and the other at the end. The pointers move towards the center of the string, comparing characters at each step.

### Reversed String

This algorithm reverses the string and compares it with the original string. If the reversed string is the same as the original, it is a palindrome.

### Recursive

The recursive algorithm checks if a string is a palindrome by dividing the string into its two ends and checking if they are equal. It then recursively calls the function on the remaining substring (excluding the ends) until the string has a length of 1 or 0.

### Stack

This algorithm uses a stack to store half of the characters of the string. It then pops characters from the stack (which will be in reverse order) and compares them with the other half of the original string.

# Python version
Python 3.11.0
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
Name                           Stmts   Miss  Cover
--------------------------------------------------
palindrome\__init__.py             0      0   100%
palindrome\algorithms.py          37      0   100%
palindrome\constants.py            2      0   100%
palindrome\data_generator.py      39      5    87%
test\__init__.py                   0      0   100%
test\test_algorithms.py           27      1    96%
test\test_data_generator.py       47      1    98%
--------------------------------------------------
TOTAL                            152      7    95%
```

# Code beautifier
This code has been beautify using black: https://github.com/psf/black. 
The command to use is `black . -l 120`.
