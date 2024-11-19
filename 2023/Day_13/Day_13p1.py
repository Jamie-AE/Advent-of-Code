# filename = 'Input/Day_13_example.txt'
filename = 'Input/Day_13_input.txt'
f = open(filename,'r')
input = f.read()

row_counts = []
col_counts = []

patterns = input.split('\n\n')

for m,pattern in enumerate(patterns):
    pattern = pattern.split('\n')
    transposed_pattern = pattern[:]
    transposed_pattern = list(map(''.join, zip(*transposed_pattern)))

    pattern_reversed = pattern[:]
    transposed_pattern_reversed = transposed_pattern[:]
    pattern_reversed.reverse()
    transposed_pattern_reversed.reverse()

    for i in range(1,len(pattern)):
        # Find indices with only one character difference in substrings
        one_char_diff_indices = []
        for j, (str1, str2) in enumerate(zip(pattern[:i][-min(len(pattern[:i]),len(pattern_reversed[:-i])):], pattern_reversed[:-i][-min(len(pattern[:i]),len(pattern_reversed[:-i])):])):
            diff_count = sum(a != b for a, b in zip(str1, str2))
            if diff_count == 1:
                one_char_diff_indices.append(j)
            elif diff_count > 1:  # Break loop if more than one difference
                one_char_diff_indices = []
                break
        if len(one_char_diff_indices) == 1:
            row_counts.append(i)
            break
        
    for i in range(1,len(transposed_pattern)):
            # Find indices with only one character difference in substrings
            one_char_diff_indices = []
            for j, (str1, str2) in enumerate(zip(transposed_pattern[:i][-min(len(transposed_pattern[:i]),len(transposed_pattern_reversed[:-i])):], transposed_pattern_reversed[:-i][-min(len(transposed_pattern[:i]),len(transposed_pattern_reversed[:-i])):])):
                diff_count = sum(a != b for a, b in zip(str1, str2))
                if diff_count == 1:
                    one_char_diff_indices.append(j)
                elif diff_count > 1:  # Break loop if more than one difference
                    one_char_diff_indices = []
                    break
            if len(one_char_diff_indices) == 1:
                col_counts.append(i)
                break

print(sum(row_counts)*100 + sum(col_counts))