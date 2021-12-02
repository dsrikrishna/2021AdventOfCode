TEST_INPUT = """199
200
208
210
200
207
240
269
260
263"""


def count_increase(input_list):
    count = 0
    for i, j in zip(input_list, input_list[1:]):
        if j > i:
            count += 1
    return count


print(count_increase([int(i) for i in TEST_INPUT.split('\n')]))

with open('./input.txt') as fid:
    input_text = fid.readlines()

print(count_increase([int(i) for i in input_text]))


def count_window_increase(input_list, window=3):
    num_ele = len(input_list)
    sums = [sum(input_list[i:i + window]) for i in range(num_ele - window+1)]
    return count_increase(sums)


print(count_window_increase([int(i) for i in TEST_INPUT.split('\n')]))

print(count_window_increase([int(i) for i in input_text]))
