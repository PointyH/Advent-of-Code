import numpy as np
from copy import deepcopy

def remove_tail_gaps(arr):
    while arr[-1] == '.':
        arr.pop()
    return arr

def checksum_calc(files):
    t = 0
    for id,file in enumerate(files):
        t += id*file
    return t

def find_spaces(files,ref):
    valid = []
    for c,[id,num] in enumerate(files):
        if ref == (id,num):
            return valid
        if id == '.' and num >= ref[1]:
            valid.append(c)

def make_file(disc):
    files = []

    c = 0
    for file,space in disc:
        for _ in range(file):
            files.append(c)
        c += 1

        for _ in range(space):
            files.append('.')
    return files

def make_file_summary(disc):
    files_sum = []
    c = 0
    for file,space in disc:
        files_sum.append((c,file))
        c += 1

        files_sum.append(('.',space))

    files_rev = [i for i in files_sum[::-1]]

    return files_sum, files_rev

def move_block(id,num,files_sum,valid):
    files_sum[valid[0]] = ('.',files_sum[valid[0]][1]-num)
    files_sum[files_sum.index((id,num))] = (0,num)
    files_sum.insert(valid[0],(id,num))
    return files_sum

def task_1(disc):
    files = make_file(disc)

    files = remove_tail_gaps(files)
    for c,id in enumerate(files):
        if id == '.':
            files[c] = files[-1]
            files.pop()
            files = remove_tail_gaps(files)

    result = checksum_calc(files)
    return result

def task_2(disc):
    files_sum, files_rev = make_file_summary(disc)

    for c,[id,num] in enumerate(files_rev):
        if id != '.':
            valid = find_spaces(files_sum,(id,num))
            if len(valid) > 0:
                files_sum = move_block(id,num,files_sum,valid)

    files = []

    for [id,num] in files_sum:
        for _ in range(num):
            if id == '.':
                files.append(0)
            else:
                files.append(id)

    return checksum_calc(files)

#disc_raw = list(open("Day_9_test_input.txt").read())
disc_raw = list(open("Day_9_puzzle_input.txt").read())

disc_raw.append(0)
disc = list(map(int,disc_raw))

disc = np.array(disc).reshape(-1,2)

print('Task 1:',task_1(disc))
print('Task 2:',task_2(disc))