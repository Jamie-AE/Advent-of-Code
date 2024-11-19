# importing the required modules
# import re
# import numpy as np
# import pandas as pd

filename = 'Input/Day_12_example.txt'
# filename = 'Input/Day_12_input.txt'
f = open(filename,'r')
input = f.read()

lines = input.split('\n')

symbols = []
numbers = []

for line in lines:
    parts = line.split(' ')
    symbols.append(parts[0])
    num_part = ''.join(parts[1:]).replace(',', '')  # Combining digits without commas
    num_list = [int(num) for num in num_part]  # Convert each character to int separately
    numbers.append(num_list)


# Count consecutive "#" for each line in symbols
for line_symbols in symbols:
    grouped_pound_count = [len(group) for group in line_symbols.replace('.', '*').replace('?', '*').split('*')]
    # Exclude empty groups if any
    grouped_pound_count = [count for count in grouped_pound_count if count > 0]
    print("Grouped '#' counts:", grouped_pound_count)