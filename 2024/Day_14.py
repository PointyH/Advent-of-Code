import re

def product(arr):
    s = 1
    for i in arr:
        s *= i
    return s

def create_robots(robots_raw):
    robots = []
    for robot in robots_raw:
        movement = re.findall('-?\d+',robot)
        robots.append({'pos_x': int(movement[0]),
                            'pos_y': int(movement[1]),
                            'velo_x': int(movement[2]),
                            'velo_y': int(movement[3])})
    return robots

def move_robots(robots,iter=1):
    for c,robot in enumerate(robots):
        end_pos_x = (robot['pos_x']+iter*robot['velo_x'])%width
        end_pos_y = (robot['pos_y']+iter*robot['velo_y'])%height

        robots[c]['pos_x'] = end_pos_x
        robots[c]['pos_y'] = end_pos_y
    return robots

def score_quadrants(robots):
    quadrants = {'qtr':0,'qtl':0,'qbr':0,'qbl':0}
    half_height = int((height-1)/2)
    half_width = int((width-1)/2)
    for robot in robots:
        if robot['pos_x'] > half_width and robot['pos_y'] > half_height:
            quadrants['qbr'] += 1
        elif robot['pos_x'] < half_width and robot['pos_y'] > half_height:
            quadrants['qbl'] += 1
        elif robot['pos_x'] > half_width and robot['pos_y'] < half_height:
            quadrants['qtr'] += 1
        elif robot['pos_x'] < half_width and robot['pos_y'] < half_height:
            quadrants['qtl'] += 1

    return product(quadrants.values())

def score_christmas_tree(robots):
    board = build_board(robots)
    score = sum(board[31])+sum(board[63])
    return score

def build_board(robots):
    board = [[0 for i in range(width)] for j in range(height)]
    for robot in robots:
        board[robot['pos_y']][robot['pos_x']] = 1
    return board

def visualise_board(board):
    for row in board:
        r = ''
        for i in row:
            if i == 0:
                r += ' '
            else:
                r += 'O'
        print(r)

#robots_raw = open("Day_14_test_input.txt").read().split('\n')
#width,height = (11,7)
robots_raw = open("Day_14_puzzle_input.txt").read().split('\n')
width,height = (101,103)

robots = create_robots(robots_raw)
robots = move_robots(robots,iter=100)
print('Task 1:',score_quadrants(robots))

robots = create_robots(robots_raw)
best = {'seconds':0,'score':0,'board':[]}
for it in range(width*height):
    score = score_christmas_tree(robots)

    if score >= best['score']:
        board = build_board(robots)
        best = {'score':score, 'seconds':it, 'board':board}

    robots = move_robots(robots)

print('Task 2:',best['seconds'])
visualise_board(best['board'])