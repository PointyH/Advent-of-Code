import re
import numpy as np

#loc_ids_raw = open("Day_1_test_input.txt").read()
loc_ids_raw = open("Day_1_puzzle_input.txt").read()

loc_ids = np.array(re.split('\n|   ',loc_ids_raw)).astype('i')
loc_ids_reshape = loc_ids.reshape(-1,2)
loc_ids_t = np.transpose(loc_ids_reshape)
loc_ids_sort = np.sort(loc_ids_t, axis=1)

#Task 1
loc_ids_diff = [abs(a-b) for a,b in zip(loc_ids_sort[0],loc_ids_sort[1])]
print('Task 1:',sum(loc_ids_diff))

#Task 2
loc_ids_sort_0,loc_ids_sort_1 = loc_ids_sort

total = 0
for i in loc_ids_sort_0:
    total += sum(np.where(loc_ids_sort_1==i,1,0))*i
print('Task 2:',total)
