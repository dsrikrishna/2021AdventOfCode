TEST_INPUT = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""
from collections import Counter

def process_input(text):
    lines = text.split('\n')
    x1s, y1s, x2s, y2s = [], [], [], []
    for line in lines:
        split_text = line.split(" -> ")
        x1, y1 = map(int, split_text[0].split(','))
        x2, y2 = map(int, split_text[1].split(','))
        x1s.append(x1)
        x2s.append(x2)
        y1s.append(y1)
        y2s.append(y2)
    return x1s,y1s,x2s,y2s

# print(process_input(TEST_INPUT))

def get_horizontal_vertical_lines(x1s,y1s,x2s,y2s):
  lines = []
  for x1,y1,x2,y2 in zip(x1s,y1s,x2s,y2s):
    if x1==x2 or y1==y2:
      lines.append([(x1,y1),(x2,y2)])
    elif abs(x1-x2)==abs(y1-y2):
      lines.append([(x1,y1),(x2,y2)])
  return lines

def get_all_points_on_lines(lines):
  points=[]
  for line in lines:
    (x1,y1),(x2,y2) = line
    if x1==x2:
      if y1<y2:
        points.extend([(x1,i) for i in range(y1,y2)])
        points.append((x2,y2))
      else:
        points.extend([(x1,i) for i in range(y2,y1)])
        points.append((x1,y1))
    elif y1==y2:
      if x1<x2:
        points.extend([(i,y1) for i in range(x1,x2)])
        points.append((x2,y2))
      else:
        points.extend([(i,y1) for i in range(x2,x1)])
        points.append((x1,y1))
    else:
      # diagonal lines
      if x1>x2 and y1>y2:
        points.extend([(x1-i,y1-i) for i in range(abs(x1-x2))])
        points.append((x2,y2))
      elif x1>x2 and y1<y2:
        points.extend([(x1-i,y1+i) for i in range(abs(x1-x2))])
        points.append((x2,y2))
      elif x1<x2 and y1>y2:
        points.extend([(x1+i,y1-i) for i in range(abs(x1-x2))])
        points.append((x2,y2))
      else:
        points.extend([(x1+i,y1+i) for i in range(abs(x1-x2))])
        points.append((x2,y2))

  return points
lines = get_horizontal_vertical_lines(*process_input(TEST_INPUT))
points = get_all_points_on_lines(lines)
counter = Counter(points)
print(len([i for i in counter if counter[i]>=2]))

# print(process_input(open('input.txt').read()))
lines = get_horizontal_vertical_lines(*process_input(open('input.txt').read()))
points=get_all_points_on_lines(lines)
counter = Counter(points)

print(len([i for i in counter if counter[i]>=2]))
