import pickle

def main():
	with open('new_obama.txt', 'r') as f:
		line = f.readlines()[0]
		lines = line.split('.')
	with open('obama_entities.pkl' , 'rb') as f:
		entities = pickle.load(f)

	dic = {}
	for i in entities:
		dic[i] = []

	for i in range(len(lines)):
		l = lines[i]
		for j in entities:
			if j.encode('utf-8') in l:
				dic[j].append(i)

	with open('obama_linenum' + '.pkl', 'wb') as f:
		pickle.dump(dic, f, pickle.HIGHEST_PROTOCOL)

main()