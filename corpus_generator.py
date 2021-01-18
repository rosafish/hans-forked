
from templates import *
import random

template_properties = {
    "lex_cross_pp_ent_templates": ("lexical_overlap", "le_around_prepositional_phrase", "entailment"),
    "lex_cross_rc_ent_templates": ("lexical_overlap", "le_around_relative_clause", "entailment"), 
    "lex_ent_conj_templates": ("lexical_overlap", "le_conjunction", "entailment"), 
    "lex_ent_pass_templates": ("lexical_overlap", "le_passive", "entailment"),
    "lex_rc_ent_templates": ("lexical_overlap", "le_relative_clause", "entailment"),
    "lex_prep_templates": ("lexical_overlap", "ln_preposition", "neutral"), 
    "lex_rc_templates": ("lexical_overlap", "ln_relative_clause", "neutral"),
    "lex_pass_templates": ("lexical_overlap", "ln_passive", "contradiction"),
    "lex_conj_templates": ("lexical_overlap", "ln_conjunction", "contradiction"),
    "lex_simple_templates": ("lexical_overlap", "ln_subject/object_swap", "contradiction"),
    "subseq_adj_templates": ("subsequence", "se_adjective", "entailment"), 
    "subseq_understood_templates": ("subsequence", "se_understood_object", "entailment"), 
    "subseq_rel_on_obj_templates": ("subsequence", "se_relative_clause_on_obj", "entailment"), 
    "subseq_pp_on_obj_templates": ("subsequence", "se_PP_on_obj", "entailment"),
    "subseq_conj_templates": ("subsequence", "se_conjunction", "entailment"),
    "subseq_pp_on_subj_templates": ("subsequence", "sn_PP_on_subject", "neutral"), 
    "subseq_rel_on_subj_templates": ("subsequence", "sn_relative_clause_on_subject", "contradiction"), 
    "subseq_past_participle_templates": ("subsequence", "sn_past_participle", "neutral"), 
    "subseq_npz_templates": ("subsequence", "sn_NP/Z", "neutral"),
    "subseq_nps_templates": ("subsequence", "sn_NP/S", "neutral"),
    "const_adv_outside_templates": ("constituent", "ce_after_since_clause", "entailment"),
    "const_quot_ent_templates": ("constituent", "ce_embedded_under_verb", "entailment"), 
    "const_conj_templates": ("constituent", "ce_conjunction", "entailment"), 
    "const_advs_ent_templates": ("constituent", "ce_adverb", "entailment"),
    "const_adv_embed_templates": ("constituent", "ce_embedded_under_since", "entailment"),
    "const_outside_if_templates": ("constituent", "cn_after_if_clause", "neutral"),
    "const_quot_templates": ("constituent", "cn_embedded_under_verb", "neutral"), 
    "const_disj_templates": ("constituent", "cn_disjunction", "neutral"), 
    "const_advs_nonent_templates": ("constituent", "cn_adverb", "neutral"),
    "const_under_if_templates": ("constituent", "cn_embedded_under_if", "neutral")  
}

lex_templates_ent = [
        "lex_cross_pp_ent_templates", "lex_cross_rc_ent_templates", "lex_ent_conj_templates", 
        "lex_ent_pass_templates", "lex_rc_ent_templates"
        ]

lex_templates_nonent = [
        "lex_prep_templates", "lex_rc_templates", "lex_pass_templates", 
        "lex_conj_templates", "lex_simple_templates"
        ]

subseq_templates_ent = [
        "subseq_adj_templates", "subseq_understood_templates", "subseq_rel_on_obj_templates", 
        "subseq_pp_on_obj_templates","subseq_conj_templates"
        ]

subseq_templates_nonent = [
        "subseq_pp_on_subj_templates", "subseq_rel_on_subj_templates", "subseq_past_participle_templates", 
        "subseq_npz_templates", "subseq_nps_templates"
        ]

const_templates_ent = [
        "const_adv_outside_templates", "const_quot_ent_templates", "const_conj_templates", 
        "const_advs_ent_templates", "const_adv_embed_templates"
        ]

