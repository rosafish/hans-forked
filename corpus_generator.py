
from templates import *
import random

lex_templates_ent = [
        ("lexical_overlap", "le_around_prepositional_phrase", "entailment", lex_cross_pp_ent_templates), 
        ("lexical_overlap", "le_around_relative_clause", "entailment",lex_cross_rc_ent_templates), 
        ("lexical_overlap", "le_conjunction", "entailment",lex_ent_conj_templates), 
        ("lexical_overlap", "le_passive", "entailment",lex_ent_pass_templates),
        ("lexical_overlap", "le_relative_clause", "entailment", lex_rc_ent_templates)
        ]

lex_templates_nonent = [
        ("lexical_overlap", "ln_preposition", "neutral", lex_prep_templates), 
        ("lexical_overlap", "ln_relative_clause", "neutral", lex_rc_templates), 
        ("lexical_overlap", "ln_passive", "contradiction", lex_pass_templates), 
        ("lexical_overlap", "ln_conjunction", "contradiction", lex_conj_templates),
        ("lexical_overlap", "ln_subject/object_swap", "contradiction", lex_simple_templates)
        ]

subseq_templates_ent = [
        ("subsequence", "se_adjective", "entailment", subseq_adj_templates), 
        ("subsequence", "se_understood_object", "entailment",subseq_understood_templates), 
        ("subsequence", "se_relative_clause_on_obj", "entailment",subseq_rel_on_obj_templates), 
        ("subsequence", "se_PP_on_obj", "entailment",subseq_pp_on_obj_templates),
        ("subsequence", "se_conjunction", "entailment",subseq_conj_templates)
        ]

subseq_templates_nonent = [
        ("subsequence", "sn_PP_on_subject", "neutral",subseq_pp_on_subj_templates), 
        ("subsequence", "sn_relative_clause_on_subject", "contradiction",subseq_rel_on_subj_templates), 
        ("subsequence", "sn_past_participle", "neutral",subseq_past_participle_templates), 
        ("subsequence", "sn_NP/Z", "neutral",subseq_npz_templates),
        ("subsequence", "sn_NP/S", "neutral",subseq_nps_templates)
        ]

const_templates_ent = [
        ("constituent", "ce_after_since_clause", "entailment",const_adv_outside_templates),
        ("constituent", "ce_embedded_under_verb", "entailment",const_quot_ent_templates), 
        ("constituent", "ce_conjunction", "entailment",const_conj_templates), 
        ("constituent", "ce_adverb", "entailment",const_advs_ent_templates),
        ("constituent", "ce_embedded_under_since", "entailment",const_adv_embed_templates)
        ]

const_templates_nonent = [
        ("constituent", "cn_after_if_clause", "neutral",const_outside_if_templates),
        ("constituent", "cn_embedded_under_verb", "neutral",const_quot_templates), 
        ("constituent", "cn_disjunction", "neutral",const_disj_templates), 
        ("constituent", "cn_adverb", "neutral",const_advs_nonent_templates),
        ("constituent", "cn_embedded_under_if", "neutral",const_under_if_templates)
        ]

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

nouns_pl = ["professors", "students", "presidents","judges","senators","secretaries","doctors","lawyers","scientists","bankers","tourists","managers","artists","authors","actors","athletes", \
            "designers", "animators", "architects", "administrators", "artisans", "therapists", "bakers", "artists", "officers", \
            "colorists", "curators", "dancers", "directors", "strategists", "essayists", "planners", "stylists", "illustrators", "lyricists", \
            "musicians", "pencillers", "photographers", "photojournalists", "potters", "sculptors", "singers", "writers", \
            "chaplains", "analysts", "counselors", "nurses", "psychiatrists", "psychologists", "psychotherapists", "workers", "engineers", \
            "technologists", "technicians"]


def no_the(sentence):
        return sentence.replace("the ", "")


def repeaters(sentence):
    condensed = no_the(sentence)
    words = []
    
    for word in condensed.split():
        if word in lemma:
            words.append(lemma[word])
        elif word in nouns_pl:
            words.append(word[:-1])
        else:
            words.append(word)

    if len(list(set(words))) == len(words):
        return False
    else:
        return True
            

def generate_samples(output_path, num_sample_per_template, template_list, data_type):
    fo = open(output_path, "w")
    fo.write("gold_label\tsentence1_binary_parse\tsentence2_binary_parse\tsentence1_parse\tsentence2_parse\tsentence1\tsentence2\tpairID\theuristic\tsubcase\ttemplate\tlow_q_expl\thigh_q_expl\tex_low_q_expl\n")

    example_counter = 0

    for template_tuple in template_list:
        heuristic = template_tuple[0]
        
        category = template_tuple[1]

        label = template_tuple[2]
        template = template_tuple[3]

        example_dict = {}
        count_examples = 0

        while count_examples < num_sample_per_template:
            example = template_filler(template, data_type)

            example_sents = tuple(example[:2])

            low_q_expl = example[-3]
            high_q_expl = example[-2]
            ex_low_q_expl = example[-1]

            if example_sents not in example_dict and not repeaters(example[0]):
                example_dict[example_sents] = 1
                pairID = "ex" + str(example_counter)
                fo.write(label + "\t" + example[5] + "\t" + example[6] + "\t" + example[3] + "\t" + example[4] + "\t" + example[0] + \
                        "\t" + example[1] + "\t" + pairID + "\t" + heuristic + "\t" + category + "\t" + example[2] + "\t" + low_q_expl + "\t" + high_q_expl + "\t" + ex_low_q_expl + "\n")
                count_examples += 1
                example_counter += 1


def template_train_test_split():
    train_templates = []
    test_templates = []

    data_list = [
        lex_templates_ent,
        lex_templates_nonent,
        subseq_templates_ent,
        subseq_templates_nonent,
        const_templates_ent,
        const_templates_nonent
    ]

    for data in data_list:
        random.shuffle(data)
        train = data[1:]
        test = [data[0]]
        train_templates.extend(train)
        test_templates.extend(test)
        
    return train_templates, test_templates

def main():
    for i in range(2): #TODO: 30 
        random.seed(i) # setting seed here works for functions imported from templates too

        # randomly sample train and test templates
        template_list_train, template_list_test = template_train_test_split()

        train_output_path = "/data/rosa/hans-forked/randomness_experiment/train_set_24T_600_seed%d.txt" % i
        test_output_path = "/data/rosa/hans-forked/randomness_experiment/test_set_6T_500_seed%d.txt" % i
        generate_samples(train_output_path, 600, template_list_train, "train")
        generate_samples(test_output_path, 500, template_list_test, "test")


if __name__=="__main__":
    main()



