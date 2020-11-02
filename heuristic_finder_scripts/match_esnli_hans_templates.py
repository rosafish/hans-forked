# match input data with HANS templates
import csv
import nltk
import sys
sys.path.append('/data/rosa/my_github/misinformation/code/')
from myTools import write_csv


global nltk2mycode
nltk2mycode = {}
nltk2mycode['CC'] = 'CC'
nltk2mycode['DT'] = 'DT'
nltk2mycode['IN'] = 'P'
nltk2mycode['JJ'] = 'ADJ'
nltk2mycode['JJR'] = 'ADJ'
nltk2mycode['JJS'] = 'ADJ'
nltk2mycode['CD'] = 'ADJ' # numbers for counting etc.
nltk2mycode['PDT'] = 'ADJ' # all/both/half/many/quite/such/this etc.
nltk2mycode['PRP$'] = 'ADJ' # his/its/her/their etc.
# nltk2mycode[':'] = ':'
# nltk2mycode[';'] = ';'
# nltk2mycode[','] = ','
nltk2mycode[':'] = 'IGNORE'
nltk2mycode[';'] = 'IGNORE'
nltk2mycode[','] = 'IGNORE'
nltk2mycode['NN'] = 'N'
nltk2mycode['NNS'] = 'N'
nltk2mycode['NNP'] = 'N'
nltk2mycode['NNPS'] = 'N'
nltk2mycode['PRP'] = 'N' # he/she/him/her etc.
nltk2mycode['VB'] = 'V'
nltk2mycode['VBD'] = 'V'
nltk2mycode['VBG'] = 'V'
nltk2mycode['VBN'] = 'V'
nltk2mycode['VBP'] = 'V'
nltk2mycode['VBZ'] = 'V'
# nltk2mycode['RB'] = 'ADV'
# nltk2mycode['RBR'] = 'ADV'
# nltk2mycode['RBS'] = 'ADV'
nltk2mycode['RB'] = 'IGNORE'
nltk2mycode['RBR'] = 'IGNORE'
nltk2mycode['RBS'] = 'IGNORE'
nltk2mycode['WDT'] = 'RELS' # relative clause
nltk2mycode['WP'] = 'RELS' # relative clause
nltk2mycode['WRB'] = 'RELS' # relative clause
nltk2mycode['TO'] = 'IGNORE' # to
nltk2mycode['RP'] = 'IGNORE' # particle
nltk2mycode['EX'] = 'IGNORE' # there
nltk2mycode['MD'] = 'IGNORE' # can/will/would etc.
nltk2mycode['POS'] = 'IGNORE' # 's
nltk2mycode['.'] = 'IGNORE'
nltk2mycode['('] = 'IGNORE'
nltk2mycode[')'] = 'IGNORE'
nltk2mycode['``'] = 'IGNORE'
nltk2mycode["''"] = "IGNORE"


