
# Parse the input, one frequency shift per line
freq_shifts = [int(l) for l in open('input.txt', 'r')]

# Part 1 - simple sum of all shifts
print(sum(freq_shifts))

# Part 2 - Find first repeated sum
# Make a cumulative sum of infinite repeats, and find first repeat
from itertools import accumulate, cycle

seen = set([0])
for partial_sum in accumulate(cycle(freq_shifts)):
    if partial_sum in seen:
        break
    seen.add(partial_sum)

print(partial_sum)
