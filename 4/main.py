TEST_INPUT = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

input_data = TEST_INPUT.split('\n')
BOARD_SIZE = 5


def get_callout_numbers_processed_boards(input_data):
    callout_numbers = input_data[0].split(',')
    callout_numbers = [int(i) for i in callout_numbers]

    boards = []

    for i in range(2, len(input_data), BOARD_SIZE + 1):
        boards.append(input_data[i:i + BOARD_SIZE])

    processed_boards = []
    for board in boards:
        processed_board = []
        for row in board:
            split_row = row.split()
            processed_board.append([int(i) for i in split_row])
        processed_boards.append(processed_board)
    return callout_numbers, processed_boards


class Board:
    def __init__(self, board_array):
        self.board_array = board_array
        self.bingo_array = [[0 for i in range(BOARD_SIZE)]
                            for j in range(BOARD_SIZE)]

    def check_bingo(self):
        #check rows
        for i in self.bingo_array:
            if set(i) == set([1]):
                return True
        # check columns
        transpose_bingo_array = list(map(list, zip(*self.bingo_array)))
        for i in transpose_bingo_array:
            if set(i) == set([1]):
                return True
        # check diags
        # if set([self.bingo_array[i][i] for i in range(BOARD_SIZE)])==set([1]):
        #   return True
        # if set([self.bingo_array[i][BOARD_SIZE-1-i] for i in range(BOARD_SIZE)]) == set([1]):
        #   return True          

    def update_bingo(self, number):
        flattened = [i for s in self.board_array for i in s]
        matches = [i for i in range(len(flattened)) if flattened[i] == number]
        board_index_match = [[i // BOARD_SIZE, i % 5] for i in matches]
        for row, col in board_index_match:
            self.bingo_array[row][col] = 1

    def get_score(self,number):
      flattened = [i for s in self.board_array for i in s]
      bingo_flattened = [i for s in self.bingo_array for i in s]
      unmarked_sum = 0
      for index,i in enumerate(bingo_flattened):
        if i==0:
          unmarked_sum+=flattened[index]
      return unmarked_sum*number
          
def get_first_board_score(input_data):
  callout_numbers, processed_boards = get_callout_numbers_processed_boards(input_data)

  boards = [Board(i) for i in processed_boards]
  for number in callout_numbers:
    for board_number,board in enumerate(boards):
      board.update_bingo(number)
      if board.check_bingo():
        score = board.get_score(number)
        break
    else:
      continue
    break
  return score

def get_last_board_score(input_data):
  callout_numbers, processed_boards = get_callout_numbers_processed_boards(input_data)

  boards = [Board(i) for i in processed_boards]
  num_boards = list(range(len(boards)))
  for number in callout_numbers:
    for board_number,board in enumerate(boards):
      board.update_bingo(number)
      if board.check_bingo():
        score = board.get_score(number)
        try:
          num_boards.remove(board_number)
        except ValueError:
          pass # already removed
      if len(num_boards)==0:
        break
    else:
      continue
    break
  return score
print(get_first_board_score(input_data))
print(get_last_board_score(input_data))
print(20*'-')

input_data = open('input.txt').read().split('\n')
print(get_first_board_score(input_data))
print(get_last_board_score(input_data))

