from collections import Counter

def find_let(let,field_dic):
    for key in list(field_dic.keys()):
        if field_dic[key] ==  let:
            return key

def find_adjacent(loc,field_dic):
    x,y = loc
    adj = [(x+x_mod,y+y_mod) for x_mod,y_mod in [[1,0],[-1,0],[0,1],[0,-1]] if field_dic.get((x+x_mod,y+y_mod),'1') == field_dic.get((x,y))[0]]
    return adj

def suffix_plots(plant,c,loc,field_dic):
    adj = find_adjacent(loc,field_dic)
    for loc in adj:
        field_dic[loc] = f'{plant}_{c}'
        field_dic = suffix_plots(plant,c,loc,field_dic)
    return field_dic

def split_plots(field):
    field_dic = {(x,y): value for y,row in enumerate(field) for x,value in enumerate(row)}
    areas = find_areas(field_dic)
    for plant in list(areas.keys()):
        c = 0
        while plant in list(field_dic.values()):
            c += 1
            loc = find_let(plant,field_dic)
            field_dic[loc] = f'{plant}_{c}'
            field_dic = suffix_plots(plant,c,loc,field_dic)
    return field_dic

def find_areas(field):
    areas = Counter()
    for key in list(field.keys()):
        areas[field[key]] += 1
    return areas

def find_perimeters(field):
    perimeters = Counter()
    for key in list(field_dic.keys()):
        adj = [True for x_mod,y_mod in [[1,0],[-1,0],[0,1],[0,-1]] if field_dic.get((key[0]+x_mod,key[1]+y_mod),'1') == field_dic.get((key[0],key[1]))]
        perimeters[field[key]] += 4-len(adj)
    return perimeters  

def find_corners(field):
    corners = Counter()
    mods = [[1,1],[1,-1],[-1,1],[-1,-1]]
    for key_x,key_y in list(field.keys()):
        for x_mod,y_mod in mods:
            peripheries = [field.get((key_x,key_y)) == field.get((key_x,key_y+y_mod)),field.get((key_x,key_y)) == field.get((key_x+x_mod,key_y))]
            if field.get((key_x,key_y)) != field.get((key_x+x_mod,key_y+y_mod)) and (all(peripheries) or not any(peripheries)):
                corners[field[(key_x,key_y)]] += 1
            elif not any (peripheries):   
                corners[field[(key_x,key_y)]] += 1
    return corners

def calc_cost(areas, perimeters):
    tot = 0
    for key in perimeters:
        tot += perimeters[key]*areas[key]
    return tot

#inp = open("Day_12_test_input.txt").read().split('\n')
inp = open("Day_12_puzzle_input.txt").read().split('\n')
field = [list(i) for i in inp]
field_dic = split_plots(field)

areas = find_areas(field_dic)
perimeters = find_perimeters(field_dic)
print('Task 1:',calc_cost(areas,perimeters))

corners = find_corners(field_dic)
print('Task 2:',calc_cost(areas,corners))