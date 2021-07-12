import csv

if __name__=='__main__':
    input_path = './templates.csv'

    with open(input_path) as f:
        reader = csv.reader(f)

        premise_len_sum = 0
        hypothesis_len_sum = 0
        nl_expl_len_sum = 0
        pt_expl_len_sum = 0
        count = 0

        for (i, line) in enumerate(reader):
            if i > 0:
                premise = line[5]
                hypothesis = line[6]
                nl_expl = line[8]
                pt_expl = line[9]

                # premise_tokens = hypothesis.split()
                # print(premise_tokens)

                premise_len_sum += len(premise.split())
                hypothesis_len_sum += len(hypothesis.split())
                nl_expl_len_sum += len(nl_expl.split())
                pt_expl_len_sum += len(pt_expl.split())

                count += 1

        print('premise avg length: ', premise_len_sum/count)
        print('hypothesis avg length: ', hypothesis_len_sum/count)
        print('nl expl avg length: ', nl_expl_len_sum/count)
        print('pt expl avg length: ', pt_expl_len_sum/count)

                




            