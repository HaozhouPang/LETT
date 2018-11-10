num_chunks = 1000000
kbfile = 'mappingbased-properties_en.ttl'
corpusfile = 'long-abstrcts_en.ttl'

with open(kbfile) as fin:
	fout = open("kb0.ttl", "wb")
	for i, line in enumerate(fin):
		fout.write(line)
		if (i+1)%num_chunks == 0:
			fout.close()
			fout = open("kb%d.ttl"%(i/num_chunks+1), "wb")

	fout.close()