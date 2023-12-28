# importing the required modules
import re
import numpy as np

# filename = 'Input/Day_6_example.txt'
filename = 'Input/Day_6_input.txt'
f = open(filename,'r')
input = f.readlines()

ways_to_win = []

race_times = [int(i) for i in re.findall(r'(\d+)', input[0])]
record_distances = [int(i) for i in re.findall(r'(\d+)', input[1])]

for i,race_time in enumerate(race_times):
    wait_times = np.arange(race_time + 1)
    distances = wait_times * (race_time - wait_times)
    ways_to_win.append(np.count_nonzero(distances > record_distances[i]))

print(np.prod(ways_to_win))

race_time = int(''.join(re.findall(r'(\d+)', input[0])))
record_distance = int(''.join(re.findall(r'(\d+)', input[1])))

wait_times = np.arange(race_time + 1, dtype='int64')
distances = wait_times * (race_time - wait_times)
ways_to_win = np.count_nonzero(distances > record_distance)

print(np.prod(ways_to_win))