import pickle
import nltk
import codecs

def main():
	with codecs.open('new_obama.txt', 'r', encoding='utf-8') as f:
		text = f.readlines()[0]
		lines = nltk.sent_tokenize(text)

	with open('lines.pkl', 'wb') as f:
		pickle.dump(lines, f, pickle.HIGHEST_PROTOCOL)

	with open('obama_entities.pkl' , 'rb') as f:
		entities = pickle.load(f)

	dic = {}
	for i in entities:
		dic[i] = []

	for i in range(len(lines)):
		l = lines[i]
		for j in entities:
			if j in l:
				dic[j].append(i)

	with open('entity_linenum' + '.pkl', 'wb') as f:
		pickle.dump(dic, f, pickle.HIGHEST_PROTOCOL)

main()