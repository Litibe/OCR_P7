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


def bruteforce_infinity_time(actions, longueur):
    combinaison = []
    if longueur == 1:
        combinaison = [[action] for action in actions]
    else:
        combinaison = [[action] for action in actions]
        for possibility in combinaison:
            for action in actions:
                if action not in possibility:
                    element = possibility[:]
                    if len(element) < longueur:
                        element.append(action)
                        element.sort()
                        if element not in combinaison:
                            combinaison.append(sorted(element))
    return combinaison


def bruteforce_with_intertool(actions, longueur):
    my_result = [c for c in combinations(actions, longueur)]
    if longueur > 0 :
        my_result.extend(bruteforce_with_intertool(actions, longueur-1))
    return my_result

def filter_max_benefice(actions, my_result):
    actions_to_buy = []
    max_benefice = 0
    min_cost = 500
    for a in my_result:
        sum = 0
        benefice = 0
        for element in a:
            for action in actions:
                if element == action[0]:
                    element = action
            sum += float(element[1])
            benefice += float(element[1])*float(element[2])/100
        if sum < 500 and benefice > max_benefice:
            max_benefice = benefice
            min_cost = sum
            actions_to_buy = a
    return actions_to_buy, max_benefice, min_cost


if __name__ == "__main__":
    start_time = time.time()
    actions = open_csv_and_extract('csv/data_20actions.csv')
    longueur = len(actions)
    actions_name = [action[0] for action in actions]
    my_result = bruteforce_with_intertool(actions_name, longueur)
    print("resultat brute force : ", len(my_result))
    print("resultat 2^n avec n=" + str(longueur) + " : " + str(2**longueur))
    actions_to_buy, max_benefice, min_cost = filter_max_benefice(actions, my_result)
    print(actions_to_buy, "benefice : ", max_benefice, "cout :", min_cost)
    print("--- %s seconds ---" % (time.time() - start_time))
