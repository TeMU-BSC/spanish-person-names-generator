"""
Given a list of male and female names, creates 10k random names composed of:
name + first name + second name

It expects a folder called 'gazeteers' with three files within it:
- female_names.txt
- male_names.txt
- surnames.txt
Author: ona.degibert@bsc.es
"""
import random
import os
from collections import Counter

def load_gazetteers():
    # Open files
    path = 'gazetteers'
    gazetteers = dict()
    for filename in os.listdir(path):
        with open(os.path.join(path, filename), 'r') as fn: # open in readonly mode
            gazetteers_list = fn.read().splitlines()
            gazetteers[filename.replace('.txt','')] = gazetteers_list
    return gazetteers

def create_names(gazetteers):
    random_names = []
    all_names = gazetteers['female_names']+gazetteers['male_names']
    surnames_counts = [(surname,0) for surname in gazetteers['surnames']]
    count = 0
    for name in all_names:
        surnames = []
        for each_surname in range(2): # we need to generate two surnames
            # get all counts
            counts = [surname_tuple[1] for surname_tuple in surnames_counts if surname_tuple[1] == count]
            # check if there's still some available, otherwise, increase count
            if count not in counts:
                count += 1
            # select only surnames with the correspondent count
            available_surnames = [surname_tuple[0] for surname_tuple in surnames_counts if surname_tuple[1] == count]
            # choose one randomly and increase count
            name_surname = random.choice(available_surnames)
            index = surnames_counts.index((name_surname,count))
            surnames_counts[index] = (name_surname,count+1)
            surnames.append(name_surname)
        random_name = ' '.join([name] + surnames)
        random_names.append(random_name)
    return random_names

def print_stats(names):
    names_len = [len(name.split()) for name in names]
    counts = Counter(names_len)
    total = sum(counts.values())
    print('\t'.join(['LEN','COUNT','%']))
    for each_len in sorted(counts):
        print('\t'.join([str(each_len),str(counts[each_len]),str(counts[each_len]*100/total)]))

def write_files(list):
    with open('10k_random_names.txt', 'w') as fn: 
        for line in list:
            fn.write(line+'\n')

def main():
    gazetteers = load_gazetteers()
    random_names = create_names(gazetteers)
    print_stats(random_names)
    write_files(random_names)
    
if __name__ == "__main__":
        main()