'''Converts generated data to esnli format and also separate by explanation quality'''

import csv
import sys
sys.path.append('/data/rosa/my_github/misinformation/code/')
from myTools import write_csv

esnli_format_header = ["pairID", "gold_label", "Sentence1", "Sentence2", "Explanation_1",
                        "Sentence1_marked_1", "Sentence2_marked_1", "Sentence1_Highlighted_1",
                        "Sentence2_Highlighted_1", "Explanation_2", "Sentence1_marked_2", "Sentence2_marked_2",
                        "Sentence1_Highlighted_2", "Sentence2_Highlighted_2", "Explanation_3", "Sentence1_marked_3",
                        "Sentence2_marked_3", "Sentence1_Highlighted_3", "Sentence2_Highlighted_3"]
                        
def main():
    data_dir_name = 'generated_data_new_setting'
    num_seeds = 3
    fi_name_list = ['dev_1', 'dev_2', 'dev_4', 'dev_7', 'dev_13', 'dev_32',
             'train_1', 'train_2', 'train_4', 'train_8', 'train_16', 'train_32', 'train_64',
             'test_ivit_300', 'test_ivot_300', 'test_ovit_300', 'test_ovot_300']
    for seed in range(num_seeds):
        for partition in range(5):
            path = './%s/seed%d/partition%d/' % (data_dir_name, seed, partition)
            for fi in fi_name_list:
                fi_path = path + fi + '.csv'
                fo_nl = path + fi + '_nl.csv' # natural language explanation
                fo_pt = path + fi + '_pt.csv'# pointer-only explanations
                fo_empty_expl = path + fi + '_empty_expl.csv' # empty_expl

                nl_rows = []
                pt_rows = []
                empty_expl_rows = []

                with open(fi_path) as f:
                    reader = csv.reader(f)
                    for (i, line) in enumerate(reader):
                        if i > 0:
                            guid = line[0]
                            label = line[5]
                            p = line[-4]
                            h = line[-3]
                            nl = line[-2]
                            pt = line[-1]

                            nl_row = [""]*19
                            nl_row[0] = guid
                            nl_row[1] = label
                            nl_row[2] = p
                            nl_row[3] = h
                            nl_row[4] = nl

                            pt_row = [""]*19
                            pt_row[0] = guid
                            pt_row[1] = label
                            pt_row[2] = p
                            pt_row[3] = h
                            pt_row[4] = pt

                            empty_expl_row = [""]*19
                            empty_expl_row[0] = guid
                            empty_expl_row[1] = label
                            empty_expl_row[2] = p
                            empty_expl_row[3] = h

                            nl_rows.append(nl_row)
                            pt_rows.append(pt_row)
                            empty_expl_rows.append(empty_expl_row)

                write_csv(fo_nl, nl_rows, esnli_format_header)
                write_csv(fo_pt, pt_rows, esnli_format_header)
                write_csv(fo_empty_expl, empty_expl_rows, esnli_format_header)

if __name__=='__main__':
    main()
