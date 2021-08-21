import csv
import time


def open_csv_and_extract(file):
    actions = {}
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
                        actions[row_csv[0]] = dict({row_csv[0] + "_cost": float(row_csv[1]),
                                                    row_csv[0] + "_profit": calcul_profit,
                                                    row_csv[0] + "_%profit": float(row_csv[2]),
                                                    })

            i += 1
    return actions


def sort_action_by(actions, benefice):
    sorted_by_dollar = sorted(benefice.items(), key=lambda x: x[0], reverse=True)
    return sorted_by_dollar


def bruteforce(actions):

    action_name = [action for action, value in actions.items()]
    liste_of_possibility = []



    for action in action_name :
        index_action = 0
        start_index = 0
        run = True
        while run :
            possibility = []
            possibility.append(action)
            liste_of_possibility.append(list(possibility))
            tempory_list = action_name[start_index:]
            while len(tempory_list) > 0:
                for element in tempory_list:
                    if element == action :
                        pass
                    else :
                        possibility.append(element)
                        if sorted(list(possibility)) in liste_of_possibility :
                            pass
                        else :
                            liste_of_possibility.append(list(possibility))

                possibility = []
                possibility.append(action)
                tempory_list.pop(0)
                run = False

    for liste in liste_of_possibility :
        #print("liste :")
        print(liste)
    return liste_of_possibility

if __name__ == "__main__":
    start_time = time.time()
    actions = open_csv_and_extract('csv/demo2.csv')
    liste = bruteforce(actions)

    print(len(liste))

    print("--- %s seconds ---" % (time.time() - start_time))
