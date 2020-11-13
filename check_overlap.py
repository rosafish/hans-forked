# find overlap samples between two datasets (in format generated by corpus_generator.py)
import collections


class Sample():
    def __init__(self, pairID, gold_label, premise, hypothesis, low_q_expl, high_q_expl):
        self.pairID = pairID
        self.gold_label = gold_label
        self.premise = premise
        self.hypothesis = hypothesis
        self.low_q_expl = low_q_expl
        self.high_q_expl = high_q_expl

    def __eq__(self, other):
        return self.gold_label==other.gold_label and \
               self.premise==other.premise and \
               self.hypothesis==other.hypothesis

    def __str__(self):
        return self.gold_label + self.premise + self.hypothesis 

    def __hash__(self):
        return hash(str(self))


def read_data(data):
    samples = []

    data_file = open(data, "r") 
    hans_lines = data_file.readlines()
    for (i, line) in enumerate(hans_lines):
        if i == 0:
            continue
        labels = line.strip().split("\t")
        # note: not taking the heuristic here because i know all these is for 1 template
        # but should take the heuristic if work with 30 templates (or anything > 1)
        sample = Sample(labels[7], labels[0], labels[5], labels[6], labels[11], labels[12])
        samples.append(sample)
        
    return samples


def output_samples_to_file(samples, path):
    print('write to: ', path)
    fo = open(path, "w")
    fo.write("gold_label\tsentence1_binary_parse\tsentence2_binary_parse\t\
    sentence1_parse\tsentence2_parse\t\
    sentence1\tsentence2\tpairID\theuristic\t\
    subcase\ttemplate\tlow_q_expl\thigh_q_expl\n")

    for sample in samples:
        fo.write(sample.gold_label + "\t" + "None" + "\t" + "None" + "\t" + \
        "None" + "\t" + "None" + "\t" + \
        sample.premise + "\t" + sample.hypothesis + "\t" + sample.pairID + "\t" + "None" + "\t" + \
        "None" + "\t" + "None" + "\t" + sample.low_q_expl + "\t" + sample.high_q_expl + "\n")
    fo.close()

def main():
    train = './rosa_heuristics_train_set_30T_15000.txt'
    dev = './rosa_heuristics_dev_set_30T_300_filtered_1500_3000.txt'
    # test = './rosa_heuristics_test_set_2500.txt'

    train_samples = read_data(train)
    dev_samples = read_data(dev)
    # test_samples = read_data(test)

    print(len(set(train_samples))) # no dups in train
    print(len(set(dev_samples))) # no dups in dev
    # print(len(set(test_samples))) # no dups in test
    # print(len(set(test_samples)|set(train_samples))) # 8 overlaps between train and test
    print(len(set(dev_samples)|set(train_samples))) # 4 overlaps between train and dev
    # print(len(set(dev_samples)|set(test_samples))) # no overlap between dev and test

    # remove dups from dev and test
    dev_filtered = set(dev_samples) - set(train_samples)
    # test_filtered = set(test_samples) - set(train_samples)
   

    # output the filtered sets
    output_samples_to_file(dev_filtered, "./rosa_heuristics_dev_set_30T_300_filtered_1500_3000_15000.txt")
    # output_samples_to_file(test_filtered, "./rosa_heuristics_test_set_2500_filtered.txt")


if __name__=="__main__":
    main()