from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
import codecs
import pickle
def get_continuous_chunks(text):
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    prev = None
    continuous_chunk = []
    current_chunk = []
    for i in chunked:
            if type(i) == Tree:
                    current_chunk.append(" ".join([token for token, pos in i.leaves()]))
            elif current_chunk:
                    named_entity = " ".join(current_chunk)
                    if named_entity not in continuous_chunk:
                            continuous_chunk.append(named_entity)
                            current_chunk = []
            else:
                    continue
    return continuous_chunk
 
def main():
    with codecs.open('data.txt', 'r', encoding='utf-8') as f:

        #print(f.readlines()[0][5699:5700])
        #exit()
        my_sent = f.readlines()[0]

        #print(my_sent == "?")
        #print(my_sent)
        #exit()

    with open('obama_entities' + '.pkl', 'wb') as f:
        pickle.dump(get_continuous_chunks(my_sent), f, pickle.HIGHEST_PROTOCOL)
    #print(len(get_continuous_chunks(my_sent)))

main()


