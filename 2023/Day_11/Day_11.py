# importing the required modules
import numpy as np

# filename = 'Input/Day_11_example.txt'
filename = 'Input/Day_11_input.txt'
f = open(filename,'r')
input = f.read().splitlines()

distances = []

# Convert data to a NumPy array
grid = np.array([list(row) for row in input])

# Find rows with only dots
rows_to_duplicate = [i for i, row in enumerate(grid) if np.count_nonzero(row == '.') == len(row)]

# Duplicate rows x times
rows = grid[rows_to_duplicate]
duplicated_rows = np.repeat(rows, 2 - 1, axis=0)

# Insert duplicated rows back into the original grid
new_grid = grid.copy()
for i, row_index in enumerate(rows_to_duplicate):
    new_grid = np.insert(new_grid, row_index + i * (2 - 1) + 1, duplicated_rows[i * (2 - 1) : (i + 1) * (2 - 1)], axis=0)

new_grid_transposed = new_grid.T

# Find rows with only dots
rows_to_duplicate = [i for i, row in enumerate(new_grid_transposed) if np.count_nonzero(row == '.') == len(row)]

# Duplicate rows x times
rows = new_grid_transposed[rows_to_duplicate]
duplicated_rows = np.repeat(rows, 2 - 1, axis=0)

# Insert duplicated rows back into the original grid
new_new_grid_transposed = new_grid_transposed.copy()
for i, row_index in enumerate(rows_to_duplicate):
    new_new_grid_transposed = np.insert(new_new_grid_transposed, row_index + i * (2 - 1) + 1, duplicated_rows[i * (2 - 1) : (i + 1) * (2 - 1)], axis=0)

# Finding indices of '#'
hash_indices = [(i, j) for i, row in enumerate(new_new_grid_transposed) for j, val in enumerate(row) if val == '#']

# Calculate distances between '#'
for i in range(len(hash_indices)):
    for j in range(i + 1, len(hash_indices)):
        x1, y1 = hash_indices[i]
        x2, y2 = hash_indices[j]
        distances.append(abs(x2 - x1) + abs(y2 - y1))
        
print(sum(distances))