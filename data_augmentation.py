import os
from io import open
import random
import glob

#Contains the white and black first and last names
names_folder = './names/docs'
names_files = os.listdir(names_folder)
files = []

#reads in the lines into each file
for file in names_files:
	with open(os.path.join(names_folder, file), 'r') as f:
		files.append(f.readlines())
		
for idx, file in enumerate(files):
	files[idx] = [name.rstrip('\n')	for name in file]

wfn_dict = {name: "" for name in files[0]}
bfn_dict = {name: "" for name in files[1]}
wln_dict = {name: "" for name in files[2]}
bln_dict = {name: "" for name in files[3]}

def swap(name):
	if name in wfn_dict:
		return random.choice(list(bfn_dict.keys()))
	elif name in bfn_dict:
		return random.choice(list(wfn_dict.keys()))
	elif name in wln_dict:
		return random.choice(list(bln_dict.keys()))
	elif name in bln_dict:
		return random.choice(list(wln_dict.keys()))
	else:
		return name
		
def swap_list(name_list):
	return [swap(name) for name in name_list]

#This is where the corpus augmentation starts
def save_list(lines, filename):
	data = '\n'.join(lines)
	file = open(filename, 'w')
	file.write(data)
	file.close()
	
input_dir = './corpus/training_set/'
files = os.listdir(input_dir)
output_dir = './corpus/swapped_training_set'
if not os.path.isdir(output_dir):
	os.makedirs(output_dir)

print('===================================================================================')
for file in files:
	print('\nSwapping names in {file}...'.format(file=file))
	with open(input_dir + file, 'r') as f:
		f = f.read()
		sentences = []
		for line in f.split('\n'):
			sentences.append(line.split())
		swapped_lines = [swap_list(line) for line in sentences]
		total_lines = [' '.join(list) for list in swapped_lines]
	out_file = os.path.join(output_dir, file.split('/')[-1].rstrip('.txt') + '_swapped.txt')
	save_list(total_lines, out_file)
	print('---Successfully swapped names in {file}'.format(file=file))
	print('\n===================================================================================')