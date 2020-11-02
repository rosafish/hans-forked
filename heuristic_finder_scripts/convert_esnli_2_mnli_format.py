# converts esnli_train.csv to multinli_1.0_train.txt format
# so that I can call the heuristic finder scripts on the esnli data as well
# Note that SNLI is in (basically) the same format as MNLI, so just add explanation from esnli to SNLI and match the pairIDs
import csv

def list_to_line(alist):
    result = ""
    for item in alist:
        result = result + item + '\t'
    result = result[:-1] 
    result = result + "\n"
    return result

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
            gold_label = line[1]
            gold_expl1 = line[4]
            premise = line[2]
            hypothesis = line[3]
            if pairID in id_expl_dict:
                print('duplicate ID')
                return
            id_expl_dict[pairID] = (premise, hypothesis, gold_label, gold_expl1)

    fo = open(output_path, "w")
    # just keep the same things for position 0, 1, 5, 6

    snli_text_file = open(snli_input_path, "r") 
    snli_lines = snli_text_file.readlines()
    for (i, line) in enumerate(snli_lines):
        parts = line.strip().split("\t")
        parts = parts[:9]
        if i == 0:
            parts.append('gold_expl1')
            fo.write(list_to_line(parts))
            continue

        pairID = parts[8] 
        snli_label = parts[0]
        if pairID in id_expl_dict:
            info_tuple = id_expl_dict[pairID]
            esnli_label = info_tuple[2]
            if snli_label.lower() != esnli_label.lower():
                print('label does not match between snli and esnli')
            #make create the new line to write
            parts[5] = info_tuple[0] # premise
            parts[6] = info_tuple[1] # hypothesis
            parts.append(info_tuple[3]) # expl1
            fo.write(list_to_line(parts))

    fo.close()
    

if __name__=='__main__':
    main()