import re

def solve_simultaneous(machine):
    ratio = abs((machine['p_y']*machine['a_x']-machine['p_x']*machine['a_y'])/(machine['p_y']*machine['b_x']-machine['p_x']*machine['b_y']))
    na = machine['p_x']/(machine['a_x']+machine['b_x']*ratio)
    nb = ratio*na

    return (na,nb)

def create_machines(codes,mod):
    machines = []
    for code in codes:
        movements = re.match('Button A: X\+(?P<a_x>\d+), Y\+(?P<a_y>\d+)\\nButton B: X\+(?P<b_x>\d+), Y\+(?P<b_y>\d+)\\nPrize: X=(?P<p_x>\d+), Y=(?P<p_y>\d+)',code)
        machines.append({'a_x':int(movements.group('a_x')),'a_y':int(movements.group('a_y')),
                        'b_x':int(movements.group('b_x')),'b_y':int(movements.group('b_y')),
                        'p_x':int(movements.group('p_x'))+mod,'p_y':int(movements.group('p_y'))+mod})
    return machines

def calc_cost(machines):
    total = 0
    for machine in machines:
        na,nb = solve_simultaneous(machine)
        na,nb = (int(round(na,0)),int(round(nb,0)))

        if na*machine['a_x']+nb*machine['b_x'] == machine['p_x'] and na*machine['a_y']+nb*machine['b_y'] == machine['p_y']:
            total += 3*na+nb

    return total


#codes = open("Day_13_test_input.txt").read().split('\n\n')
codes = open("Day_13_puzzle_input.txt").read().split('\n\n')

machines = create_machines(codes,0)
print('Task 1:',calc_cost(machines))

machines = create_machines(codes,10000000000000)
print('Task 2:',calc_cost(machines))