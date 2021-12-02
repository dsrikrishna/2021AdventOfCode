TEST_INPUT = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

def get_final_position_without_aim(input_list):
  horizontal, depth = 0,0
  for i in input_list:
    direction, mag = i.split(' ')
    if direction =='forward':
      horizontal+=int(mag)
    elif direction == 'down':
      depth+=int(mag)
    elif direction=='up':
      depth-=int(mag)
  
  return horizontal,depth

def get_final_position(input_list):
  horizontal, depth,aim = 0,0,0
  for i in input_list:
    direction, mag = i.split(' ')
    if direction =='forward':
      horizontal+=int(mag)
      depth+=int(mag)*aim
    elif direction == 'down':
      aim+=int(mag)
    elif direction=='up':
      aim-=int(mag)
  return horizontal,depth,aim

h,d,a = get_final_position(TEST_INPUT.split('\n'))


print("Final Position : {0}, Product: {1}".format((h,d),h*d))


with open('input.txt') as fid:
  input_text = fid.readlines()

h,d,a = get_final_position(input_text)


print("Final Position : {0}, Product: {1}".format((h,d),h*d))