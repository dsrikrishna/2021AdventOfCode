TEST_INPUT = """2199943210
3987894921
9856789892
8767896789
9899965678"""

lines = TEST_INPUT.split("\n")


class Grid:
    def __init__(self, lines) -> None:
        self.grid = []
        for line in lines:
            nums = [int(i) for i in line]
            self.grid.append(nums)
        num_cols = len(self.grid[0])
        num_rows = len(self.grid)
        self.padded_grid = [[9 for i in range(num_cols + 2)]]
        for j in self.grid:
            self.padded_grid.append([9, *j, 9])
        self.padded_grid.append([9 for i in range(num_cols + 2)])
        self.basin_locations=set()
        self.keep_searching_basin = False


    def get_low_points(self):
        self.low_points_heights = []
        self.low_points_locations = []

        num_rows = len(self.padded_grid) - 2
        num_cols = len(self.padded_grid[0]) - 2
        for r in range(1, num_rows + 1):
            for c in range(1, num_cols + 1):
                if (
                    self.padded_grid[r - 1][c] > self.padded_grid[r][c]
                    and self.padded_grid[r][c] < self.padded_grid[r + 1][c]
                    and self.padded_grid[r][c - 1] > self.padded_grid[r][c]
                    and self.padded_grid[r][c] < self.padded_grid[r][c + 1]
                ):
                    self.low_points_locations.append((r, c))

        # print(low_points_locations)
        self.low_points_heights = [
            self.padded_grid[i[0]][i[1]] for i in self.low_points_locations
        ]

    def get_basins(self,location):
        self.keep_searching_basin=False
        current_basin_locations = set(list(self.basin_locations))
        r,c=location
        self.basin_locations.add((r,c))
        if self.padded_grid[r - 1][c] != 9 and self.padded_grid[r - 1][c] > self.padded_grid[r][c]:
            self.basin_locations.add((r - 1, c))
        if self.padded_grid[r + 1][c] != 9 and self.padded_grid[r + 1][c] > self.padded_grid[r][c]:
            self.basin_locations.add((r + 1, c))
        if self.padded_grid[r][c - 1] != 9 and self.padded_grid[r][c - 1] > self.padded_grid[r][c]:
            self.basin_locations.add((r, c - 1))
        if self.padded_grid[r][c + 1] != 9 and self.padded_grid[r][c + 1] > self.padded_grid[r][c]:
            self.basin_locations.add((r, c + 1))
        
        if self.basin_locations - current_basin_locations:
            self.keep_searching_basin=True
        else:
            self.keep_searching_basin=False
        
        if self.keep_searching_basin==True:
            for loc in (self.basin_locations-current_basin_locations):
                self.get_basins(loc)
            else:
                return
    def reset_basin(self):
        self.basin_locations=set()        
def get_product_of_max_three_basins(lines):
    g = Grid(lines)
    g.get_low_points()
    # print(g.low_points_locations)
    basin_location_sizes=[]
    for loc in g.low_points_locations:
        g.get_basins(loc)
        basin_location_sizes.append(len(g.basin_locations))
        g.reset_basin()
      
    top_three = sorted(basin_location_sizes)[-3:]
    return top_three[0]*top_three[1]*top_three[2]

lines =open('./input.txt').read().split('\n')

print(get_product_of_max_three_basins(lines))