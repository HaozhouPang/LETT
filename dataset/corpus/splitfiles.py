num_chunks = 10000
kbfile = 'mappingbased-properties_en.ttl'
corpusfile = 'long-abstracts_en.ttl'

with open(corpusfile) as fin:
	fout = open("corpus0.ttl", "wb")
	for i, line in enumerate(fin):
		fout.write(line)
		if (i+1)%num_chunks == 0:
			fout.close()
			fout = open("corpus%d.ttl"%(i/num_chunks+1), "wb")

	fout.close()