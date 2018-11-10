from multiprocessing import Pool
import mmap

def work(kbfile):
	print("%s"%kbfile)

	with open(kbfile) as f:
		content = f.readlines()
	content = [x.strip() for x in content]

	items = []
	for line in content:
		if 'date' in line and line not in items:
			items.append(line)
		if 'year' in line and line not in items:
			items.append(line)
		if 'Date' in line and line not in items:
			items.append(line)
		if 'Year' in line and line not in items:
			items.append(line)

	return '\n '.join(items)
		


def main():
	nums = 33 # total tasks
	tasks = []
	output = 'kb-output.ttl'
	fout = open(output, "w+")

	for i in range(nums):
		tasks.append("kb%d.ttl"%i)

	pool = Pool(8)
	results = pool.map_async(work, tasks)
	print(results.get())
	fout.write('\n\n\n\n'.join(results.get()))
	fout.close()
	pool.close()
	pool.join()

if __name__ == '__main__':
	main()