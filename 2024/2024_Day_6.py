def find_guard(board_grid):
    for y,row in enumerate(board_grid):
        for x,cell in enumerate(row):
            if cell in ('^','>','<','v'):
                return (x,y), cell

def task_1(board_grid,board):
    loc,direction = find_guard(board_grid)
    visited = set()

    running = True
    while running:
        visited.add(loc)
        new_loc = (loc[0]+movement[direction][0],loc[1]+movement[direction][1])
        if not board.get(new_loc,False):
            running = False
        elif board.get(new_loc)=='#':
            direction = keys[(keys.index(direction)+1)%4]
        else:
            loc = new_loc
    return visited

def check_repeat(board):
    loc,direction = find_guard(board_grid)
    visited = {}

    running = True
    while running:
        new_loc = (loc[0]+movement[direction][0],loc[1]+movement[direction][1])
        if not board.get(new_loc,False):
            return False
        elif board.get(new_loc)=='#':
            if direction in visited.get(new_loc,[]):
                return True
            if new_loc in visited.keys():
                visited[new_loc].append(direction)
            else:
                visited[new_loc] = [direction]
            direction = keys[(keys.index(direction)+1)%4]
        else:
            loc = new_loc
            
def task_2(board_grid,board):
    visited = task_1(board_grid,board)
    repeat = 0
    for loc in visited:
        if board[loc] == '.':
            board[loc] = '#'
            if check_repeat(board):
                repeat += 1
            board[loc] = '.'
    return repeat
        
#board_raw = open("Day_6_test_input.txt").read()
board_raw = open("Day_6_puzzle_input.txt").read()


movement = {'^':[0,-1],'>':[1,0],'v':[0,1],'<':[-1,0]}
keys = list(movement.keys())

board_grid = [list(i) for i in board_raw.split('\n')]
board = {(x,y):value for y,line in enumerate(board_grid) for x,value in enumerate(line)}

#Task 1
print('Task 1:',len(task_1(board_grid,board)))

#Task 2
print('Task 2:',task_2(board_grid,board))

            
