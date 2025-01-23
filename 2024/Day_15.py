def find_char(warehouse):
    for key,val in warehouse.items():
        if val == '@':
            return list(key)

def mod_map(warehouse):
    replace = {'O':'[]','#':'##','@':'@.','.':'..'}
    warehouse_new = []
    for row in warehouse:
        r = ''
        for val in row:
            r += replace[val]
        warehouse_new.append(r)
    warehouse = {(x,y): warehouse_new[y][x] for y in range(len(warehouse_new)) for x in range(len(warehouse_new[0]))}
    return warehouse
    
def add(point,direction):
    return (point[0]+direction[0],point[1]+direction[1])

def move(moving_from,moving_to,warehouse):
    warehouse[moving_to] = warehouse[moving_from]
    warehouse[moving_from] = '.'
    return warehouse

def move_char(warehouse,loc_from,d):
    loc_to = add(loc_from, move_dir[d])
    if warehouse[loc_to] == '.':
        warehouse = move(loc_from,loc_to,warehouse)
        return warehouse,True, loc_to
        
    elif warehouse[loc_to] == '#':
        return warehouse,False, loc_from

    elif warehouse[loc_to] == 'O' or (warehouse[loc_to] in ('O','[',']') and d in ('>','<')):
        warehouse,free,_ = move_char(warehouse,loc_to,d)
        if free:
            warehouse = move(loc_from,loc_to,warehouse)
            return warehouse,free,loc_to
        return warehouse,free,loc_from

    elif warehouse[loc_to] in ('[',']') and d in ('^','v'):
        otherhalf = {'[':(1,0),']':(-1,0)}
        moving = [loc_from]
        for value in moving:
            next = add(value,move_dir[d])
            if warehouse[next] == '#':
                return warehouse,False,loc_from
            elif warehouse[next] in ('[',']') and next not in moving:
                moving.append(next)
                if add(next,otherhalf[warehouse[next]]) not in moving:
                    moving.append(add(next,otherhalf[warehouse[next]]))
        for moving_from in moving[::-1]:
            moving_to = add(moving_from,move_dir[d])
            warehouse = move(moving_from,moving_to,warehouse)
        return warehouse,True,loc_to


def calc_gps(warehouse):
    score = 0
    for key,val in warehouse.items():
        if val in ('O','['):
            score += 100*key[1]+key[0]
    return score

def simulate_movement(warehouse,directions):
    char_loc = find_char(warehouse)

    for d in directions:
        loc_from = tuple(char_loc)
        warehouse,free, char_loc = move_char(warehouse,loc_from,d)
        char_loc = list(char_loc)
    return warehouse

def print_warehouse(warehouse):
    prev = [0,0]
    row = ''
    for key,val in warehouse.items():
        if key[1] == prev[1]:
            row += val
        else:
            print(row)
            row = val
        prev = key
    print(row)

#warehouse_raw = open("Day_15_test_input.txt").read().split('\n')
warehouse_raw = open("Day_15_puzzle_input.txt").read().split('\n')

split = warehouse_raw.index('')
warehouse_lis = warehouse_raw[:split]
warehouse = {(x,y): warehouse_raw[y][x] for y in range(len(warehouse_lis)) for x in range(len(warehouse_raw[0]))}

directions = ''
for direction_seg in warehouse_raw[split+1:]:
    directions += direction_seg
directions = list(directions)

move_dir = {'^':[0,-1],'<':[-1,0],'>':[1,0],'v':[0,1]}
#print_warehouse(warehouse)
warehouse = simulate_movement(warehouse,directions)
print('Task 1:',calc_gps(warehouse))
#print_warehouse(warehouse)

warehouse = mod_map(warehouse_lis)
#print_warehouse(warehouse)
warehouse = simulate_movement(warehouse,directions)
print('Task 2:',calc_gps(warehouse))
#print_warehouse(warehouse)