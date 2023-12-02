# importing the required modules
import tkinter as tk
from tkinter.filedialog import *
import csv
import re

root1 = tk.Tk()
root1.withdraw() # don't need the full GUI
filename = askopenfilename(title='Please select input txt file', filetypes=[("txt", ".txt")]) # show an "Open" dialog box and return the path to the selected file
if filename == "":
    raise SystemExit("No txt file chosen")
root1.destroy()

calibration_values_a = []
calibration_values_b = []

num = ['0','1','2','3','4','5','6','7','8','9']
spelled = ['zero','one','two','three','four','five','six','seven','eight','nine']
spelled_backwards = [i[::-1] for i in spelled]

map_dict = dict(zip(spelled,num))
map_dict_rev = dict(zip(spelled_backwards[::-1],num[::-1]))

with open(filename,'r') as csvfile:
    lines = csv.reader(csvfile, delimiter='\t')
    for row in lines:
        row_subs = re.compile("|".join(map_dict.keys())).sub(lambda ele: map_dict[re.escape(ele.group(0))], row[0])
        row_rev_subs = re.compile("|".join(map_dict_rev.keys())).sub(lambda ele: map_dict_rev[re.escape(ele.group(0))], row[0][::-1])
        digits_a = re.findall(r'\d+', row[0])
        digits_rev_a = re.findall(r'\d+', row[0][::-1])
        digits_b = re.findall(r'\d+', row_subs)
        digits_rev_b = re.findall(r'\d+', row_rev_subs)
        calibration_values_a.append(int(digits_a[0][0] + digits_rev_a[0][0]))
        calibration_values_b.append(int(digits_b[0][0] + digits_rev_b[0][0]))

print(sum(calibration_values_a), sum(calibration_values_b))