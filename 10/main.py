from typing import Text

from statistics import median

TEST_INPUT = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

illegal_points_dict = {")": 3, "]": 57, "}": 1197, ">": 25137}
incomplete_points_dict = {")": 1, "]": 2, "}": 3, ">": 4}

class LineBracketTracker:
    def __init__(self, line) -> None:
        self.paren = 0  # 1 for every open and -1 for every close char
        self.square = 0
        self.angle = 0
        self.curly = 0

        self.paren_pos = None  # every as yet unmatched bracket pos will be stored here, reset after self.paren is 0
        self.square_pos = None
        self.angle_pos = None
        self.curly_pos = None

        self.line = line

    def check_line_corrupt_or_incomplete(self):
        for idx, i in enumerate(self.line):
            if i == "(":
                self.paren += 1
                if self.paren == 0:
                    self.paren_pos = None
                else:
                    self.paren_pos = idx
            elif i == ")":
                self.paren += -1
                if self.paren == 0:
                    self.paren_pos = None
                else:
                    self.paren_pos = idx
            elif i == "[":
                self.square += 1
                if self.square == 0:
                    self.square_pos = None
                else:
                    self.square_pos = idx
            elif i == "]":
                self.square += -1
                if self.square == 0:
                    self.square_pos = None
                else:
                    self.square_pos = idx
            elif i == "{":
                self.curly += 1
                if self.curly == 0:
                    self.curly_pos = None
                else:
                    self.curly_pos = idx
            elif i == "}":
                self.curly += -1
                if self.curly == 0:
                    self.curly_pos = None
                else:
                    self.curly_pos = idx
            elif i == "<":
                self.angle += 1
                if self.angle == 0:
                    self.angle_pos = None
                else:
                    self.angle_pos = idx
            elif i == ">":
                self.angle += -1
                if self.angle == 0:
                    self.angle_pos = None
                else:
                    self.angle_pos = idx

        print([self.square, self.angle, self.curly, self.paren])


lines = TEST_INPUT.split("\n")

# l = LineBracketTracker(lines[2])
# l.check_line_corrupt_or_incomplete()
def process_lines(line):
    complement_dict = {"(": ")", "[": "]", "<": ">", "{": "}"}

    expected_chars = []
    for i in line:
        if i in complement_dict.keys():
            expected_chars.append(complement_dict[i])
        elif expected_chars[-1] == i:
            expected_chars.pop()
        else:
            return i
    return expected_chars

def score_calcs(lines):
    illeage_points_score = 0
    incomplete_score_list = []
    for line in lines:
        incomplete_points_score = 0
        output = process_lines(line)
        if len(output)==1:
            illeage_points_score+=illegal_points_dict[output]
        else:
            scores = [incomplete_points_dict[i] for i in output]
            for i in scores[-1::-1]:
                incomplete_points_score*=5
                incomplete_points_score+=i
            incomplete_score_list.append(incomplete_points_score)
    return illeage_points_score, incomplete_score_list



lines = open('./10/input.txt').read().split('\n')

illegal_score, incomplete_list = score_calcs(lines)

print(illegal_score, median(incomplete_list))