def get_hans_templates():
    # NOTE: do not include ., because the original snli might not have periods

    # Subsequence: Not entailed
    # [(0,"the"), (1,nouns),(2,nps_verbs), (3,"the"), (4,nouns), (5,"VP"), (6, ".")]
    # [0,1,2,3,4,6]
    subseq_nps_templates = {'name': 'subseq_nps_templates', 
                            'premise': [['DT', 'N', 'V', 'DT', 'N', 'V']], 
                            'hypothesis': [['DT', 'N', 'V', 'DT', 'N']]} 
    # [(0,"the"), (1,nouns), (2,preps), (3,"the"), (4,nouns), (5,"VP"), (6, ".")]
    # [3,4,5,6]
    subseq_pp_on_subj_templates = {'name': 'subseq_pp_on_subj_templates', 
                                   'premise': [['DT', 'N', 'P', 'DT', 'N', 'V']], 
                                   'hypothesis': [['DT', 'N', 'V']]}
    # [(0,"the"), (1,nouns), (2,rels), (3,transitive_verbs), (4,"the"), (5,nouns), (6,"VP"), (7,".")]
    # [4,5,6,7]
    subseq_rel_on_subj_templates = {'name': 'subseq_rel_on_subj_templates',
                                    'premise': [['DT', 'N', 'RELS', 'V', 'DT', 'N', 'V']],
                                    'hypothesis': [['DT', 'N', 'V']]}
    # [(0,"the"), (1,nouns), (2,past_participles), (3,"in"), (4,"the"), (5,location_nouns_b),(6,"VP"),(7,".")],[0,1,2,3,4,5,7]
    # [(0,"the"), (1,nouns), (2,transitive_verbs),(3,"the"),(4,nouns), (5,past_participles), (6,"in"), (7,"the"), (8,location_nouns_b),(9,".")],[3,4,5,6,7,8,9]
    subseq_past_participle_templates = {'name': 'subseq_past_participle_templates',
                                        'premise': [['DT', 'N', 'V', 'P', 'DT', 'N', 'V'], 
                                                    ['DT', 'N', 'V', 'DT', 'N', 'V', 'P', 'DT', 'N']],
                                        'hypothesis': [['DT', 'N', 'V', 'P', 'DT', 'N'], 
                                                       ['DT', 'N', 'V', 'P', 'DT', 'N']]}
    # [(0,conjs), (1,"the"), (2,nouns), (3,npz_verbs), (4,"the"), (5,nouns), (6,"VP"), (7, ".")], [1,2,3,4,5,7]
    # [(0,conjs), (1,"the"), (2,nouns_pl), (3,npz_verbs_plural), (4,"the"), (5,nouns), (6,"VP"), (7, ".")], [1,2,3,4,5,7] 
    # the 2nd one differs from the 1st one only in terms of plurality, which is ignored in our algorithm
    subseq_npz_templates = {'name' : 'subseq_npz_templates',
                            'premise': [['CC', 'DT', 'N', 'V', 'DT', 'N', 'V']], 
                            'hypothesis': [['DT', 'N', 'V', 'DT', 'N']]}

    # Subsequence: Entailed
    # [(0, "the"), (1,nouns), (2,"and"), (3,"the"), (4,nouns), (5,"VP"), (6, ".")], [3,4,5,6]
    # [(0, "the"), (1,nouns),(2, transitive_verbs), (3, "the"), (4, nouns), (5, "and"), (6, "the"), (7, nouns), (8, ".")], [0,1,2,3,4,8]
    subseq_conj_templates = {'name': 'subseq_conj_templates', 
                             'premise': [['DT', 'N', 'CC', 'DT', 'N', 'V'], 
                                         ['DT', 'N', 'V', 'DT', 'N', 'CC', 'DT', 'N']], 
                             'hypothesis': [['DT', 'N', 'V'], 
                                            ['DT', 'N', 'V', 'DT', 'N']]}
    # [(0, adjs), (1,nouns_pl), (2,"VP"), (3, ".")]
    # [1,2,3]
    subseq_adj_templates = {'name': 'subseq_adj_templates', 'premise': [['ADJ', 'N', 'V']], 'hypothesis': [['N', 'V']]}
    # [(0,"the"), (1,nouns), (2,understood_argument_verbs), (3, "the"), (4,"vobj:2"), (5, ".")]
    # [0,1,2,5]
    # vobj:2 is the object and is therefore a noun
    subseq_understood_templates = {'name': 'subseq_understood_templates',
                                   'premise': [['DT', 'N', 'V', 'DT', 'N']],
                                   'hypothesis': [['DT', 'N', 'V', 'N']]}
    # [(0, "the"), (1,nouns), (2,transitive_verbs), (3,"the"), (4,nouns), (5,"RC"), (6,".")]
    # [0,1,2,3,4,6]
    # RC: 
        # 1. rel + " " + verb
        # 2. rel + " the " + arg + " " + verb
        # 3. rel + " " + verb + " the " + arg
    subseq_rel_on_obj_templates = {'name': 'subseq_rel_on_obj_templates',
                                   'premise': [['DT', 'N', 'V', 'DT', 'N', 'RELS', 'V'],
                                               ['DT', 'N', 'V', 'DT', 'N', 'RELS', 'DT', 'N', 'V'],
                                               ['DT', 'N', 'V', 'DT', 'N', 'RELS', 'V', 'DT', 'N']],
                                   'hypothesis': [['DT', 'N', 'V', 'DT', 'N'],
                                                  ['DT', 'N', 'V', 'DT', 'N'],
                                                  ['DT', 'N', 'V', 'DT', 'N']]}
    # [(0, "the"), (1,nouns), (2,transitive_verbs), (3,"the"), (4,nouns), (5,preps), (6,"the"), (7,nouns), (8,".")]
    # [0,1,2,3,4,8]
    subseq_pp_on_obj_templates = {'name': 'subseq_pp_on_obj_templates',
                                  'premise': [['DT', 'N', 'V', 'DT', 'N', 'P', 'DT', 'N']],
                                  'hypothesis': [['DT', 'N', 'V', 'DT', 'N']]}

    debug_templates = {'name': 'debug_templates', 'premise': [['DT', 'N', 'V', 'DT', 'ADJ', 'N', 'P', 'DT', 'N']], 'hypothesis': [['DT', 'N', 'V', 'DT', 'ADJ', 'N']]}

    templates = {}
    templates['ent'] = [subseq_conj_templates, subseq_adj_templates, debug_templates]
    templates['non-ent'] = [subseq_nps_templates, subseq_pp_on_subj_templates, debug_templates]
    return templates


