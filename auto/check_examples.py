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
                # check if generated explanation example contains variable names
                for j in range(10, 14, 1):
                    contains_var(line[j])

                # check if NL explanation contains period at the end
                high_expl = line[-2]
                high_expl_tokens = high_expl.split(' ')
                if high_expl_tokens[-1] != '.':
                    print('last token is not period in high q expl for line: ', line)

                # TODO: check pointer templates (only contain N, V, Adj, Adv from NL templates)
                # nl_template = line[-7]
                # pointer_template = line[-6]
                # var_list = eval(line[-5])

                # TODO: for nl explanation check "the" in front of N (except for special cases such as Np and "a" Ns and adj + N and ?)
                for i in range(len(high_expl_tokens)):
                    #?


if __name__=='__main__':
    main()