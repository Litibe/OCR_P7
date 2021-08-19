import csv
import time


def open_csv_and_extract(file):
    actions = {}
    benefice = {}
    with open(file, 'r') as csvfile:
        csvfile_open = csv.reader(csvfile, delimiter=',', quotechar='|')
        i = 0
        for row_csv in csvfile_open:
            if i == 0:
                pass
            else:
                calcul_benefice = round(float(row_csv[1]) * float(row_csv[2]) / 100, 2)
                actions[row_csv[0]] = dict({row_csv[0] + "_cost": float(row_csv[1]),
                                            row_csv[0] + "_evolution": float(row_csv[2]),
                                            row_csv[0] + "_benefice": calcul_benefice})
                benefice[calcul_benefice] = row_csv[0]
            i += 1
    return actions, benefice


def sort_action_by(actions, benefice):
    sorted_by_dollar = sorted(benefice.items(), key=lambda x: x[0], reverse=True)
    return sorted_by_dollar


def search_rentability(actions, benefice, sorted_by_dollar):
    buy = 0
    win = 0
    action_to_buy = []
    i = 0
    for dollar, action_name in sorted_by_dollar:
        action_cost = (actions.get(action_name)).get(action_name + "_cost")
        if i < 0:
            i += 1
        else:
            if buy + action_cost < 500 and dollar > 0 :
                buy += action_cost
                win += dollar
                action_to_buy.append(action_name)

    print(buy)
    print(win)
    print(action_to_buy)


if __name__ == "__main__":
    start_time = time.time()
    actions, benefice = open_csv_and_extract('csv/dataset1_Python+P7.csv')
    sorted_by_dollar = sort_action_by(actions, benefice)
    search_rentability(actions, benefice, sorted_by_dollar)
    print(actions.get('Share-VNQN'))
    print("--- %s seconds ---" % (time.time() - start_time))
