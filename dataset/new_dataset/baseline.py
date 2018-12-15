import pickle
def main():
	with open('entity_linenum.pkl' , 'rb') as f:
		dictionary = pickle.load(f)
		#for i in dictionary:
		#	print(i, dictionary[i])
		#exit()



	with open('new_time_sentence.txt', 'r') as f:
		lines = f.readlines()
		sent_dic = {}
		for line in lines:
			try:
				key, value = line.rstrip().split(':')
			except:
				key = line.rstrip().split(':')[0]
				value = line.rstrip().split(':')[1:]
			sent_dic[int(key)] = value

	
	lst = []
	for j in dictionary:
		for i in dictionary[j]:

			try:
				lst.append((j, str(i), sent_dic[i]))

			except:
				continue
	with open('out', 'w') as f:
		for i in lst:
			try:
				f.write(i[0] + "#" + i[2] + "#" + i[1] + '\n' )
			except:
				continue
main()