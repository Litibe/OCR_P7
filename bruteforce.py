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
                    if float(row_csv[1]) <= 0 or float(row_csv[2]) <= 0:
                        pass
                    else:
                        actions.append((row_csv[0], row_csv[1], row_csv[2]))
            i += 1
    return actions

def search(actions, my_result):
    for number in range(1, len(actions)+1):
        my_result.extend([c for c in combinations(actions, number)])
    return my_result

def brutef(actions, longueur):
    combinaison = []
    if longueur == 1 :
        for action in actions:
            combinaison.append([action])
    else:
        for action in actions :
            combinaison.append([action])
        for possibility in combinaison:
            for action in actions:
                if action not in possibility:
                    element = possibility[:]
                    if len(element) < longueur:
                        element.append(action)
                        element.sort()
                        if element not in combinaison :
                            combinaison.append(sorted(element))
    return combinaison


if __name__ == "__main__":
    start_time = time.time()
    actions = open_csv_and_extract('csv/demo.csv')
    longueur = 5
    actions_name = [action[0] for action in actions]
    my_result = brutef(actions_name, longueur)
    print(len(my_result))
    #b = search(actions, my_result)
    #print(len(b))
    print("--- %s seconds ---" % (time.time() - start_time))
