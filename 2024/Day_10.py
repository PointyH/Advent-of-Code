def find_trailheads(topo):
    trailheads = []
    for key in list(topo.keys()):
            if topo[key] == 0:
                trailheads.append(key)
    return trailheads

def find_next_level(locs,topo):
    squares = set()
    old_height = topo.get(locs[0])
    for x,y in locs:
        mod = [[1,0],[-1,0],[0,1],[0,-1]]
        adj = {(x+x_mod,y+y_mod) for x_mod,y_mod in mod if topo.get((x+x_mod,y+y_mod)) == old_height+1}
        squares.update(adj)
    if old_height == 8:
        return squares
    else:
        squares = find_next_level(list(squares),topo)
    return squares

def find_path(loc,total,topo):
    x,y = loc
    old_height = topo.get(loc)

    mod = [[1,0],[-1,0],[0,1],[0,-1]]
    squares = [(x+x_mod,y+y_mod) for x_mod,y_mod in mod if topo.get((x+x_mod,y+y_mod)) == old_height+1]
    if old_height == 8:
        total += len(squares)
        return total
    else:
        for square in squares:
            total = find_path(square,total,topo)
    return total





#inp = open("Day_10_test_input.txt").read()
inp = open("Day_10_puzzle_input.txt").read()

topo = {(int(x),int(y)): int(val) for y,row in enumerate(inp.split('\n')) for x,val in enumerate(row)}

trailheads = find_trailheads(topo)

tot = 0
for loc in trailheads:
    tot += len(find_next_level([loc],topo))
print('Task 1:', tot)

total = 0
for loc in trailheads:
    total += find_path(loc,0,topo)
print('Task 2:',total)