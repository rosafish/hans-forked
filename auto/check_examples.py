"""
Check generated examples 
"""
import csv 
import random
from variables import *
from generate_single_example import *

def contains_var(sentence):
    for var_name in var_of_string:
        if var_name in sentence:
            print('var %s in sentence %s' % (var_name, sentence))
    for var_name in var_type_subtypes:
        if var_name in sentence:
            print('var %s in sentence %s' % (var_name, sentence))

def get_variable(var):
    variable_name, variable_index, variable_type, variable_subtype, variable_association = parse_variable(var)
    return Variable(variable_name, variable_index, variable_type, variable_subtype, variable_association)

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

                premise = line[-4]
                premise_tokens = premise.split(' ')
                if premise_tokens[-1] != '.':
                    print('last token is not period in premise for line: ', line)

                hypothesis = line[-3]
                hypothesis_tokens = hypothesis.split(' ')
                if hypothesis_tokens[-1] != '.':
                    print('last token is not period in hypothesis for line: ', line)

                # check pointer templates (only contain N, V, Adj, Adv from NL templates)
                nl_template = line[-7]
                nl_template = nl_template[:-1]
                nl_template_tokens = nl_template.split(' ')
                pointer_template = line[-6]
                pointer_template_tokens = pointer_template.split(' ')
                var_list = eval(line[-5])
                constructed_pt_template_list = ['']
                for token in nl_template_tokens:
                    if token in var_list:
                        variable = get_variable(token)
                        if variable.type in ['N', 'V', 'Adj', 'Adv', 'O']:
                            constructed_pt_template_list.append(token)
                    elif token in ['not', 'know']:
                        constructed_pt_template_list.append(token)
                if constructed_pt_template_list != pointer_template_tokens:
                    print('line: ', line)
                    print('current:', pointer_template_tokens)
                    print('should be:', constructed_pt_template_list)
                    print()
                    # break
                

                # for nl explanation check "the" in front of N (except for special cases such as Np and "a" Ns and adj + N and ?)
                for i in range(len(nl_template_tokens)):
                    token = nl_template_tokens[i]
                    # print(token)
                    if token in var_list:
                        variable = get_variable(token)
                        # print(variable.type)
                        if variable.type == 'N' and variable.subtype != 'Np':
                            prev_token = nl_template_tokens[i-1]
                            if prev_token != 'the':
                                print('prev_token: ', prev_token)
                                print('token: ', token)
                                print('missing "the" in front of noun in high q expl for line: ', line)
                                print('')


if __name__=='__main__':
    main()