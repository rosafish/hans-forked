
f = open("esnli_train_subseq.txt", "a")
fi = open("esnli_train.txt", "r")

count_entailment = 0
count_neutral = 0
count_contradiction = 0

for line in fi:
    parts = line.strip().split("\t")

    premise = parts[5]
    hypothesis = parts[6]
    label = parts[0]

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
        #print(premise, hypothesis, label, parts[1])
        #print(label)
        if label == "entailment":
            count_entailment += 1
        if label == "neutral":
            count_neutral += 1
            print(premise, hypothesis, label, file=f)
        if label == "contradiction":
            count_contradiction += 1
            print(premise, hypothesis, label, file=f)

    #print(premise, hypothesis, label)

print("Entailment:", count_entailment, file=f)
print("Contradiction:", count_contradiction, file=f)
print("Neutral:", count_neutral, file=f)
