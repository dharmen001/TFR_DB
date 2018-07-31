from itertools import *

for perm in permutations('ABCD'):
    print(perm)

for comb in combinations('ABCD', 5):
    print(comb)

print(dir())