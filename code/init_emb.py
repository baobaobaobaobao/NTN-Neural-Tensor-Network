import params
import scipy.io as sio
import numpy as np

entities_string='/entities.txt'
relations_string='/relations.txt'
embeds_string='/initEmbed.mat'
training_string='/train.txt'
test_string='/test.txt'
dev_string='/dev.txt'

#input: path of dataset to be used
#output: python list of entities in dataset
def load_entities(data_path=params.data_path):
    words_index,word,entities_index ={},[],[]
    entities_file = open(data_path+entities_string)
    entities_list = entities_file.read().strip().split('\n')
    words_list = [entity.lstrip('__').split('_')[:-1] for entity in entities_list]
    for items in words_list:
    	word = word + items
    word = list(set(word))
    for x in word:
    	words_index[x] = word.index(x)
    for i in words_list:
    	temp = [words_index[j] for j in i]
    	entities_index.append(temp)
    print(entities_index)
    entities_file.close()
    return entities_list
if __name__ == '__main__':
	load_entities()