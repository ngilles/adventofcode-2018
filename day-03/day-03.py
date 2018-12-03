import re

from collections import namedtuple
from itertools import chain
from pprint import pprint

input_txt = '''#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2'''

input_txt = open('input.txt', 'r').read()

Claim = namedtuple('Claim', 'id left top width height')
ex = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')

try:
    claims = [Claim(*[int(i) for i in ex.match(l).groups()]) for l in input_txt.split('\n')]
except Exception as e:
    print(e)

cloth_height = max(claim.top + claim.height for claim in claims)
cloth_width = max(claim.left + claim.width for claim in claims)


# Part 1
cloth = [[0] * cloth_width for _ in range(cloth_height)]

def cut_cloth(cloth, claim):
    for row in range(claim.top, claim.top + claim.height):
        cloth_bit = cloth[row][claim.left:claim.left + claim.width]
        cloth[row][claim.left:claim.left + claim.width] = [c + 1 for c in cloth_bit]

for claim in claims:
    cut_cloth(cloth, claim)

print(sum(1 for v in chain.from_iterable(cloth) if v > 1))


# Part 2
cloth = [[0] * cloth_width for _ in range(cloth_height)]

def cut_cloth(cloth, claim):
    new_intersection = set()
    for row in range(claim.top, claim.top + claim.height):
        cloth_bit = cloth[row][claim.left:claim.left + claim.width]
        for c  in cloth_bit:
            if c != 0:
                new_intersection.add(claim.id),
                new_intersection.add(c)
        cloth[row][claim.left:claim.left + claim.width] = [claim.id for c in cloth_bit]

    return new_intersection

claim_set = set(claim.id for claim in claims)

for claim in claims:
    intersects = cut_cloth(cloth, claim)
    for ic in intersects:
        if ic in claim_set:
            claim_set.remove(ic)


#pprint(cloth)
print(claim_set)
