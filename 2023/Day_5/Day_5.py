# importing the required modules
import re
import numpy as np

# filename = 'Input/Day_5_example.txt'
filename = 'Input/Day_5_input.txt'
f = open(filename,'r')
input = f.read()

locations = []

seeds = np.array(re.findall(r'(\d+)', re.search(r'seeds:.*seed-to-soil map:', input, re.DOTALL).group()), dtype=np.int64)
# seeds = np.reshape(np.array(re.findall(r'(\d+)', re.search(r'seeds:.*seed-to-soil map:', input, re.DOTALL).group()), dtype=np.int64), (-1,2))

seed_to_soil_map = np.reshape(np.array(re.findall(r'(\d+)', re.search(r'seed-to-soil map:.*soil-to-fertilizer map:', input, re.DOTALL).group()), dtype=np.int64), (-1,3))
soil_to_fertilizer_map = np.reshape(np.array(re.findall(r'(\d+)', re.search(r'soil-to-fertilizer map:.*fertilizer-to-water map:', input, re.DOTALL).group()), dtype=np.int64), (-1,3))
fertilizer_to_water_map = np.reshape(np.array(re.findall(r'(\d+)', re.search(r'fertilizer-to-water map:.*water-to-light map:', input, re.DOTALL).group()), dtype=np.int64), (-1,3))
water_to_light_map = np.reshape(np.array(re.findall(r'(\d+)', re.search(r'water-to-light map:.*light-to-temperature map:', input, re.DOTALL).group()), dtype=np.int64), (-1,3))
light_to_temperature_map = np.reshape(np.array(re.findall(r'(\d+)', re.search(r'light-to-temperature map:.*temperature-to-humidity map:', input, re.DOTALL).group()), dtype=np.int64), (-1,3))
temperature_to_humidity_map = np.reshape(np.array(re.findall(r'(\d+)', re.search(r'temperature-to-humidity map:.*humidity-to-location map:', input, re.DOTALL).group()), dtype=np.int64), (-1,3))
humidity_to_location_map = np.reshape(np.array(re.findall(r'(\d+)', re.search(r'humidity-to-location map:.*', input, re.DOTALL).group()), dtype=np.int64), (-1,3))

seed_to_soil_map = np.concatenate((np.array(seed_to_soil_map[:,0:2]), seed_to_soil_map[:,0:2] + np.array([seed_to_soil_map[:,2]]*2).T),axis=1)
soil_to_fertilizer_map = np.concatenate((np.array(soil_to_fertilizer_map[:,0:2]), soil_to_fertilizer_map[:,0:2] + np.array([soil_to_fertilizer_map[:,2]]*2).T),axis=1)
fertilizer_to_water_map = np.concatenate((np.array(fertilizer_to_water_map[:,0:2]), fertilizer_to_water_map[:,0:2] + np.array([fertilizer_to_water_map[:,2]]*2).T),axis=1)
water_to_light_map = np.concatenate((np.array(water_to_light_map[:,0:2]), water_to_light_map[:,0:2] + np.array([water_to_light_map[:,2]]*2).T),axis=1)
light_to_temperature_map = np.concatenate((np.array(light_to_temperature_map[:,0:2]), light_to_temperature_map[:,0:2] + np.array([light_to_temperature_map[:,2]]*2).T),axis=1)
temperature_to_humidity_map = np.concatenate((np.array(temperature_to_humidity_map[:,0:2]), temperature_to_humidity_map[:,0:2] + np.array([temperature_to_humidity_map[:,2]]*2).T),axis=1)
humidity_to_location_map = np.concatenate((np.array(humidity_to_location_map[:,0:2]), humidity_to_location_map[:,0:2] + np.array([humidity_to_location_map[:,2]]*2).T),axis=1)

# for seed_range in seeds:
#     for seed in range(seed_range[0],seed_range[0] + seed_range[1]):
for seed in seeds: # remove indent
    for line in seed_to_soil_map:
        soil = seed
        if seed >= line[1] and seed <= line[3]:
            soil = line[0] + seed - line[1]
            break
    for line in soil_to_fertilizer_map:
        fertilizer = soil
        if soil >= line[1] and soil <= line[3]:
            fertilizer = line[0] + soil - line[1]
            break
    for line in fertilizer_to_water_map:
        water = fertilizer
        if fertilizer >= line[1] and fertilizer <= line[3]:
            water = line[0] + fertilizer - line[1]
            break
    for line in water_to_light_map:
        light = water
        if water >= line[1] and water <= line[3]:
            light = line[0] + water - line[1]
            break
    for line in light_to_temperature_map:
        temperature = light
        if light >= line[1] and light <= line[3]:
            temperature = line[0] + light - line[1]
            break
    for line in temperature_to_humidity_map:
        humidity = temperature
        if temperature >= line[1] and temperature <= line[3]:
            humidity = line[0] + temperature - line[1]
            break
    for line in humidity_to_location_map:
        location = humidity
        if humidity >=line[1] and humidity <= line[3]:
            location = line[0] + humidity - line[1]
            break
    locations.append(location)


        # print(soil)
        # print(fertilizer)
        # print(water)
        # print(light)
        # print(temperature)
        # print(humidity)
        # print(location)



print(min(locations))