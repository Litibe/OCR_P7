import csv
import time
from itertools import combinations



def open_csv_and_extract(file):
    actions = []
    with open(file, 'r') as csvfile:
        csvfile_open = csv.reader(csvfile, delimiter=',', quotechar='|')
        i = 0
        for row_csv in csvfile_open:
            if i == 0:
                pass
            else:
                if float(row_csv[1]) <= float(0):
                    pass
                else:
                    calcul_profit = round(float(row_csv[1]) * float(row_csv[2]) / 100, 2)
                    if float(row_csv[1]) <= 0 or float(row_csv[2]) <= 0:
                        pass
                    else:
                        actions.append((row_csv[0], float(row_csv[1]), calcul_profit))
            i += 1
    return actions

def search(actions, my_result):
    for number in range(1, len(actions)+1):
        my_result.extend([c for c in combinations(actions, number)])
    return my_result


def search2(actions, my_result):
    for number in range(1, len(actions)+1):
        for c in combinations(actions, number):
            my_result.append(c)
    return my_result


if __name__ == "__main__":
    start_time = time.time()
    actions = open_csv_and_extract('csv/demo.csv')
    #print(actions)
    my_result = []
    b = search2(actions, my_result)
    print(len(b))
    print("--- %s seconds ---" % (time.time() - start_time))
