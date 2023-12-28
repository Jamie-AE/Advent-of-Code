# importing the required modules
import re
from collections import Counter
import numpy as np
import operator

# filename = 'Input/Day_7_example.txt'
filename = 'Input/Day_7_input.txt'
f = open(filename,'r')
input = f.readlines()

hands_processed = []
strengths = []

hands = list(map(lambda x: x.split(' ')[0], input))
bids = list(map(lambda x: int((x.split(' ')[1]).replace(r'\n','')), input))

card = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
# card_strength = [14,13,12,11,10,9,8,7,6,5,4,3,2]
card_strength = [14,13,12,1,10,9,8,7,6,5,4,3,2]
map_dict = dict(zip(card,card_strength))

for hand in hands:
    hands_processed.append([map_dict[k] for k in re.findall(r'[A-Z]|\d', hand)])

for i, hand in enumerate(hands_processed):
    original_hand = hand
    if 1 in hand:
        if Counter(hand).most_common()[0][0] == 1 and not Counter(hand).most_common()[0][1] == 5:
            hand = [Counter(hand).most_common()[1][0] if x==1 else x for x in hand]
        else:
            hand = [Counter(hand).most_common()[0][0] if x==1 else x for x in hand]
    Five_of_a_kind = (sum((num==5) * 1 for num in Counter(hand).values()) == 1) * 1
    Four_of_a_kind = (sum((num==4) * 1 for num in Counter(hand).values()) == 1) * 1
    Full_house = (sum((num==3) * 1 for num in Counter(hand).values()) == 1 and sum((num==2) * 1 for num in Counter(hand).values()) == 1) * 1
    Three_of_a_kind = (sum((num==3) * 1 for num in Counter(hand).values()) == 1) * 1
    Two_pair = (sum((num==2) * 1 for num in Counter(hand).values()) == 2) * 1
    Pair = (sum((num==2) * 1 for num in Counter(hand).values()) == 1) * 1
    strengths.append([Five_of_a_kind,Four_of_a_kind,Full_house,Three_of_a_kind,Two_pair,Pair,original_hand[0],original_hand[1],original_hand[2],original_hand[3],original_hand[4],bids[i]])

results = sorted(strengths, key=operator.itemgetter(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

print(sum([i[-1] for i in results] * np.arange(1,len(strengths)+1)))