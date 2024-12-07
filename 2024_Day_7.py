import re

def make_integer(arr):
    return list(map(int,arr))

def target_reachable(target,sofar,calc,operations):
    for op in operations:
        if len(calc) == 0:
            return sofar, True
        if op == '+':
            new_sofar = sofar+calc[0]
        elif op == 'x':
            new_sofar = sofar*calc[0]
        elif op == '||':
            new_sofar = int(str(sofar)+str(calc[0]))
        new_sofar,done = target_reachable(target,new_sofar,calc[1:],operations)
        if new_sofar == target and done:
            return new_sofar, done
        else:
            done = False
    return sofar,done

def run_calculations(targets, calcs, operations):
    total = 0
    for target, calc in zip(targets, calcs):
        sofar = calc[0]
        sofar, done = target_reachable(target,sofar,calc[1:],operations)
        if sofar == target:
            total += target
    return total

#inp = open("Day_7_test_input.txt").read()
inp = open("Day_7_puzzle_input.txt").read()
targets = make_integer(re.findall('(\d+):',inp))
calcs = [make_integer(line[1:].split(' ')) for line in re.findall(':(.*)',inp)]

#Task 1
print('Task 1:',run_calculations(targets, calcs, ['+','x']))

#Task 2
print('Task 2:',run_calculations(targets, calcs, ['+','x','||']))