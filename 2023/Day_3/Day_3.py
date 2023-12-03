# importing the required modules
import csv
import re
import pandas as pd
from string import punctuation

input = []
processed = []
numbers = []

filename = 'Input/Day_3_input.txt'
with open(filename,'r') as csvfile:
    lines = csv.reader(csvfile, delimiter='\t')
    for row in lines:
        input.append(row[0])
        nums = re.findall(r'(\d+)', row[0])
        delimiters = [*punctuation] + [*nums]
        regex_pattern = r'(\|'.join(map(re.escape, delimiters))
        duplicated_numbers = [[i]*len(i) for i in re.findall('(\d+|[\W_])',row[0])]
        processed.append([i for j in duplicated_numbers for i in j])
        numbers.append(nums)

all_numbers = [i for j in numbers for i in j]

processed = pd.DataFrame(processed)
bool_numbers = processed.isin(all_numbers)

bool_symbol = processed.isin([*punctuation.replace('.','')])

bool_location = bool_symbol | bool_symbol.shift(periods=-1, axis="rows") | bool_symbol.shift(periods=1, axis="rows") | bool_symbol.shift(periods=-1, axis="columns") | bool_symbol.shift(periods=1, axis="columns") | bool_symbol.shift(periods=-1, axis="rows").shift(periods=-1, axis="columns") | bool_symbol.shift(periods=-1, axis="rows").shift(periods=1, axis="columns") | bool_symbol.shift(periods=1, axis="rows").shift(periods=-1, axis="columns") | bool_symbol.shift(periods=1, axis="rows").shift(periods=1, axis="columns")
part_numbers = processed[bool_location & ~bool_symbol & bool_numbers].fillna(0).astype(int)
duplicated_partnumber = part_numbers == part_numbers.shift(periods=1, axis="columns")
part_numbers_final = processed[bool_location & ~bool_symbol & bool_numbers].fillna(0).astype(int)[~duplicated_partnumber]

print(int(sum(part_numbers_final.sum())))

gear_ratio_sumation = 0

for i in range(0,processed.shape[0]):
    for j in range(0,processed.shape[1]):
        if processed.loc[i,j] == '*':
            cell = processed.loc[i-1:i+1,j-1:j+1]
            cell = cell[~cell.isin([*punctuation])]
            duplicates = cell == cell.shift(periods=1, axis="columns")
            cell = cell[~duplicates]
            if sum(cell[~cell.isin([*punctuation])].astype(float).count(numeric_only=True)) == 2:
                gear_ratio = cell.astype(float).product().product()
                gear_ratio_sumation+=gear_ratio

print(int(gear_ratio_sumation))