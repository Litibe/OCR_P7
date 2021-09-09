import csv
import time


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


def construction_tableau(actions, budget):
    # tableau double
    # abcisse avec recherche budget, première case 0 pour initialiser
    # ordonnées liste des actions , première case 0 pour initialiser
    tableau = [[0 for x in range(budget + 1)] for x in range(len(actions) + 1)]

#  on commence par index 1 et Non 0 pour faire comparation de l'action en cours avec action précédente
    for number_action in range(1, len(actions) + 1):
        # extraction de l'index des actions pour search_actions
        for monnaie in range(1, budget + 1):
            # extraction de chaque euro issue du budget pour comparatif
            # (NAME_ACTION, cost, %profit)
            # si l'action en cours a un cout d'achat < au budget en cours
            if int(actions[number_action-1][1]) <= int(monnaie):
                tableau[number_action][monnaie] = max(
                    float(actions[number_action-1][2]
                          )*float(
                        actions[number_action-1][1])/100 + float(
                        tableau[number_action-1][int(monnaie)-int(actions[number_action-1][1])]), float(tableau[number_action-1][monnaie]))
                #au dessus calcul du benefice de l action depuis cout/%profit
            else :
                tableau[number_action][monnaie] = float(tableau[number_action-1][monnaie])

    for ligne in tableau :
        print(ligne)
if __name__ == "__main__":
    start_time = time.time()
    actions = open_csv_and_extract('csv/demo.csv')
    resultat = construction_tableau(actions, 500)

    print("--- %s seconds ---" % (time.time() - start_time))
