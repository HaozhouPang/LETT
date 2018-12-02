from __future__ import division
import pickle
import spacy
def main():
	# weight for the semantic feature
	nlp = spacy.load('en')
	weight_pos = 1

	with open("new_obama.txt", 'r') as f:
		lines = f.readlines()[0]
		corpus_sent = lines.split(".")

	with open('linenum_entity.pkl' , 'rb') as f:
		line_to_entity = pickle.load(f)

	with open('time_sentence.txt', 'r') as f:
		lines = f.readlines()
		line_to_time = {}
		for line in lines:
			try:
				key, value = line.rstrip().split(':')
			except:
				key = line.rstrip().split(':')[0]
				value = line.rstrip().split(':')[1:]
			line_to_time[int(key)] = value


	pairs = {}

	for i in range(len(corpus_sent)):
		
		if i % 1000 == 0:
			print "step ", i
		
		try:
			entities = line_to_entity[i]
			time = line_to_time[i]
		except:
			continue
		sent = unicode(corpus_sent[i], 'utf-8')
		doc = nlp(sent)
		sub_toks = [tok for tok in doc if (tok.dep_ == "nsubj")]

		# convert token to str
		temp = []
		for i in sub_toks:
			temp.append(str(i))

		subject = unicode("".join(temp), 'utf-8')

		if subject in entities:
			if subject not in pairs:
				pairs[subject] = {}
				pairs[subject][time] = weight_pos
			else:
				try:
					if time not in pairs[subject]:
						pairs[subject][time] = weight_pos
					else:
						pairs[subject][time] += weight_pos
				except:
					print "SHIT HAPPENED"
					continue

	with open('pair_pos_score.pkl', 'wb') as f:
		pickle.dump(pairs, f, pickle.HIGHEST_PROTOCOL)

def printpairs():
	pairs = {}
	with open('pair_pos_score.pkl', 'r') as f:
		pairs = pickle.load(f)

	for k in pairs:
		for t in pairs[k]:
			if pairs[k][t] >= 3:
				print(k, t, pairs[k][t])




if __name__ == '__main__':
    main()
    #printpairs()


