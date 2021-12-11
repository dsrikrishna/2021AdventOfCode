TEST_INPUT = """3,4,3,1,2"""

def simulate_fish_life(input_list,num_days):
    timer = [0 for i in range(9)]
    for i in input_list:
        timer[i]+=1
    for i in range(num_days):
  
        new_timer = timer[1:]+[0]
        new_timer[8] =timer[0]
        new_timer[6]+=timer[0]
        timer=new_timer
    return sum(timer)

input_list = [int(i) for i in TEST_INPUT.split(',')]
assert simulate_fish_life(input_list,18) == 26

assert simulate_fish_life(input_list,80) == 5934

puzzle_input = open('./input.txt').read().split(',')
puzzle_input = [int(i) for i in puzzle_input]

print(simulate_fish_life(puzzle_input,80))

print(simulate_fish_life(puzzle_input,256))