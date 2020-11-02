import sys
sys.path.append('/data/rosa/my_github/misinformation/code/')
from myTools import write_csv

fi = open("esnli_train.txt", "r")

fo_path = './esnli_train_subseq.csv'
fo_header = ['guid', 'label', 'premise', 'hypothesis', 'expl1', 'template']
fo_row_data = []

count_entailment = 0
count_neutral = 0
count_contradiction = 0

for line in fi:
    parts = line.strip().split("\t")

    premise = parts[5]
    hypothesis = parts[6]
    label = parts[0]
    guid = parts[8]
    expl1 = parts[-1]

    prem_words = []
    hyp_words = []

    for word in premise.split():
        if word not in [".", "?", "!"]:
            prem_words.append(word.lower())

    for word in hypothesis.split():
        if word not in [".", "?", "!"]:
            hyp_words.append(word.lower())

    prem_filtered = " ".join(prem_words)
    hyp_filtered = " ".join(hyp_words)

    if hyp_filtered in prem_filtered:
        if label == "entailment":
            count_entailment += 1
        if label == "neutral":
            count_neutral += 1
            #print(premise, hypothesis, label)
            fo_row_data.append([guid, label, premise, hypothesis, expl1, ""])
        if label == "contradiction":
            count_contradiction += 1
            # print(premise, hypothesis, label)
            fo_row_data.append([guid, label, premise, hypothesis, expl1, ""])

print("Entailment:", count_entailment)
print("Contradiction:", count_contradiction)
print("Neutral:", count_neutral)

write_csv(fo_path, fo_row_data, fo_header)
