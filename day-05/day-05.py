
import string

from collections import deque
from pprint import pprint

polymer = 'dabAcCaCBAcCcaDA'
polymer = open('input.txt', 'r').read()


def reduce_polymer(polymer, filter_type=None):
    reduced_polymer = deque()

    for e in (e for e in polymer if e.lower() != filter_type):
        if len(reduced_polymer) and e.swapcase() == reduced_polymer[-1]:
            reduced_polymer.pop()
        else:
            reduced_polymer.append(e)
    
    return ''.join(reduced_polymer)

# Part 1
reduced_polymer = reduce_polymer(polymer)
#print(reduced_polymer)
print(len(reduced_polymer))

# Part 2
print(min(len(reduce_polymer(polymer, e)) for e in string.ascii_lowercase))