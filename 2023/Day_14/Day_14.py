filename = 'Input/Day_14_example.txt'
# filename = 'Input/Day_14_input.txt'
f = open(filename,'r')
input = f.read()
input = input.split('\n')

def move_up(grid):
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'O':
                # Move 'O' upwards until it hits a '#'
                for k in range(i - 1, -1, -1):
                    if grid[k][j] == '#':
                        break
                    elif grid[k][j] == '.':
                        grid[k][j], grid[k + 1][j] = 'O', '.'  # Move 'O' up
                    elif grid[k][j] == 'O':
                        break  # Stop if another 'O' is encountered above

    return grid

def sum_positions(grid):
    total_sum = 0

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 'O':
                total_sum += i+1  # Add row index (+1) to total sum

    return total_sum

def rotate_clockwise_90(grid):
    rows = len(grid)
    cols = len(grid[0])

    rotated = [['' for _ in range(rows)] for _ in range(cols)]  # Create a new grid for rotated values

    for i in range(rows):
        for j in range(cols):
            rotated[j][rows - 1 - i] = grid[i][j]  # Rotate clockwise

    return rotated

# Convert data to a list of lists (grid)
grid = [list(row) for row in input]

for j in range(0,3):
    for i in range(0,4):
        # Move 'O's upwards in the grid
        grid = move_up(grid)
        # Rotate the grid by 90 degrees clockwise
        grid = rotate_clockwise_90(grid)


# reverse so row can be indexed from the bottom
grid.reverse()

# Calculate the sum of positions of 'O's after movement
total_sum = sum_positions(grid)

print(total_sum)