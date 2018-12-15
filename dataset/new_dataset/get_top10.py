import heapq
from operator import itemgetter
def main():
	dic = {}
	with open('out','r') as f:
		lines = f.readlines()
	for l in lines:
		try:
			name, time, line_num = l.split("#")
		except:
			continue
		pair = (name, time)
		if pair in dic:
			dic[pair] += 1
		else:
			dic[pair] = 1

	lst = heapq.nlargest(50, dic.items(), key=itemgetter(1))
	for i in lst:
		print str(i) + '\n'



main()