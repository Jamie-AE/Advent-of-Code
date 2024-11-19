# importing the required modules
import re
import numpy as np
import pandas as pd

# filename = 'Input/Day_10_example.txt'
filename = 'Input/Day_10_input.txt'
f = open(filename,'r')
input = f.readlines()

input = [i.replace('7','X') for i in input]

processed = [re.findall(r'\S', i) for i in input]
processed1 = [re.findall(r'\S', i) for i in input]
processed2 = [re.findall(r'\S', i) for i in input]
processed3 = [re.findall(r'\S', i) for i in input]
processed4 = [re.findall(r'\S', i) for i in input]

N_map = dict(zip(['|', '-', 'L', 'J', 'X', 'F', 'S'],[[0,-1,1],[0,0,0],[0,0,0],[0,0,0],[-1,0,4],[1,0,2],[0,-1,1]]))
E_map = dict(zip(['|', '-', 'L', 'J', 'X', 'F', 'S'],[[0,0,0],[1,0,2],[0,0,0],[0,-1,1],[0,1,3],[0,0,0],[1,0,2]]))
S_map = dict(zip(['|', '-', 'L', 'J', 'X', 'F', 'S'],[[0,1,3],[0,0,0],[1,0,2],[-1,0,4],[0,0,0],[0,0,0],[0,1,3]]))
W_map = dict(zip(['|', '-', 'L', 'J', 'X', 'F', 'S'],[[0,0,0],[-1,0,4],[0,-1,1],[0,0,0],[0,0,0],[0,1,3],[-1,0,4]]))

i = [item for innerlist in processed for item in innerlist].index('S')%len(processed)
j = [item for innerlist in processed for item in innerlist].index('S')//len(processed)

