"""
Reads csv file with templates and fill in 1 generated example for each template
"""
import csv 
import random
from variables import *

import sys
sys.path.append('/data/rosa/my_github/misinformation/code/')
from myTools import write_csv


class Variable:
    def __init__(self, variable_name, variable_index, variable_type, variable_subtype=None, variable_association=None):
        self.name=variable_name # e.g. N1, Np2, etc.
        self.index=variable_index # index for the n-th variable of the same type in the template
        self.type=variable_type # e.g. N, V, etc.
        self.subtype=variable_subtype # e.g. Vi, Vt, Np, Ns etc.
        self.association=variable_association # e.g. N1_BE1 has association N1
        self.check()
    
    def check(self):
        # check Be to have associated nouns
        if self.type=='Be' and self.association==None:
            print('error: variable Be needs to have an associated noun')

    def set_value(self, value):
        self.value=value


class Template:
    def __init__(self, csv_id, heuristic, template, subtemplate_id, label, premise, hypothesis, \
                 high_quality, low_quality, extreme_low_quality, natural_language, var_list):
        self.id=csv_id # id in templates.csv, used for debugging purpose only
        self.heuristic=heuristic 
        self.template=template
        print('template: ', template)
        self.subtemplate_id=subtemplate_id
        print('subtemplate_id: ', subtemplate_id)
        self.label=label
        self.premise=premise
        self.hypothesis=hypothesis
        self.high_quality=high_quality
        self.low_quality=low_quality
        self.extreme_low_quality=extreme_low_quality
        self.natural_language=natural_language
        # print('var_list: ', var_list)
        self.var_list=eval(var_list) 
        # print('self.var_list: ', type(self.var_list))
        self.variable_dict = dict((var_name, self.get_variable(var_name)) for var_name in self.var_list)
        self.sample_words()
        self.generate_examples()

    def get_variable(self, var):
        variable_name, variable_index, variable_type, variable_subtype, variable_association = parse_variable(var)
        return Variable(variable_name, variable_index, variable_type, variable_subtype, variable_association)
        
    def sample_words(self):
        """ sample word for each variable in variable_dict.values(), check for dups for each var type """
        sampled_nouns = set()
        sampled_verbs = set()
        sampled_dict={'N': sampled_nouns, 'V': sampled_verbs}
        
        for variable in self.variable_dict.values():
            value=None
            if variable.type in ['Be', 'O']:
                continue
            if variable.type in ['V', 'N']:
                have_value=False
                while contains_dup(sampled_dict[variable.type], value) or not have_value:
                    if variable.subtype != None:
                        print("subtype")
                        print(variable.name)
                        value = random.sample(var_of_string[variable.subtype],1)[0]
                        have_value = True
                    else:
                        # print("no subtype")
                        # print(variable.name)
                        value = random.sample(var_of_string[variable.type],1)[0]
                        have_value = True
                # print('variable.name: ', variable.name)
                # print('value: ', value)
                sampled_dict[variable.type].add(have_value)
            
            else:
                print("not N, V, Be")
                print(variable.name)
                print(variable.type)
                print(variable.subtype)
                print('variable.name: ', variable.name)
                print('variable.type: ', variable.type)
                value = random.sample(var_of_string[variable.type],1)[0]
            variable.set_value(value)
            # print('variable.name: ', variable.name)
            # print('variable.value: ', variable.value)
        # decide Be after sampling all nouns
        for variable in self.variable_dict.values():
            if variable.type=='Be':
                association = variable.association
                for v in self.variable_dict.values():
                    # print('v.name: ', v.name)
                    # print('association: ', association)
                    if v.name == association:
                        if v.subtype == 'Np':
                            variable.set_value('are')
                        elif v.subtype == 'Ns':
                            variable.set_value('is')
                        else: #N
                            if v.name[-1]=='s':
                                variable.set_value('are')
                            else:
                                variable.set_value('is')
            elif variable.type=="O":
                association = variable.association
                for v in self.variable_dict.values():
                    # print('v.name: ', v.name)
                    # print('association: ', association)
                    if v.name == association:
                        dictionary = var_of_string[v.subtype+'O']
                        O_list = dictionary[v.value]
                        value = random.sample(O_list,1)[0]
                        variable.set_value(value)
                
    def generate_examples(self):
        """ fill word in for the examples and output for p, h, and different expls """
        # premise
        self.example_premise = self.get_one_example(self.premise)
        # hypotheis
        self.example_hypotheis = self.get_one_example(self.hypothesis)
        # high_quality
        self.example_high_quality = self.get_one_example(self.high_quality)
        # low_quality
        self.example_low_quality = self.get_one_example(self.low_quality)
        # extreme_low_quality
        self.example_extreme_low_quality = self.get_one_example(self.extreme_low_quality)
        # natural_language
        self.example_natural_language = self.get_one_example(self.natural_language)

    def get_one_example(self, template):
        has_period = False
        if template[-1] =='.':
            holder = template[:-1]
            has_period = True
        else:
            holder = template
        template_t_list = holder.split()
        example_t_list = [t if t not in self.variable_dict.keys() else self.variable_dict[t].value for t in template_t_list] 
        
        if has_period: example_t_list.append('.')
        return ' '.join(example_t_list)

    def output(self):
        """
        output in a list for the output csv row format
        """
        return [self.id, self.heuristic, self.template, self.subtemplate_id, self.label, self.premise, self.hypothesis, \
                self.high_quality, self.low_quality, self.extreme_low_quality, self.natural_language, self.var_list, \
                self.example_premise, self.example_hypotheis, self.example_high_quality, self.example_low_quality, \
                self.example_extreme_low_quality]
        

