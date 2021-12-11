TEXT_INPUT = """16,1,2,0,4,2,7,1,2,14"""

input_list = [int(i) for i in TEXT_INPUT.split(',')]
def get_energy_vals(input_list):
    energy_vals = []
    for i in range(max(input_list)):
        # energy_vals.append(sum([abs(x-i) for x in input_list]))
        energy_vals.append(sum([abs(x-i)*(abs(x-i)+1)/2 for x in input_list]))
    return energy_vals
energy_vals = get_energy_vals(input_list)

print(min(energy_vals))
puzzle_input = open('./input.txt').read().split(',')
puzzle_input = [int(i) for i in puzzle_input]

energy_vals = get_energy_vals(puzzle_input)
print(min(energy_vals))
