import numpy as np

def calc_change(stone):
    if stone == 0:
        stone = [1]
    elif len(str(stone)) %2 == 0:
        stone_string = str(stone)
        firstpart, secondpart = stone_string[:len(stone_string)//2], stone_string[len(stone_string)//2:]
        stone = [int(firstpart),int(secondpart)]
    else:
        stone = [stone*2024]
    return stone

def blink(in_stones):
    out_stones = {}

    for in_key,in_val in in_stones.items():
        out_key = calc_change(in_key)
        
        for key in out_key:
            out_stones[key] = out_stones.get(key,0) + in_val
    return out_stones

def count_stones(stones):
    return sum(list(stones.values()))

def run_gaze(stones,blinks):
    for _ in range(blinks):
        stones = blink(stones)
    return count_stones(stones)

#inp = open("Day_11_test_input.txt").read()
inp = open("Day_11_puzzle_input.txt").read()
stones = inp.split(' ')

stones = {int(i):stones.count(i) for i in stones}

print('Task 1:',run_gaze(stones,25))
print('Task 2:',run_gaze(stones,75))
