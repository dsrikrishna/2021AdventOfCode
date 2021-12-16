TEST_INPUT = """2199943210
3987894921
9856789892
8767896789
9899965678"""

lines = TEST_INPUT.split('\n')
def get_padded_grid(lines):
    grid = []
    for line in lines:
        nums = [int(i) for i in line]
        grid.append(nums)
    num_cols = len(grid[0])
    num_rows = len(grid)
    
    padded_grid = [[9 for i in range(num_cols + 2)]]
    for j in grid:
        padded_grid.append([9, *j, 9])
    padded_grid.append([9 for i in range(num_cols + 2)])
    return padded_grid

def find_low_points(lines):
    padded_grid = get_padded_grid(lines)
    low_points_heights = []
    low_points_locations = []

    num_rows = len(padded_grid)-2
    num_cols = len(padded_grid[0])-2
    for r in range(1, num_rows+1):
        for c in range(1, num_cols+1):
            if padded_grid[r -1][c] > padded_grid[r][c] and \
            padded_grid[r][c] < padded_grid[r + 1][c] and \
            padded_grid[r][c - 1] > padded_grid[r][c] and \
            padded_grid[r][c] < padded_grid[r][c + 1]:
                low_points_locations.append((r, c))

    # print(low_points_locations)
    low_points_heights = [padded_grid[i[0]][i[1]] for i in low_points_locations]
    return low_points_heights, low_points_locations
low_points_heights, low_points_locations = find_low_points(lines)
print(sum(low_points_heights)+len(low_points_heights))
print(low_points_heights)

# lines = open('input.txt').read().split('\n')
# low_points_heights = find_low_points(lines)
# print(sum(low_points_heights)+len(low_points_heights))

def get_basin_size(location, padded_grid):
    basin_locations=[]
    if len(location)>0:
        r,c = location
    else:
        return 0
    if padded_grid[r-1][c]!=9 and padded_grid[r-1][c]>padded_grid[r][c]:
        basin_locations.append((r-1,c))
    if padded_grid[r+1][c]!=9 and padded_grid[r+1][c]>padded_grid[r][c]:
        basin_locations.append((r+1,c))
    if padded_grid[r][c-1]!=9 and padded_grid[r][c-1]>padded_grid[r][c]:
        basin_locations.append((r,c-1))
    if padded_grid[r][c+1]!=9 and padded_grid[r][c+1]>padded_grid[r][c]:
        basin_locations.append((r,c+1))
    num_locs=len(basin_locations)
    print(location, num_locs)
    for loc in basin_locations:
        num_locs+=get_basin_size(loc,padded_grid)
    return num_locs

padded_grid = get_padded_grid(lines)
for loc in low_points_locations:
    print(loc,get_basin_size(loc,padded_grid))