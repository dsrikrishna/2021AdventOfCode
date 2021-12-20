TEST_INPUT = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""


class Grid:
    def __init__(self, array) -> None:
        self.grid = array
        self.num_rows = len(array)
        self.num_cols = len(array[0])
        self.recursion_count = 0
        self.flashes = 0
        # self.padded_grid = [0*]

    def perform_step(self):
        self.plus_one()
        self.check_and_propagate_flashes()
        self.count_flashes()
        self.check_all_flash()
    def check_all_flash(self):
        flattened_grid = self.flattened_grid()
        if set(flattened_grid)==set([0]):
            return True
        else:
            False
    def count_flashes(self):
        flattened_grid = self.flattened_grid()
        self.flashes+=sum([1 for i in flattened_grid if i==0])
    def flattened_grid(self):
        flattened_grid = []
        for i in range(self.num_rows):
            flattened_grid.extend([j for j in self.grid[i]])
        return flattened_grid
    def check_and_propagate_flashes(self):
        self.recursion_count+=1
        flash_positions = []
        flattened_grid = self.flattened_grid()
        while any([True for j in flattened_grid if j>9]):
            for i in range(self.num_rows):
                for j in range(self.num_cols):
                    if self.grid[i][j]>=10:
                        self.grid[i][j]=0
                        flash_positions.append((i,j))
            for position in flash_positions:
                self.increment_neighbors(position)
            self.check_and_propagate_flashes()
            flattened_grid = self.flattened_grid()
        else:
            return

    def plus_one(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.grid[i][j] += 1

    def increment_neighbors(self, pos):
        i, j = pos
        neighbors = [
            (i - 1, j - 1),
            (i - 1, j),
            (i - 1, j + 1),
            (i, j - 1),
            (i, j + 1),
            (i + 1, j - 1),
            (i + 1, j),
            (i + 1, j + 1),
        ]
        allowed_neighbors = [
            (p, q) for (p, q) in neighbors if 0 <= p <= 9 and 0 <= q <= 9
        ]
        for position in allowed_neighbors:
            p, q = position
            if self.grid[p][q]!=0:
                self.grid[p][q]+=1
                if self.grid[p][q]>9:
                    pass

    def __repr__(self) -> str:
        return '\n'.join([''.join([str(k) for k in l]) for l in self.grid])

lines = TEST_INPUT.split('\n')
grid=[]
for l in lines:
    grid.append([int(i) for i in l])

test_grid = Grid(grid)

# for i in range(195):
#     test_grid.perform_step()
# print(test_grid)
# print(test_grid.flashes)
step_num=0
while not test_grid.check_all_flash():
    test_grid.perform_step()
    step_num+=1
print(step_num)
lines = open('./input.txt').read().split('\n')
grid=[]
for l in lines:
    grid.append([int(i) for i in l])

grid = Grid(grid)
# for i in range(100):
#     grid.perform_step()
# print(grid)
# print(grid.flashes)

step_num=0
while not grid.check_all_flash():
    grid.perform_step()
    step_num+=1
print(step_num)