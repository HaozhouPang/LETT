from __future__ import division
import pickle
from pycorenlp import StanfordCoreNLP
#import spacy
def main():
	# weight for the semantic feature
	#nlp = spacy.load('en')
	nlp = StanfordCoreNLP('http://localhost:9000')
	weight_sub = 1
	corpus_sent = ()
	with open("lines.pkl", 'rb') as f:
		temp = pickle.load(f)
		for i in temp:
			corpus_sent += (i,)



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

	#print corpus_sent
	#exit()

	for i in range(0, len(corpus_sent)):
		if i % 1000 == 0:
			print "step ", i
		if i % 5000 == 0:
			with open('pair_sub_score.pkl', 'wb') as f:
				pickle.dump(pairs, f, pickle.HIGHEST_PROTOCOL)

		
		try:
			entities = line_to_entity[i]
			time = line_to_time[i]
		except:
			continue
		#sent = unicode(corpus_sent[i], 'utf-8')
		#doc = nlp(sent)
		#sub_toks = [tok for tok in doc if (tok.dep_ == "nsubj")]

		# convert token to str
		#temp = []
		#for i in sub_toks:
		#	temp.append(str(i))

		#subject = unicode("".join(temp), 'utf-8')
		try:
			#print 'TEST'
			output = nlp.annotate(str(corpus_sent[i]), properties={'annotators': 'tokenize,ssplit,pos,depparse,parse','outputFormat': 'json'})
			#print "PASS"
			parsed_sent = output['sentences'][0]['parse']
			start = parsed_sent.find('(NP (')
			end = parsed_sent.find('))\n')

			sub = parsed_sent[start+4:end+1]
			toks = sub.split()
			#print toks
			subject = ""
			for tok in range(len(toks)):
				if tok % 2 == 1:

					subject += toks[tok][0:-1] + " "
			subject = subject[:-1]
		except:
			continue
		#print subject
		if subject in entities:
			if subject not in pairs:
				pairs[subject] = {}
				pairs[subject][time] = weight_sub
			else:
				try:
					if time not in pairs[subject]:
						pairs[subject][time] = weight_sub
					else:
						pairs[subject][time] += weight_sub
				except:
					print "SHIT HAPPENED"
					continue

	with open('pair_sub_score.pkl', 'wb') as f:
		pickle.dump(pairs, f, pickle.HIGHEST_PROTOCOL)

def printpairs():
	pairs = {}
	with open('pair_sub_score.pkl', 'r') as f:
		pairs = pickle.load(f)

	for k in pairs:
		for t in pairs[k]:
			if pairs[k][t] >= 1:
				print(k, t, pairs[k][t])




if __name__ == '__main__':
    main()
    printpairs()




