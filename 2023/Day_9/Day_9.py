# importing the required modules
import re

# filename = 'Input/Day_9_example.txt'
filename = 'Input/Day_9_input.txt'
f = open(filename,'r')
input = f.readlines()

extrapolated_forward_numbers = []
extrapolated_backwards_numbers = []

# Function to compute the next number in the sequence
def extrapolate_sequence(sequence):
    differences = sequence[:]
    while True:
        next_number = differences[-1] + differences[-2] - differences[-3]
        differences.append(next_number)
        if len(set(differences[-3:])) == 1:
            return differences[-1]

# Process each line of data
for line in input:
    initial_numbers = list(map(int, line.split()))
    all_numbers = [initial_numbers]

    while True:
        numbers = all_numbers[-1]
        differences = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]
        numbers = differences[:]
        all_numbers.append(numbers)
        if differences.count(0) == len(differences):
            break

    for i in range(len(all_numbers)-1):
        all_numbers[-2-i].append(all_numbers[-2-i][-1] + all_numbers[-1-i][-1])
        all_numbers[-2-i].insert(0,all_numbers[-2-i][0] - all_numbers[-1-i][0])

    extrapolated_forward_numbers.append(all_numbers[0][-1])
    extrapolated_backwards_numbers.append(all_numbers[0][0])


print(sum(extrapolated_forward_numbers))
print(sum(extrapolated_backwards_numbers))