def get_pos_tags(text):
    # nltk pos tags and then convert to my codes for different word types
    token_list = nltk.tokenize.word_tokenize(text)
    nltk_pos_tags =  nltk.pos_tag(token_list)
    
    global nltk2mycode
    # my_pos_tags = []
    # for pair in nltk_pos_tags:
    #     nltk_pt = pair[1]
    #     if nltk_pt in nltk2mycode: 
    #         my_pt = nltk2mycode[nltk_pt]
    #         my_pos_tags.append(my_pt)
    #     else:
    #         print("unknown word type: ", pair)
    my_pos_tags = [nltk2mycode[pair[1]] if pair[1] in nltk2mycode else print("unknown word type: ", pair) for pair in nltk_pos_tags]

    my_pos_tags_filtered = [pt for pt in my_pos_tags if pt!='IGNORE']

    return my_pos_tags_filtered
    

def match_templates(label, p_my_pt, h_my_pt, templates):
    label_templates = templates['ent'] if label == 'entailment' else templates['non-ent'] #TODO: check
    matched_template_name = None

    for template in label_templates:
        p_templates = template['premise']
        h_templates = template['hypothesis']
        assert len(p_templates) == len(h_templates)
        for i in range(len(p_templates)):
            p_template = p_templates[i]
            h_template = h_templates[i]
            if p_template == p_my_pt and h_template == h_my_pt:
                if matched_template_name != None:
                    print('multiple matches!')
                matched_template_name = template['name']

    return matched_template_name


def main():
    hans_found_support_case = './esnli_train_subseq.csv'
    output_file = './esnli_train_subseq_with_templates.csv'
    output_header = None
    output_rows = []

    hans_templates = get_hans_templates()

    with open(hans_found_support_case) as f:
        reader = csv.reader(f)
        for (i, line) in enumerate(reader):
            if i == 0:
                output_header = line
                continue
            label = line[1]
            premise_pos = get_pos_tags(line[2])
            hypothesis_pos = get_pos_tags(line[3])
            template_name = match_templates(label, premise_pos, hypothesis_pos, hans_templates)
            if template_name != None:
                line[-1] = template_name
                print('template_name: ', template_name)
                output_rows.append(line)

    write_csv(output_file, output_rows, output_header)

if __name__=='__main__':
    main()