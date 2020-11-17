
from templates import *

data_type = "train" 

template_list_train = [
        ("lexical_overlap", "ln_preposition", "neutral", lex_prep_templates), 
        ("lexical_overlap", "ln_relative_clause", "neutral", lex_rc_templates), 
        ("lexical_overlap", "ln_passive", "contradiction", lex_pass_templates), 
        ("lexical_overlap", "ln_conjunction", "contradiction", lex_conj_templates), 
        ("lexical_overlap", "le_around_prepositional_phrase", "entailment", lex_cross_pp_ent_templates), 
        ("lexical_overlap", "le_around_relative_clause", "entailment",lex_cross_rc_ent_templates), 
        ("lexical_overlap", "le_conjunction", "entailment",lex_ent_conj_templates), 
        ("lexical_overlap", "le_passive", "entailment",lex_ent_pass_templates), 
        ("subsequence", "sn_PP_on_subject", "neutral",subseq_pp_on_subj_templates), 
        ("subsequence", "sn_relative_clause_on_subject", "contradiction",subseq_rel_on_subj_templates), 
        ("subsequence", "sn_past_participle", "neutral",subseq_past_participle_templates), 
        ("subsequence", "sn_NP/Z", "neutral",subseq_npz_templates), 
        ("subsequence", "se_adjective", "entailment", subseq_adj_templates), 
        ("subsequence", "se_understood_object", "entailment",subseq_understood_templates), 
        ("subsequence", "se_relative_clause_on_obj", "entailment",subseq_rel_on_obj_templates), 
        ("subsequence", "se_PP_on_obj", "entailment",subseq_pp_on_obj_templates),  
        ("constituent", "cn_after_if_clause", "neutral",const_outside_if_templates),
        ("constituent", "cn_embedded_under_verb", "neutral",const_quot_templates), 
        ("constituent", "cn_disjunction", "neutral",const_disj_templates), 
        ("constituent", "cn_adverb", "neutral",const_advs_nonent_templates), 
        ("constituent", "ce_after_since_clause", "entailment",const_adv_outside_templates),
        ("constituent", "ce_embedded_under_verb", "entailment",const_quot_ent_templates), 
        ("constituent", "ce_conjunction", "entailment",const_conj_templates), 
        ("constituent", "ce_adverb", "entailment",const_advs_ent_templates)
        ]

template_list_dev = [
        ("lexical_overlap", "ln_subject/object_swap", "contradiction", lex_simple_templates), 
        ("lexical_overlap", "le_relative_clause", "entailment", lex_rc_ent_templates), 
        ("subsequence", "sn_NP/S", "neutral",subseq_nps_templates), 
        ("subsequence", "se_conjunction", "entailment",subseq_conj_templates),  
        ("constituent", "cn_embedded_under_if", "neutral",const_under_if_templates), 
        ("constituent", "ce_embedded_under_since", "entailment",const_adv_embed_templates)
        ]

if data_type == "dev":
    template_list = template_list_dev
elif data_type == "train":
    template_list = template_list_train

def no_the(sentence):
    return sentence.replace("the ", "")

lemma = {}
lemma["professors"] = "professor"
lemma["students"] = "student"
lemma["presidents"] = "president"
lemma["judges"] = "judge"
lemma["senators"] = "senator"
lemma["secretaries"] = "secretary"
lemma["doctors"] = "doctor"
lemma["lawyers"] = "lawyer"
lemma["scientists"] = "scientist"
lemma["bankers"] = "banker"
lemma["tourists"] = "tourist"
lemma["managers"] = "manager"
lemma["artists"] = "artist"
lemma["authors"] = "author"
lemma["actors"] = "actor"
lemma["athletes"] = "athlete"

def repeaters(sentence):
    condensed = no_the(sentence)
    words = []
    
    for word in condensed.split():
        if word in lemma:
            words.append(lemma[word])
        else:
            words.append(word)

    if len(list(set(words))) == len(words):
        return False
    else:
        return True

fo = open("rosa_heuristics_train_set_more_nouns_24T_2400.txt", "w")
#fo.write("heuristic\tsubcase\ttemplate\tlabel\tpremise\thypothesis\tpremise_parse\thypothesis_parse\tpremise_binary_parse\thypothesis_binary_parse\n")
fo.write("gold_label\tsentence1_binary_parse\tsentence2_binary_parse\tsentence1_parse\tsentence2_parse\tsentence1\tsentence2\tpairID\theuristic\tsubcase\ttemplate\tlow_q_expl\thigh_q_expl\n")

example_counter = 0

for template_tuple in template_list:
    heuristic = template_tuple[0]
    category = template_tuple[1]
    label = template_tuple[2]
    template = template_tuple[3]

    example_dict = {}
    count_examples = 0

    while count_examples < 100:
        example = template_filler(template)

        example_sents = tuple(example[:2])

        low_q_expl = example[-2]
        high_q_expl = example[-1]

        if example_sents not in example_dict and not repeaters(example[0]):
            example_dict[example_sents] = 1
            pairID = "ex" + str(example_counter)
            fo.write(label + "\t" + example[5] + "\t" + example[6] + "\t" + example[3] + "\t" + example[4] + "\t" + example[0] + \
                     "\t" + example[1] + "\t" + pairID + "\t" + heuristic + "\t" + category + "\t" + example[2] + "\t" + low_q_expl + "\t" + high_q_expl + "\n")
            #fo.write(heuristic + "\t" + category + "\t" + example[2] + "\t" + label + "\t" + example[0] + "\t" + example[1] + "\t" + example[3] + "\t" + example[4] + "\t" + example[5] + "\t" + example[6] + "\n")
            count_examples += 1
            example_counter += 1
            