def contains_dup(word_set, word):
    """ checks if word has singular/plural form in word_set """
    # print('word_set: ', word_set)
    # print('word: ', word)
    if word in word_set:
        return True
    elif word in Ns:
        if word+"s" in word_set:
            return True
    elif word in Np:
        if word[:-1] in word_set:
            return True
    else:
        return False


def parse_variable(var):
    # print('var: ', var)
    var_name = var
    # association
    var_association = None
    association_var = var.split('_')
    if len(association_var) == 2:
        var_association = association_var[0]
        var = association_var[1]
    elif len(association_var) == 1:
        var = association_var[0]
    else:
        print('error: too many _ in variable name')
    # index
    var_index = var[-1]
    var=var[:-1]
    # type and subtype
    var_type = None
    var_subtype = None
    if var in var_type_subtypes.keys():
        var_type = var
    else:
        var_subtype = var
        for k, v in var_type_subtypes.items(): 
            if var_subtype in v:
                var_type = k
        if var_type==None:
            var_subtype=None
    # print('var_type: ', var_type)
    # print('var_subtype: ', var_subtype)
    return var_name, var_index, var_type, var_subtype, var_association


def read_templates(fi):
    """
    input: 
    fi: file path

    output:
    a list of Template objects 
    """
    templates = []
    with open(fi) as f:
        reader = csv.reader(f)
        for (i, line) in enumerate(reader):
            if i > 0:
                # print(line)
                # print(len(line))
                template = Template(line[0], line[1], line[2], line[3], line[4], line[5], line[6], \
                                    line[7], line[8], line[9], line[10], line[11])
                templates.append(template)
    return templates


def main():
    random.seed(2021)
    fi = './templates.csv'
    fo = './templates_with_example.csv'
    
    # read templates 
    templates = read_templates(fi)

    output_header = ["id", "heuristic", "template", "subtemplate_id", "label", "premise", "hypothesis", \
                     "high_quality", "low_quality", "extreme_low_quality", "natural_language", "var_list", \
                     "example_premise", "example_hypotheis", "example_high_quality", "example_low_quality", \
                     "example_extreme_low_quality"]
    output_rows = [t.output() for t in templates]

    write_csv(fo, output_rows, output_header)


if __name__=="__main__":
    main()