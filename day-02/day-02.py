
from collections import Counter

box_ids = [
    'abcdef',
    'bababc',
    'abbcde',
    'abcccd',
    'aabcdd',
    'abcdee',
    'ababab',
]

box_ids = [l.strip() for l in open('input.txt', 'r')]

# Count the number of each letter in the box ids
freqs = [Counter(box_id) for box_id in box_ids]

doubles = sum(1 for box_id_freqs in freqs if 2 in box_id_freqs.values())
triplets = sum(1 for box_id_freqs in freqs if 3 in box_id_freqs.values())

def diffs(s1,s2):
    return sum(1 for a, b in zip(s1, s2) if a != b)

print(doubles*triplets)

# O(n^2) yuck, but hey, we don't have so many!
print([(s1, s2) for s1 in box_ids for s2 in box_ids if diffs(s1,s2) == 1])
