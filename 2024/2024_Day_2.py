import numpy as np

def check_safe(a):
    if a == sorted(a) or a == sorted(a,reverse=True):
        diff = [abs(a[i]-a[i-1]) for i in range(1,len(a))]
        if max(diff) <= 3 and min(diff) >= 1:
            return True
        else:
            return False
    else:
        return False
    
#inp = open("Day_2_test_input.txt").readlines()
reports_raw = open("Day_2_puzzle_input.txt").readlines()

reports = [list(map(int,report.split(' '))) for report in reports_raw]

#Task 1
c = 0
for report in reports:
    if check_safe(report):
        c += 1
print('Task 1:',c)

#Task 2
c = 0
for report in reports:
    if check_safe(report):
        c += 1
    else:
        for i in range(len(report)):
            new_report = report.copy()
            new_report.pop(i)
            if check_safe(new_report):
                c += 1
                break
print('Task 2:',c)
    
