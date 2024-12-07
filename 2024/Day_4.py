import re
import copy

def count_xmas(inp):
    total = 0
    for line in inp:
        xmas = re.findall('XMAS',''.join(line))
        samx = re.findall('SAMX',''.join(line))
        total += len(xmas)+len(samx)
    return total

def transpose(arr):
    tup = list(zip(*arr))
    return [list(i) for i in tup]

def diag_straight_1(inp):
    new_mat = []
    n = len(inp[0])
    for i,line in enumerate(inp):
        for _ in range(i):
            line.insert(0,'H')
        line.extend(['H' for _ in range(n-i)])
        new_mat.append(line)
    new_mat_t = transpose(new_mat)
    return new_mat_t

def diag_straight_2(inp):
    new_mat = []
    n = len(inp[0])
    for i,line in enumerate(inp):
        for _ in range(n-i):
            line.insert(0,'H')
        line.extend(['H' for _ in range(i)])
        new_mat.append(line)
    new_mat_t = transpose(new_mat)
    return new_mat_t

def task_1(mat):
    inc = count_xmas(mat)
    totals.append(inc)

    mat_t = transpose(mat)
    inc = count_xmas(mat_t)
    totals.append(inc)

    diag_1 = diag_straight_1(mat)
    inc = count_xmas(diag_1)
    totals.append(inc)

    diag_2 = diag_straight_2(mat_t)
    inc = count_xmas(diag_2)
    totals.append(inc)

    return sum(totals)      

def task_2(mat):
    c = 0
    for x,line in enumerate(mat[1:-1], start=1):
        for y,letter in enumerate(line[1:-1], start=1):
            if letter == 'A':
                if mat[x-1][y-1] != mat[x+1][y+1] and mat[x+1][y-1] != mat[x-1][y+1]:
                    if all([mat[x+i][y+j] in ('S','M') for i,j in [[1,1],[1,-1],[-1,1],[-1,-1]]]):
                        c += 1
                    else:
                        continue
                else:
                    continue
            else:
                continue
    return c

#word_search_raw = open("Day_4_test_input.txt").readlines()
word_search_raw = open("Day_4_puzzle_input.txt").readlines()
word_search = [list(i) for i in word_search_raw]

totals = []
inc = 0

#Task 1
word_search_copy = copy.deepcopy(word_search)
print('Task 1:',task_1(word_search))

#Task 2
print('Task 2:',task_2(word_search_copy))



