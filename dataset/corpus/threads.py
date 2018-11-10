from multiprocessing import Pool
import mmap

def work(cfile):
	print("%s"%cfile)
	
	fin = open('kb-output.ttl',"r")
	inp = fin.readlines()
	fin.close()
	kb = [x.strip() for x in inp]


	with open(cfile) as f:
		content = f.readlines()
	content = [x.strip() for x in content]

	items = []
	for line in content:
		a = line.split()[0]
		for x in kb:
			if x in a:
				items.append(a)

	return '\n '.join(items)
		


def main():
	nums = 100 # total tasks
	tasks = []
	output = 'corpus-output.ttl'
	fout = open(output, "w+")

	for i in range(nums):
		tasks.append("corpus%d.ttl"%i)

	pool = Pool(4)
	results = pool.map_async(work, tasks)
	#print(results.get())
	fout.write('\n\n\n\n'.join(results.get()))
	fout.close()
	pool.close()
	pool.join()

if __name__ == '__main__':
	main()