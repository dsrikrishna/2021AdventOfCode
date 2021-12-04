TEST_INPUT = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""
from collections import Counter


def get_gamma_rate_epsilon_rate(input_list):
    most_common = []
    least_common = []
    for i in range(len(input_list[0])):
        most_common.append(
            Counter([j[i] for j in input_list]).most_common()[0][0])
        least_common.append(
            Counter([j[i] for j in input_list]).most_common()[-1][0])
    return ''.join(most_common), ''.join(least_common)


most_common, least_common = get_gamma_rate_epsilon_rate(TEST_INPUT.split('\n'))

print(int(most_common, 2) * int(least_common, 2))

with open('input.txt') as fid:
    input_list = fid.readlines()
input_list = [i.strip() for i in input_list]
most_common, least_common = get_gamma_rate_epsilon_rate(input_list)
print(int(most_common, 2) * int(least_common, 2))

print('-' * 20)


def get_o2_co2_ratings(input_list):
    most_common = []
    least_common = []
    subset = input_list
    while len(subset) > 1:
        print('before:',len(subset))
        for i in range(len(input_list[0])):
          bit_counter = Counter([j[i]for j in subset]).most_common()
          most_common_bit = bit_counter[0][0]
          if len(bit_counter)==2:
            if bit_counter[0][1]==bit_counter[1][1]:
              most_common_bit='1'
          most_common.append(most_common_bit)
          subset = [j for j in subset if j[i] == most_common_bit]
          print('after:',len(subset))
    
    subset = input_list
    
    while len(subset)>1:
      print('before:',len(subset))
      for i in range(len(input_list[0])):
          bit_counter = Counter([j[i]for j in subset]).most_common()
          least_common_bit = bit_counter[-1][0]
          if len(bit_counter)==2:
            if bit_counter[0][1]==bit_counter[1][1]:
              least_common_bit='0'
          least_common.append(least_common_bit)
          subset = [j for j in subset if j[i] == least_common_bit]
          print('after:',len(subset))

    return ''.join(most_common), ''.join(least_common)


print(get_o2_co2_ratings(TEST_INPUT.split('\n')))

with open('input.txt') as fid:
    input_list = fid.readlines()
input_list = [i.strip() for i in input_list]
most_common, least_common = get_o2_co2_ratings(input_list)
print(int(most_common, 2) * int(least_common, 2))