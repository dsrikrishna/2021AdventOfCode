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

input_data=TEST_INPUT.split('\n')
BOARD_SIZE=5
def get_callout_numbers_processed_boards(input_data):
  callout_numbers = input_data[0].split(',')
  callout_numbers = [int(i) for i in callout_numbers]

  boards=[]

  for i in range(2,len(input_data),BOARD_SIZE+1):
    boards.append(input_data[i:i+BOARD_SIZE])
  
  processed_boards = []
  for board in boards:
    processed_board = []
    for row in board:
      split_row=row.split()
      processed_board.append([int(i) for i in split_row])
    processed_boards.append(processed_board)
  return callout_numbers, processed_boards

def find_bingo_board(callout_numbers,processed_boards):
  