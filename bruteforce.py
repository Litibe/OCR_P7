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


def search(actions, longueur):
    my_result = [list(c) for c in combinations(actions, longueur)]
    return my_result


def brutef(actions, longueur):
    combinaison = []
    if longueur == 1 :
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
                        if element not in combinaison :
                            combinaison.append(sorted(element))
    return combinaison


def recurssive(actions, combinaison, longueur):
    for possibility in combinaison:
        for action in actions:
            if action not in possibility:
                if len(possibility) < longueur:
                    element = possibility[:]
                    element.append(action)
                    element.sort()
                    if element not in combinaison:
                        combinaison.append((element))
    return combinaison


def filter_by_size(my_result):
    actions_to_buy = []
    max_benefice = 0
    min_cost = 500
    for a in my_result :
        sum = 0
        benefice=0
        for element in a :
            sum += float(element[1])
            benefice += float(element[1])*float(element[2])/100
        if sum < 500 and benefice>max_benefice:
            max_benefice = benefice
            min_cost = sum
            actions_to_buy = a
    return actions_to_buy, max_benefice, min_cost


if __name__ == "__main__":
    start_time = time.time()
    actions = open_csv_and_extract('csv/demo.csv')
    longueur = 5
    actions_name = [action[0] for action in actions]
    my_result = brutef(actions, longueur)
    print(len(my_result))
    actions_to_buy, max_benefice, min_cost = filter_by_size(my_result)
    print(actions_to_buy, "benefice : ", max_benefice, "cout :", min_cost)
    print("--- %s seconds ---" % (time.time() - start_time))
