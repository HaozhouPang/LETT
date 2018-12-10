import pickle
def main():
	pair_base = {}
	pair_pos = {}
	pair_sub = {}
	pair_dist = {}

	final_pairs = {}

	with open('pair_baseline_score.pkl', 'r') as f:
		pair_base = pickle.load(f)
	with open('pair_pos_score.pkl', 'r') as f:
		pair_pos = pickle.load(f)
	with open('pair_sub_score.pkl', 'r') as f:
		pair_sub = pickle.load(f)
	with open('pair_dist_score.pkl', 'r') as f:
		pair_dist = pickle.load(f)

	for i in pair_base:
		entity = i
		for time in pair_base[entity]:

			if i not in final_pairs:
				final_pairs[entity] = {}
				final_pairs[entity][time] = pair_base[entity][time]
			else:
				if time not in final_pairs[entity]:
					final_pairs[entity][time] = pair_base[entity][time]
				else:
					final_pairs[entity][time] += pair_base[entity][time]

	for i in pair_pos:
		entity = i
		for time in pair_pos[entity]:
			if i not in final_pairs:
				final_pairs[entity] = {}
				final_pairs[entity][time] = pair_pos[entity][time]
			else:
				if time not in final_pairs[entity]:
					final_pairs[entity][time] = pair_pos[entity][time]
				else:
					final_pairs[entity][time] += pair_pos[entity][time]

	for i in pair_sub:
		entity = i
		for time in pair_sub[entity]:
			if i not in final_pairs:
				final_pairs[entity] = {}
				final_pairs[entity][time] = pair_sub[entity][time]
			else:
				if time not in final_pairs[entity]:
					final_pairs[entity][time] = pair_sub[entity][time]
				else:
					final_pairs[entity][time] += pair_sub[entity][time]

	for i in pair_dist:
		entity = i
		for time in pair_dist[entity]:
			if i not in final_pairs:
				final_pairs[entity] = {}
				final_pairs[entity][time] = pair_dist[entity][time]
			else:
				if time not in final_pairs[entity]:
					final_pairs[entity][time] = pair_dist[entity][time]
				else:
					final_pairs[entity][time] += pair_dist[entity][time]

	for k in final_pairs:
		for t in final_pairs[k]:
			if final_pairs[k][t] >= 130:
				print(k, t, final_pairs[k][t])

main()