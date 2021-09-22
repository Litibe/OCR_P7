import csv
import time
from itertools import combinations


def open_csv_and_extract(file):
    actions = []
    with open(file, 'r') as csvfile:
        csvfile_open = csv.reader(csvfile, delimiter=',', quotechar='|')
        i = 0
        for row_csv in csvfile_open:

            if i != 0 and float(row_csv[1]) > float(0) and float(
                    row_csv[2]) > float(0):
                # conversion donnees *100 pour suppression virgule
                # calcul beneficie en index 3
                # ajout dans liste sous forme tuple
                actions.append((row_csv[0],
                                float(row_csv[1]),
                                row_csv[2],
                                round(
                                    float(row_csv[1]) * float(
                                        row_csv[2])/100, 2)))
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


def bruteforce_with_itertools(actions, longueur):
    my_result = [c for c in combinations(actions, longueur)]
    if longueur > 0 :
        my_result.extend(bruteforce_with_itertools(actions, longueur-1))
    return my_result

def filter_max_benefice(brute_force_results):
    actions_to_buy = []
    max_benefice = 0
    max_cost = 500
    for proposition_combinaison in brute_force_results:
        sum_actions = 0
        benefice = 0
        for action in proposition_combinaison:
            sum_actions += action[1]
            benefice += action[3]
        if sum_actions < 500 and benefice > max_benefice:
            max_benefice = benefice
            max_cost = sum_actions
            actions_to_buy = proposition_combinaison
    return actions_to_buy, max_benefice, max_cost



if __name__ == "__main__":
    start_time = time.time()
    actions = open_csv_and_extract('csv/data_20actions.csv')
    my_result = bruteforce_with_itertools(actions, len(actions))
    print("resultat brute force : ", len(my_result))
    print("resultat 2^n avec n=" + str(len(actions)) + " : " + str(2**len(actions)))
    actions_to_buy, max_benefice, min_cost = filter_max_benefice(my_result)
    for action in actions_to_buy :
        print(action)
    print("benefice : ", max_benefice, "cout :", min_cost)
    print("--- %s seconds ---" % (time.time() - start_time))
