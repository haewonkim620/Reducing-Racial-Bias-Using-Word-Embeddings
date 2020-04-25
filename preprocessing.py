import os
import pandas as pd

'''
	The following code is used to strip the corpus 
	of any unwanted symbols
'''

dir = './corpus/training_set/'
bad_chars = ['[', ']', '(', ')', '<', '>', '{', '}', '/', '\'', '"', '=', '-', '.', ',', '|', ';', ':', '*', '+', '&', '#', '%', '?', '$', '_']
files = os.listdir(dir)

print('===================================================================================')
#Opening each file
for file in files:
	lines = []
	path = dir + file
	
	with open(path, 'r') as reader:
		lines = reader.readlines()
		
		#Making the text lowercase
		print('\nMaking {file} lowercase...'.format(file=file))
		#Stripping symbols out of the text
		print('Stripping unwanted symbols from {file}...'.format(file=file))
		for i in range(len(lines)):
			for char in bad_chars:
				lines[i] = lines[i].replace(char, ' ').lower()
		print('---Successfully stripped unwanted symbols from {file}'.format(file=file))
		print('---Successfully made {file} lowercase'.format(file=file))
	
	with open(path, 'w') as writer:
		writer.writelines(lines)
	print('\n===================================================================================')
	
'''
	The following code is used to make all of the
	occupations lowercase
'''
dir = './occupations/'
files = os.listdir(dir)

for file in files:
	with open(dir + file, 'r') as reader:
		lines = reader.readlines()
		lines = [line.lower() for line in lines]
		#lines[-1] = lines[-1] + '\n'
		#lines += [line.rstrip('\n') + 's\n' for line in lines]
		
	with open(dir + file, 'w') as writer:
		writer.writelines(lines)

'''
	The following code is used to remove duplicates
	from the texts of names. This also goes and
	allocates the intersections between the lists of 
	names to one list. This is done by calculating 
	the ratio of the frequency of the given name with 
	the total count of names
'''
dir = './names/spreadsheets/'
files = os.listdir(dir)
for i in range(0, len(files), 2):
	path = dir + files[i]
	df = pd.read_csv(path)
	df = df[['Name', 'Count']]

	wn_freqs = {}
	white_total = 0
	for idx, row in df.iterrows():
		n = row['Name'].lower()
		count = int(row['Count'])
		if n in wn_freqs:
			wn_freqs[n] += count
		else:
			wn_freqs[n] = count
		white_total += count

	excel_file = dir + files[i+1]
	df = pd.read_csv(excel_file)
	df = df[['Name', 'Count']]

	bn_freqs = {}
	black_total = 0
	for idx, row in df.iterrows():
		n = row['Name'].lower()
		count = row['Count']
		if n in bn_freqs:
			bn_freqs[n] += count
		else:
			bn_freqs[n] = count
		black_total += count

	wn_set = set(wn_freqs.keys())
	bn_set = set(bn_freqs.keys())
	intersect = list(wn_set.intersection(bn_set))
	white_names_set = set()
	black_names_set = set()

	for name in intersect:
		white_prop = wn_freqs[name] / white_total
		black_prop = bn_freqs[name] / black_total
		if black_prop >= white_prop:
			black_names_set.add(name)
		else:
			white_names_set.add(name)
			
	wn_set -= black_names_set
	bn_set -= white_names_set
	
	wdelete = [key for key in wn_freqs if key not in wn_set]
	for key in wdelete: del wn_freqs[key]
			
	bdelete = [key for key in bn_freqs if key not in bn_set]
	for key in bdelete: del bn_freqs[key]
			
	wn_list = list(wn_freqs.items())
	bn_list = list(bn_freqs.items())
	
	wn_list.sort(key=lambda tpl: tpl[1])
	bn_list.sort(key=lambda tpl: tpl[1])
	
	diff = abs(len(wn_list) - len(bn_list))
	wn_len = len(wn_list)
	bn_len = len(bn_list)
	l = wn_list if wn_len > bn_len else bn_list
	for j in range(diff):
		l.pop(0)
	if wn_len < bn_len:
		bn_list = l
	else:
		wn_list = l
	
	wn_text = files[i].replace('.csv', '.txt')
	bn_text = files[i+1].replace('.csv', '.txt')
	text_dir = './names/docs/'
	
	with open(text_dir + wn_text, 'w') as w, open(text_dir + bn_text, 'w') as b:
		w.writelines([tpl[0] + '\n' for tpl in wn_list])
		b.writelines([tpl[0] + '\n' for tpl in bn_list])