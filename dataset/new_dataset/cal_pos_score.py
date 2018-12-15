from __future__ import division
import pickle
import nltk 
def main():
	# weight for the semantic feature
	weight_pos = 1

	with open("lines.pkl", 'r') as f:
		corpus_sent = pickle.load(f)

	with open('line_entity.pkl' , 'rb') as f:
		line_to_entity = pickle.load(f)

	with open('new_time_sentence.txt', 'r') as f:
		lines = f.readlines()
		line_to_time = {}
		for line in lines:
			try:
				key, value = line.rstrip().split(':')
			except:
				key = line.rstrip().split(':')[0]
				value = " ".join(line.rstrip().split(':')[1:])
				
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

		sent = nltk.word_tokenize(corpus_sent[i])
		pos_tag = nltk.pos_tag(sent)
		key_word = []
		Continue = False
		key_str = ""
		for tag in pos_tag:
			if Continue == False:
				key_str = ""
			if tag[1] == 'NNP':
				key_str += tag[0] + " "
				Continue = True

			if tag[1] != 'NNP':
				Continue = False
				if key_str != "":
					key_word.append(key_str[:-1])

		#print(key_word)
		for subject in key_word:
			if subject in entities:
				try:
					if subject not in pairs:
						pairs[subject] = {}
						pairs[subject][time] = weight_pos
					else:
						
						if time not in pairs[subject]:
							pairs[subject][time] = weight_pos
						else:
							pairs[subject][time] += weight_pos
				except:
					print "line" + str(i) + "SHIT HAPPENED"
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
    printpairs()


