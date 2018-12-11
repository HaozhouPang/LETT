import os
import json
import codecs
import pickle
import nltk

if __name__ == '__main__':
	#test_case = u'I need a desk for tomorrow from 2pm to 3pm'

	fout = open("time_test_obama.txt", "a")
	f1 = open("line_pos.txt", "w")

	with codecs.open("new_obama.txt","r", encoding="utf-8") as f:
		text = f.readlines()[0]
		lines = nltk.sent_tokenize(text)

	sentences = lines
	sen_list = []
	for s in sentences:
		if sen_list == []:
			start = 1
			end = start + len(s)-1
		else:
			start = sen_list[-1][1] + 1
			end = start + len(s)
		sen_list.append([start, end])
	st = []
	for sen in sen_list:
		st.append(str(sen[0]) + '\t' + str(sen[1]))

	f1.write('\n'.join(st))
	f1.close()

	#test_case = lines
	#test_case = lines.strip()
	'''
	jar_files = os.path.join(os.path.dirname(__file__), 'jars')
	sutime = SUTime(jars=jar_files, mark_time_ranges=True)
	#result = json.dumps(sutime.parse(test_case), sort_keys=True, indent=4)
	
	result = sutime.parse(test_case)
	with open('time_obama_store'+ '.pkl', 'wb') as fi:
		pickle.dump(result, fi, pickle.HIGHEST_PROTOCOL)
	'''
	write_to_file = []
	result = {}
	with open('time_obama_store.pkl', 'r') as fi:
		result = pickle.load(fi)
		#result = json.dumps(result, sort_keys=True, indent=4)
	#f1.write(result)
	#f1.close() 

	ridx = 0
	idx = 0
	while idx < len(sen_list) and ridx < len(result):
		#print ridx
		sen_start = sen_list[idx][0]
		sen_end = sen_list[idx][1]

		if result[ridx]['start'] > sen_end:
			idx = idx + 1

		if result[ridx]['start'] >= sen_start and result[ridx]['end'] <= sen_end:
			print(result[ridx]['value'])
			write_to_file.append(str(idx) + ": " + result[ridx]['text'].encode('ascii', 'replace'))
			ridx = ridx + 1

	fout.write(write_to_file)
	fout.close()
