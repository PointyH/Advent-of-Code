import re

#task 1
def task_1(memory):
    muls = re.findall('mul\([0-9]{1,3},[0-9]{1,3}\)',memory)

    total = 0
    for entry in muls:
        nums = re.search('(?P<num_1>\d+),(?P<num_2>\d+)',entry)
        num_1, num_2 = nums.group('num_1','num_2')
        total += int(num_1)*int(num_2)

    return total

def task_2(memory):
    dos = memory.split('do()')

    clean_memory = ''
    for entry in dos:
        rem_dont = entry.split("don't()")
        clean_memory += rem_dont[0]
    return clean_memory

#memory = open("Day_3_test_input.txt").read()
memory = open("Day_3_puzzle_input.txt").read()

#Task 1
print('Task 1:',task_1(memory))

#Task 2
clean_memory = task_2(memory)
print('Task 2:',task_1(clean_memory))