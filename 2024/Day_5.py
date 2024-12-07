def page_correct(c,page,update):
    if any([i in update[c:] for i in rules.get(page,[0])]):
        return False
    else:
        return True

def validate_order(update):
    for c,page in enumerate(update):
        if not page_correct(c,page,update):
            return False
        else:
            pass
    return True

def move_page(page, arr,rules):
    arr.remove(page)
    for i in range(len(arr)-1,-1,-1):
        if arr[i] in rules.get(page,[0]):
            arr.insert(i+1,page)
            return arr

def calc_answer(arr):
    return sum([int(i[int(len(i)/2-0.5)]) for i in arr])

#manual_raw = open("Day_5_test_input.txt").read()
manual_raw = open("Day_5_puzzle_input.txt").read()

manual = manual_raw.split('\n')

rules = {}
updates = []
for line in manual:
    if '|' in line:
        val = int(line[:2])
        key = int(line[-2:])

        if key in rules.keys():
            rules[key].append(val)
        else:
            rules[key] = [val]
    elif line == '':
        continue
    else:
        updates.append(list(map(int,line.split(','))))

#Task 1
correct = []
incorrect = []
for update in updates:
    valid = validate_order(update)
    if valid:
        correct.append(update)
    else:
        incorrect.append(update)
print('Task 1:',calc_answer(correct))

#Task 2
reordered = []
for update in incorrect:
    update_copy = update.copy()
    while not validate_order(update):
        for c,page in enumerate(update):
            if not page_correct(c,page,update):
                update_copy = move_page(page, update_copy,rules)
        update = update_copy.copy()
    reordered.append(update)

print('Task 2:',calc_answer(reordered))
            
    
        
