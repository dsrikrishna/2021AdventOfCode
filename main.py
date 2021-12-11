TEST_INPUT = """3,4,3,1,2"""

from math import floor


def simulate_lantern_fish_brute(input_list, num_days=80):
    current_list = input_list

    for j in range(num_days):
        for i in current_list:
            if i == 0:
                current_list.append(9)
        next_day_list = [(i - 1) if i > 0 else 6 for i in current_list]
        current_list = next_day_list
    return current_list


def simulate_lantern_fish(input_list, num_days=80):
    number_of_fish = 0
    for i in input_list:
        number_of_fish, child_fish_start_days = simulate_fish_generated(
            i, num_days)




def simulate_fish_generated(starting_life, days_left):
    if days_left<=0:
        return 0,[]
    else: 
        if starting_life != 8:
            number_of_fish_generated = (days_left - starting_life) // 7 + 1
            child_fish_start_days = [
                starting_life + i * 7 + 1
                for i in range(0, int(floor(days_left - starting_life) / 7))
            ]
        elif starting_life == 8:
            number_of_fish_generated = (days_left - starting_life-8) // 7 + 1

            child_fish_start_days = [8]
            child_fish_start_days.extend([starting_life+i*7+1 for i in range(0, int(floor(days_left - starting_life) / 7))])
        
        for c_d in child_fish_start_days:
            c_days_left = days_left - c_d
            n, c = simulate_fish_generated(8,c_days_left)
            number_of_fish_generated+=n
        return number_of_fish_generated, child_fish_start_days


# input_list = [int(i) for i in TEST_INPUT.split(',')]
# output=simulate_lantern_fish(input_list,18)
# expected_output =[6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8]
# assert output==expected_output

# print(len(output))
# print(len(simulate_lantern_fish(input_list,200)))

# input_data = open('input.txt').read()
# input_list = [ int(i) for i in input_data.split(',')]
# print(len(simulate_lantern_fish(input_list,80)))

# print(simulate_fish_generated(3, 19))

input_list = [int(i) for i in TEST_INPUT.split(',')]


NUM_DAYS = 80
num_fish = len(input_list)
for i in input_list:
    num_fish += simulate_fish_generated(i, NUM_DAYS)[0]

print(num_fish)