x_enclosed = np.empty((len([item for innerlist in processed for item in innerlist])//len(processed), len(processed)))
y_enclosed = np.empty((len([item for innerlist in processed for item in innerlist])//len(processed), len(processed)))
x_enclosed[:] = np.nan
y_enclosed[:] = np.nan
x_enclosed = pd.DataFrame(x_enclosed)
y_enclosed = pd.DataFrame(y_enclosed)

steps = 0
coord = [i,j,1]

a = 1
while a == 1:
    if processed1[coord[1]][coord[0]] == 0:
        a = 0
    elif coord[2] == 0 or processed[coord[1]][coord[0]] == '.' or  coord[0] < 0 or coord[1] < 0:
        processed1 = np.empty((len([item for innerlist in processed for item in innerlist])//len(processed), len(processed)))
        processed1[:] = np.nan
        a = 0
    elif coord[2] == 1:
        processed1[coord[1]][coord[0]] = steps
        steps += 1
        direction = N_map[processed[coord[1]][coord[0]]][2]
        coord = [sum(x) for x in zip(coord, N_map[processed[coord[1]][coord[0]]])]
        coord[2] = direction
    elif coord[2] == 2:
        processed1[coord[1]][coord[0]] = steps
        steps += 1
        direction = E_map[processed[coord[1]][coord[0]]][2]
        coord = [sum(x) for x in zip(coord, E_map[processed[coord[1]][coord[0]]])]
        coord[2] = direction
    elif coord[2] == 3:
        processed1[coord[1]][coord[0]] = steps
        steps += 1
        direction = S_map[processed[coord[1]][coord[0]]][2]
        coord = [sum(x) for x in zip(coord, S_map[processed[coord[1]][coord[0]]])]
        coord[2] = direction
    elif coord[2] == 4:
        processed1[coord[1]][coord[0]] = steps
        steps += 1
        direction = W_map[processed[coord[1]][coord[0]]][2]
        coord = [sum(x) for x in zip(coord, W_map[processed[coord[1]][coord[0]]])]
        coord[2] = direction

steps = 0
coord = [i,j,2]

a = 1
while a == 1:
    if processed2[coord[1]][coord[0]] == 0:
        a = 0
    elif coord[2] == 0 or processed[coord[1]][coord[0]] == '.' or  coord[0] < 0 or coord[1] < 0:
        processed2 = np.empty((len([item for innerlist in processed for item in innerlist])//len(processed), len(processed)))
        processed2[:] = np.nan
        a = 0
    elif coord[2] == 1:
        processed2[coord[1]][coord[0]] = steps
        steps += 1
        direction = N_map[processed[coord[1]][coord[0]]][2]
        coord = [sum(x) for x in zip(coord, N_map[processed[coord[1]][coord[0]]])]
        coord[2] = direction
    elif coord[2] == 2:
        processed2[coord[1]][coord[0]] = steps
        steps += 1
        direction = E_map[processed[coord[1]][coord[0]]][2]
        coord = [sum(x) for x in zip(coord, E_map[processed[coord[1]][coord[0]]])]
        coord[2] = direction
    elif coord[2] == 3:
        processed2[coord[1]][coord[0]] = steps
        steps += 1
        direction = S_map[processed[coord[1]][coord[0]]][2]
        coord = [sum(x) for x in zip(coord, S_map[processed[coord[1]][coord[0]]])]
        coord[2] = direction
    elif coord[2] == 4:
        processed2[coord[1]][coord[0]] = steps
        steps += 1
        direction = W_map[processed[coord[1]][coord[0]]][2]
        coord = [sum(x) for x in zip(coord, W_map[processed[coord[1]][coord[0]]])]
        coord[2] = direction

steps = 0
coord = [i,j,3]

a = 1
while a == 1:
    if processed3[coord[1]][coord[0]] == 0:
        a = 0
    elif coord[2] == 0 or processed[coord[1]][coord[0]] == '.' or  coord[0] < 0 or coord[1] < 0:
        processed3 = np.empty((len([item for innerlist in processed for item in innerlist])//len(processed), len(processed)))
        processed3[:] = np.nan
        a = 0
    elif coord[2] == 1:
        processed3[coord[1]][coord[0]] = steps
        steps += 1
        direction = N_map[processed[coord[1]][coord[0]]][2]
        coord = [sum(x) for x in zip(coord, N_map[processed[coord[1]][coord[0]]])]
        coord[2] = direction
    elif coord[2] == 2:
        processed3[coord[1]][coord[0]] = steps
        steps += 1
        direction = E_map[processed[coord[1]][coord[0]]][2]
        coord = [sum(x) for x in zip(coord, E_map[processed[coord[1]][coord[0]]])]
        coord[2] = direction
    elif coord[2] == 3:
        processed3[coord[1]][coord[0]] = steps
        steps += 1
        direction = S_map[processed[coord[1]][coord[0]]][2]
        coord = [sum(x) for x in zip(coord, S_map[processed[coord[1]][coord[0]]])]
        coord[2] = direction
    elif coord[2] == 4:
        processed3[coord[1]][coord[0]] = steps
        steps += 1
        direction = W_map[processed[coord[1]][coord[0]]][2]
        coord = [sum(x) for x in zip(coord, W_map[processed[coord[1]][coord[0]]])]
        coord[2] = direction

steps = 0
coord = [i,j,4]

a = 1
while a == 1:
    if processed4[coord[1]][coord[0]] == 0:
        a = 0
    elif coord[2] == 0 or processed[coord[1]][coord[0]] == '.' or  coord[0] < 0 or coord[1] < 0:
        processed4 = np.empty((len([item for innerlist in processed for item in innerlist])//len(processed), len(processed)))
        processed4[:] = np.nan
        a = 0
    elif coord[2] == 1:
        processed4[coord[1]][coord[0]] = steps
        steps += 1
        direction = N_map[processed[coord[1]][coord[0]]][2]
        coord = [sum(x) for x in zip(coord, N_map[processed[coord[1]][coord[0]]])]
        coord[2] = direction
    elif coord[2] == 2:
        processed4[coord[1]][coord[0]] = steps
        steps += 1
        direction = E_map[processed[coord[1]][coord[0]]][2]
        coord = [sum(x) for x in zip(coord, E_map[processed[coord[1]][coord[0]]])]
        coord[2] = direction
    elif coord[2] == 3:
        processed4[coord[1]][coord[0]] = steps
        steps += 1
        direction = S_map[processed[coord[1]][coord[0]]][2]
        coord = [sum(x) for x in zip(coord, S_map[processed[coord[1]][coord[0]]])]
        coord[2] = direction
    elif coord[2] == 4:
        processed4[coord[1]][coord[0]] = steps
        steps += 1
        direction = W_map[processed[coord[1]][coord[0]]][2]
        coord = [sum(x) for x in zip(coord, W_map[processed[coord[1]][coord[0]]])]
        coord[2] = direction

processed1 = pd.DataFrame(processed1).apply(pd.to_numeric,errors='coerce')
processed2 = pd.DataFrame(processed2).apply(pd.to_numeric,errors='coerce')
processed3 = pd.DataFrame(processed3).apply(pd.to_numeric,errors='coerce')
processed4 = pd.DataFrame(processed4).apply(pd.to_numeric,errors='coerce')

processed = processed1.combine(processed2, np.fmin).combine(processed3, np.fmin).combine(processed4, np.fmin)

print(processed.max().max())

for index, row in processed.iterrows():
    for idx, col in row.items():
        if np.isnan(processed.loc[idx,:index]).ne(np.isnan(processed.loc[idx,:index]).shift()).cumsum().tail(1).values[0] == 3 and np.isnan(processed.loc[idx,index]):
            x_enclosed.loc[idx,index] = 1
        elif processed.loc[idx,:index].count() == 2:
            break

0