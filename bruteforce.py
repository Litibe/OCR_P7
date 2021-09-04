import csv
import time
from itertools import combinations


class Action:

    def __init__(self, name, cost, profit):
        self.name = name
        self.cost = float(cost)
        self.profit = float(profit)
        self.benefice = round(float(float(cost) * float(profit) /100), 2)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.name


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
                    if float(row_csv[1]) <= 0 or float(row_csv[2]) <= 0:
                        pass
                    else:
                        row_csv[0] = Action(row_csv[0], row_csv[1], row_csv[2])
                        actions.append(row_csv[0])
            i += 1
    return actions

def search(actions, my_result):
    for number in range(1, len(actions)+1):
        my_result.extend([c for c in combinations(actions, number)])
    return my_result

def brute(actions, my_result):
    pass


if __name__ == "__main__":
    start_time = time.time()
    actions = open_csv_and_extract('csv/demo.csv')
    print(actions)
    my_result = []
    #b = search(actions, my_result)
    #print(len(b))
    print("--- %s seconds ---" % (time.time() - start_time))
