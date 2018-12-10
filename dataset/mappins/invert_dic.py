import pickle
def main():
	with open('entity_linenum.pkl', 'r') as f:
		dic = pickle.load(f)
	invert_dic = {}

	for i in dic:
		for j in dic[i]:
			if j not in invert_dic:
				invert_dic[j] = [i]
			else:
				invert_dic[j].append(i)

	with open('line_entity.pkl', 'wb') as f:
		pickle.dump(invert_dic, f, pickle.HIGHEST_PROTOCOL)

main()