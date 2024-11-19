# importing the required modules
import re
import numpy as np

# filename = 'Input/Day_5_example.txt'
filename = 'Input/Day_5_input.txt'
f = open(filename,'r')
input = f.read()

# Split input data into lines
lines = input.strip().split('\n')

# Extract seeds data
seeds_line = lines[0]
seeds_data = [int(val) for val in seeds_line.split(':')[1].split()]
seeds = np.array(seeds_data)

# def generate_seeds_from_input(seed_input):
#     seeds = []
#     for i in range(0, len(seed_input), 2):
#         start_seed = seed_input[i]
#         seed_range = seed_input[i + 1]
#         seeds.extend(list(range(start_seed, start_seed + seed_range)))
#     return seeds

# seeds = generate_seeds_from_input(seeds_data)

# Extract and process maps
maps_data = "\n".join(lines[1:])  # Combine lines for maps
maps = maps_data.strip().split('\n\n')

# Initialize a dictionary to store the NumPy arrays for each map
map_arrays = {}
map_names = []  # List to store map names

# Process each map
for map_data in maps:
    map_lines = map_data.strip().split('\n')
    map_name = map_lines[0].replace(':', '')  # Extract map name
    map_names.append(map_name)  # Store map name in the list
    values = [[int(val) for val in line.split()] for line in map_lines[1:]]  # Extract numerical values
    map_arrays[map_name] = np.array(values)  # Store values as a NumPy array

# Store maps in dictionaries for efficient lookup
maps = {
    'seed_to_soil': map_arrays['seed-to-soil map'],
    'soil_to_fertilizer': map_arrays['soil-to-fertilizer map'],
    'fertilizer_to_water': map_arrays['fertilizer-to-water map'],
    'water_to_light': map_arrays['water-to-light map'],
    'light_to_temperature': map_arrays['light-to-temperature map'],
    'temperature_to_humidity': map_arrays['temperature-to-humidity map'],
    'humidity_to_location': map_arrays['humidity-to-location map']
}

# Function to perform mapping for a given seed through all maps
def map_seed(seed):
    current_value = seed
    for key in maps:
        current_map = maps[key]
        for mapping in current_map:
            if mapping[1] <= current_value and mapping[1] + mapping[2 ] >= current_value:
                current_value = mapping[0] + current_value - mapping[1]
                break
    return current_value

# Map each seed through all maps
mapped_seeds = [map_seed(seed) for seed in seeds]

print(min(mapped_seeds))