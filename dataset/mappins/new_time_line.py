import os
import json
import codecs
import pickle
import nltk
from sutime import SUTime

if __name__ == '__main__':

	fout = open("new_time_sentence.txt", "w")

	with codecs.open("new_obama.txt","r", encoding="utf-8") as f:
		text = f.readlines()[0]
		lines = nltk.sent_tokenize(text)

	sentences = lines

	jar_files = os.path.join(os.path.dirname(__file__), 'jars')
	sutime = SUTime(jars=jar_files, mark_time_ranges=True)
	#result = json.dumps(sutime.parse(test_case), sort_keys=True, indent=4)
	result = []
	for i in range(len(sentences)):
		sen = sentences[i]	
		r = sutime.parse(sen)
		if r != []:
			for ri in r:
				ri["linenum"] = i
				result.append(ri)
	
	with open('time_obama_store'+ '.pkl', 'w') as fi:
		pickle.dump(result, fi, pickle.HIGHEST_PROTOCOL)
	
	'''
	result = []
	with open('time_obama_store.pkl','r') as f:
		result = pickle.load(f)
	'''
	write_to_file = []
	for r in result:
		w = str(r["linenum"]) + ': ' + r["text"]
		write_to_file.append(w)
	fout.write('\n'.join(write_to_file))
	fout.close()

