TEST_INPUT = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

MASTER = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg'
}
MASTER_COUNTER = {'a': 8, 'b': 6, 'c': 8, 'd': 7, 'e': 4, 'f': 9, 'g': 7}

from collections import Counter


class SegmentMapper:
    def __init__(self,digits_string):
        self.mapper = dict((k, '') for k in 'abcdefg')
        self.process_numeral_strings(digits_string)

    def process_numeral_strings(self, input_string):
        counter = Counter("".join(input_string.split(" ")))
        list_of_strings  = input_string.split(" ")
        self.mapper['e'] = [i for i in counter.keys() if counter[i] == 4][0]
        self.mapper['b'] = [i for i in counter.keys() if counter[i] == 6][0]
        self.mapper['f'] = [i for i in counter.keys() if counter[i] == 9][0]
    
        string_for_7 = [i for i in list_of_strings if len(i)==3][0]
        string_for_1 = [i for i in list_of_strings if len(i)==2][0]
        string_for_4 = [i for i in list_of_strings if len(i)==4][0]
        string_for_8 = [i for i in list_of_strings if len(i)==7][0]
        # self.mapper['a']="".join(sorted(string_for_7)).replace("".join(sorted(string_for_1)),'')
        self.mapper['a']=list(set(sorted(string_for_7)) - set(sorted(string_for_1)))[0]

        self.mapper['c']=''.join([i for i in counter.keys() if counter[i]==8]).replace(self.mapper['a'],'')
        known_segments_4 = "".join(sorted(self.mapper['b']+self.mapper['c']+self.mapper['f']))


        self.mapper['d'] = "".join(sorted(string_for_4)).replace(known_segments_4,'')
        self.mapper['d'] = list(set(sorted(string_for_4)) - set(sorted(known_segments_4)))[0]

        self.mapper['g'] = list(set(sorted(string_for_8)) - set(sorted(list(self.mapper.values()))))[0]
        self.get_number_map()
    
    def get_number_map(self):
        self.number_map = dict((i,'') for i in range(10))

        for i in range(10):
            self.number_map[i] = "".join(sorted([self.mapper[j] for j in MASTER[i]]))

    def give_number_from_string(self,string):
        for i in range(10):
            if self.number_map[i]=="".join(sorted(string)):
                return i



def count_simple_numbers(lines):
    count_simple = 0
    for line in input_lines:
        digits = line.split("|")[1].strip().split(" ")
        lengths = [len(i) for i in digits]
        for i in lengths:
            if i in [2, 3, 4, 7]:
                count_simple += 1
    return count_simple

input_lines = TEST_INPUT.split('\n')

# print(count_simple_numbers(input_lines))
# print(input_lines)
# input_lines = open('input.txt').read().split('\n')
# print(count_simple_numbers(input_lines))
def decode_numbers(input_lines):
    numbers = []
    for line in input_lines:
        digits, number_to_decode = line.split("|")
        digits =digits.strip()
        number_to_decode=number_to_decode.strip().split(" ")
        digits_mapper = SegmentMapper(digits)
        decoded_digits = []
        for i in number_to_decode:
            decoded_digits.append(str(digits_mapper.give_number_from_string(i.strip())))
        decoded_number = int("".join(decoded_digits))
        numbers.append(decoded_number)
    return numbers

input_lines = open('input.txt').read().split('\n')
print(sum(decode_numbers(input_lines)))