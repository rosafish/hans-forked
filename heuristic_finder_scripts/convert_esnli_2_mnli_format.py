# converts esnli_train.csv to multinli_1.0_train.txt format
# so that I can call the heuristic finder scripts on the esnli data as well
# Note that SNLI is in (basically) the same format as MNLI, so just add explanation from esnli to SNLI and match the pairIDs
import csv


def main():
    esnli_input_path = '/data/rosa/data/esnli/esnli_train.csv'
    snli_input_path = '/data/rosa/data/glue/glue_data/SNLI/original/snli_1.0_train.txt'
    output_path = './esnli_train.txt'

    id_expl_dict = dict()
    with open(esnli_input_path, newline='') as fi:
        reader = csv.reader(fi)
        for (i, line) in enumerate(reader):
            if i == 0:
                continue
            pairID = line[0]
            # gold_label = line[1]
            gold_expl1 = line[4]
            if pairID in id_expl_dict:
                print('duplicate ID')
                return
            id_expl_dict[pairID] = gold_expl1

    fo = open(output_path, "w")
    # just keep the same things for position 0, 1, 5, 6

    snli_text_file = open(snli_input_path, "r") 
    snli_lines = snli_text_file.readlines()
    for (i, line) in enumerate(snli_lines):
        if i == 0:
            fo.write(line[:-1] + "\tgold_expl1\n")
            continue
        labels = line.strip().split("\t")
        pairID = labels[8] 
        if pairID in id_expl_dict:
            gold_expl1 = id_expl_dict[pairID]
            fo.write(line[:-1] + "\t" + gold_expl1+ "\n")

    fo.close()
    

if __name__=='__main__':
    main()