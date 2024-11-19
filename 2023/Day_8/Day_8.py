# importing the required modules
import re
import numpy as np

# filename = 'Input/Day_8_example.txt'
# filename = 'Input/Day_8_example2.txt'
filename = 'Input/Day_8_input.txt'
f = open(filename,'r')
input = f.readlines()

directions = re.findall(r'[A-Z]', input[0])
mapping = [re.findall(r'[A-Z0-9]+', i) for i in input[2:]]

origins = [i[0] for i in mapping]
L_dests = [i[1] for i in mapping]
R_dests = [i[2] for i in mapping]

L_map = dict(zip(origins,L_dests))
R_map = dict(zip(origins,R_dests))

location = 'AAA'

i = 0
count = 0

while location != 'ZZZ':
    if directions[i] == 'L':
        location = L_map[location]
    elif directions[i] == 'R':
        location = R_map[location]
    if i == len(directions)-1:
        i = 0
    else:
        i+=1
    count+=1

print(count)

locations = [i[0] for i in mapping if i[0][-1]=='A']

i = 0
count = 0

while [i[-1] for i in locations]!=['Z']*len(locations):
    if directions[i] == 'L':
        locations = [L_map[location] for location in locations]
    elif directions[i] == 'R':
        locations = [R_map[location] for location in locations]
    if i == len(directions)-1:
        i = 0
    else:
        i+=1
    count+=1

print(count)