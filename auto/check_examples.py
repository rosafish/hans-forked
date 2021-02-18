"""
Check generated examples 
"""
import csv 
import random
from variables import *

def contains_var(sentence):
    for var_name in var_of_string:
        if var_name in sentence:
            print('var %s in sentence %s' % (var_name, sentence))
    for var_name in var_type_subtypes:
        if var_name in sentence:
            print('var %s in sentence %s' % (var_name, sentence))

def main():
    fi = './templates_with_example.csv'

    with open(fi) as f:
        reader = csv.reader(f)
        for (i, line) in enumerate(reader):
            if i > 0:
                for j in range(12, 16, 1):
                    contains_var(line[j])


if __name__=='__main__':
    main()