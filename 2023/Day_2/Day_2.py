# importing the required modules
import csv
import re
import pandas as pd

num_reds = 12
num_greens = 13
num_blues = 14

processed = []

delimiters = "Game ", " ", ":", ", ", "; "
regex_pattern = '|'.join(map(re.escape, delimiters))

filename = 'Input/Day_2_input.txt'
with open(filename,'r') as csvfile:
    lines = csv.reader(csvfile, delimiter='\t')
    for row in lines:
        processed.append(re.split(regex_pattern,row[0]))

processed = pd.DataFrame(processed)

red_loc = processed == 'red'
green_loc = processed == 'green'
blue_loc = processed == 'blue'

reds = processed[red_loc.shift(periods=-1, axis="columns")].fillna(0)
greens = processed[green_loc.shift(periods=-1, axis="columns")].fillna(0)
blues = processed[blue_loc.shift(periods=-1, axis="columns")].fillna(0)

max_reds = reds.astype(int).max(axis=1)
max_greens = greens.astype(int).max(axis=1)
max_blues = blues.astype(int).max(axis=1)

possible = (max_reds <= num_reds) & (max_greens <= num_greens) & (max_blues <= num_blues)
possible_games = processed[1].astype(int)[possible]

powers = max_reds * max_greens * max_blues

print(sum(possible_games), sum(powers))