const_templates_nonent = [
        "const_outside_if_templates", "const_quot_templates", "const_disj_templates", 
        "const_advs_nonent_templates", "const_under_if_templates"
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
            

def generate_samples(output_path, num_sample_per_template, template_list):
    fo = open(output_path, "w")
    fo.write("gold_label\tsentence1_binary_parse\tsentence2_binary_parse\tsentence1_parse\tsentence2_parse\tsentence1\tsentence2\tpairID\theuristic\tsubcase\ttemplate\tlow_q_expl\thigh_q_expl\tex_low_q_expl\n")

    example_counter = 0

    for template in template_list:
        properties = template_properties[template]

        heuristic = properties[0]
        
        category = properties[1]

        label = properties[2]

        example_dict = {}
        count_examples = 0

        while count_examples < num_sample_per_template:
            example = template_filler(template)

            example_sents = tuple(example[:2])

            low_q_expl = example[-3]
            high_q_expl = example[-2]
            ex_low_q_expl = example[-1]

            if example_sents not in example_dict and not repeaters(example[0]):
                example_dict[example_sents] = 1
                pairID = "ex" + str(example_counter)
                fo.write(label + "\t" + example[5] + "\t" + example[6] + "\t" + example[3] + "\t" + example[4] + "\t" + example[0] + \
                        "\t" + example[1] + "\t" + pairID + "\t" + heuristic + "\t" + category + "\t" + example[2] + "\t" + low_q_expl + \
                        "\t" + high_q_expl + "\t" + ex_low_q_expl + "\n")
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

def old_hans_vocab_stats():
    nouns_sg = ["professor", "student", "president","judge","senator","secretary","doctor","lawyer","scientist","banker","tourist","manager","artist","author","actor","athlete"]
    transitive_verbs =  ["recommended", "called", "helped","supported","contacted","believed","avoided","advised","saw","stopped","introduced","mentioned","encouraged","thanked","recognized","admired"]
    intransitive_verbs =  ["slept", "danced", "ran","shouted","resigned","waited", "arrived", "performed"]
    adjs = ["important", "popular", "famous", "young", "happy", "helpful", "serious", "angry"] # All at least 100 times in MNLI
    advs = ["quickly", "slowly", "happily", "easily", "quietly", "thoughtfully"] # All at least 100 times in MNLI
    
    print('hans old vocab stats:')
    print("nouns_sg: ", len(nouns_sg))
    print("transitive_verbs: ", len(transitive_verbs))
    print("intransitive_verbs: ", len(intransitive_verbs))
    print("adjs: ", len(adjs))
    print("advs: ", len(advs))

def current_hans_vocab_stats():
    print('hans current vocab stats:')
    print("nouns_sg_test: ", len(nouns_sg_test))
    print("transitive_verbs_test: ", len(transitive_verbs_test)+2) # "believed", "stopped"
    print("intransitive_verbs_test: ", len(intransitive_verbs_test)+1) # "left"
    print("adjs_test: ", len(adjs_test))
    print("advs_test: ", len(advs_test))

def main():
    # current_hans_vocab_stats()
    # old_hans_vocab_stats()

    num_seeds = 30

    random.seed(2021)
    seeds = random.sample(range(1, 2021), num_seeds)
    print(seeds)

    for i in range(num_seeds): 
        print(i)
        random.seed(seeds[i]) # setting seed here works for functions imported from templates too

        # randomly sample train and test templates
        template_list_train, template_list_test = template_train_test_split()
        print('template_list_train: ', len(template_list_train))
        print('template_list_test: ', len(template_list_test))

        train_output_path = "/data/rosa/hans-forked/randomness_experiment/train_set_24T_600_seed%d.txt" % i
        # match vocab + match 24 template
        mvmt_test_output_path = "/data/rosa/hans-forked/randomness_experiment/mvmt_test_set_24T_500_seed%d.txt" % i
       
        # mismatch vocab + match 24 template
        misvmt_test_output_path = "/data/rosa/hans-forked/randomness_experiment/misvmt_test_set_24T_500_seed%d.txt" % i

         # match vocab + mismatch 6 template
        mvmist_test_output_path = "/data/rosa/hans-forked/randomness_experiment/mvmist_test_set_6T_500_seed%d.txt" % i

        # mismatch vocab + mismatch 6 template
        misvmist_test_output_path = "/data/rosa/hans-forked/randomness_experiment/misvmist_test_set_6T_500_seed%d.txt" % i

        # training data
        split_seen_words() # Randomly split seen words for training data. Note: test use the unseen words 
        set_datasets_by_type("train")
        generate_samples(train_output_path, 600, template_list_train)
        # match vocab + match 24 template
        generate_samples(mvmt_test_output_path, 500, template_list_train)
        # match vocab + mismatch 6 template
        generate_samples(mvmist_test_output_path, 500, template_list_test)

        # test data
        set_datasets_by_type("test")
        # mismatch vocab + match 24 template
        generate_samples(misvmt_test_output_path, 500, template_list_train)
        # mismatch vocab + mismatch 6 template
        generate_samples(misvmist_test_output_path, 500, template_list_test)


if __name__=="__main__":
    main()



