# filename = 'Input/Day_13_example.txt'
filename = 'Input/Day_13_input.txt'
f = open(filename,'r')
input = f.read()

row_counts = []
col_counts = []

patterns = input.split('\n\n')

def row_to_int(row):
    # Convert "#" to 1, "." to 0, and represent the row as an integer
    return int(row.replace('#', '1').replace('.', '0'), 2)

for m,pattern in enumerate(patterns):
    pattern = pattern.split('\n')
    transposed_pattern = [''.join(row[i] for row in pattern) for i in range(len(pattern[0]))]

    int_rows = [row_to_int(row) for row in pattern]
    transposed_int_rows = [row_to_int(row) for row in transposed_pattern]
    int_rows_reversed = int_rows[:]
    transposed_int_rows_reversed = transposed_int_rows[:]
    int_rows_reversed.reverse()
    transposed_int_rows_reversed.reverse()

    for i in range(1,len(int_rows)):
        # Compare rows using bitwise operations
        if int_rows[:i][-min(len(int_rows[:i]),len(int_rows_reversed[:-i])):] == int_rows_reversed[:-i][-min(len(int_rows[:i]),len(int_rows_reversed[:-i])):]:
            row_counts.append(i)

    for i in range(1,len(transposed_int_rows)):
        # Compare rows using bitwise operations
        if transposed_int_rows[:i][-min(len(int_rows[:i]),len(transposed_int_rows_reversed[:-i])):] == transposed_int_rows_reversed[:-i][-min(len(transposed_int_rows[:i]),len(transposed_int_rows_reversed[:-i])):]:
            col_counts.append(i)


print(sum(row_counts)*100 + sum(col_counts))