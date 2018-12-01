import pickle

def main():
    # distance to give score
    distance = 3

    weight_distance = 1 # weight for distance
    weight_frequency = 0.1 # weight for frequency

    # pairs of entity and temporal taggings
    pairs = {}

    # load the list of entities with line numbers.
    entities = {}
    with open('entity_linenum.pkl', 'r') as f:
        entities = pickle.load(f)

    # load the list of temporal taggings with line numbers
    lines = [];
    time = {}; # dictionary for sentence and time
    with open('time_sentence.txt', 'r') as f:
        lines = f.readlines();

    for line in lines:
        temp = line.split(':')
        time[temp[0]] = temp[1]

    i = 0
    for keytime in time:
        key_time = int(keytime)
        i += 1
        print(key_time, i)

        for key_entity in entities:
            # the distance from time expression that has weight value
            r = range(max(0, key_time - distance), min(len(entities[key_entity])-1, key_time + distance))

            freq_count = 0 # count the occurances within the distance
            for linesnum in entities[key_entity]:
                if linesnum > (key_time + distance): # pruning
                    break
                if linesnum in r:
                    freq_count += 1
                    # counstruct the result dictionary
                    if key_entity not in pairs:
                        pairs[key_entity] = {};
                        pairs[key_entity][time[keytime]] = weight_distance/(abs(linesnum-key_time)+1)
                    else:
                        if key_time not in pairs[key_entity]:
                            pairs[key_entity][time[keytime]] = weight_distance/(abs(linesnum-key_time)+1)
                        else: # add the score of distance to the pair
                            pairs[key_entity][time[keytime]] += weight_distance/(abs(linesnum-key_time)+1)

            if freq_count != 0:
                # add the score of frequency to the pair
                pairs[key_entity][time[keytime]] += weight_frequency * freq_count

    print(pairs)
    with open('pair_result.pkl', 'wb') as f:
        pickle.dump(pairs, f, pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
    main()
