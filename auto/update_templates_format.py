# the old templates.csv had format issue: there is space after the comma separator, and it can affect tokenization 
# the modeling part.
import csv
import sys
sys.path.append('/data/rosa/my_github/misinformation/code/')
sys.path.append('/home/zhouy1/misinformation/code/')
from myTools import write_csv


def main():
    fi = './templates.csv'
    fo = './templates_new.csv'

    rows = []

    with open(fi) as f:
        reader = csv.reader(f)
        for (i, line) in enumerate(reader):
            if i == 0:
                header = line
            if i > 0:
                for j in range(len(line)):
                    item = line[j]
                    while item[0] == ' ':
                        item = item[1:]
                    while item[-1] == ' ':
                        item = item[:-1]
                    line[j] = item
                rows.append(line)

    write_csv(fo, rows, header)
    

if __name__=='__main__':
    main()