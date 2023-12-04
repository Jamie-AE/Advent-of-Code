# importing the required modules
import csv
import re

input = []
winning_nums = []
nums = []

points_total = 0

filename = 'Input/Day_4_input.txt'
with open(filename,'r') as csvfile:
    lines = csv.reader(csvfile, delimiter='\t')
    for i, row in enumerate(lines):
        input.append(row[0])
        winning_nums.append(re.findall(r'(\d+)', row[0].split(': ')[1].split(' | ')[0]))
        nums.append(re.findall(r'(\d+)', row[0].split(': ')[1].split(' | ')[1]))
        points_this_game = 0
        j = 0
        for num in nums[i]:
            if num in winning_nums[i]:
                if j == 0:
                    points_this_game = 1
                else:
                    points_this_game = points_this_game * 2
                j+=1
        points_total = points_total + points_this_game

print(points_total)

instances = [1]*len(nums)
for i, card in enumerate(nums):
    count = 0 
    for num in card:
        if num in winning_nums[i]:
            count += 1
    if count > 0:
        for k in range(0,count):
            instances[i+k+1] += instances[i]        

print(sum(instances))