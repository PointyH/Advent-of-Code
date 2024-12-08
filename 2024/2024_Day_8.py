from itertools import permutations
from copy import deepcopy

def count_hash(arr):
    t = 0
    for line in arr:
        t += line.count('#')
    return t

#antennae_raw = open("Day_8_test_input.txt").read()
antennae_raw = open("Day_8_puzzle_input.txt").read()

antennae_1 = [list(line) for line in antennae_raw.split('\n')]
antennae_2 = deepcopy(antennae_1)

antennae_loc = {}

for y,line in enumerate(antennae_1):
    for x,antenna in enumerate(line):
        if antenna != '.':
            if antenna in list(antennae_loc.keys()):
                antennae_loc[antenna].append((y,x))
            else:
                antennae_loc[antenna] = [(y,x)]

for key in list(antennae_loc.keys()):
    comb = list(permutations(antennae_loc[key],2))
    for a1,a2 in comb:
        new_y,new_x = [a1[0],a1[1]]
        c = 0
        while all([i>=0 and i<len(antennae_1) for i in (new_x,new_y)]):
            if c == 1:
                antennae_1[new_y][new_x] = '#'
            antennae_2[new_y][new_x] = '#'
            new_y,new_x = [new_y+a1[0]-a2[0],new_x+a1[1]-a2[1]]
            c += 1

print('Task 1:',count_hash(antennae_1))
print('Task 2:',count_hash(antennae_2)) 