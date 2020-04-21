import pandas as pd
import _pickle as pickle


class Goals:
    def __init__(self, name, description, record=None):
        self.name = name
        self.description = description
        self.record = record


def save_data():
    with open('data.obj', 'wb') as file:
        pickle.dump(goals_lst, file)


def load_data():
    global goals_lst
    file = open('data.obj', 'rb')
    goals_lst = pickle.load(file)


def menu():
    options = {'0': " - View planner for current week",
               '1': " - View goals:",
               '2': " - New goal",
               '3': " - Delete goal"}
    for idx, idx_name in options.items():
        print(idx, idx_name)
    option = input("...: ")
    if option == '0':
        array()
        menu()
    elif option == '1':  # View goals
        view()
        menu()
    elif option == '2':  # New goal
        new_goal()
        menu()
    elif option == '3':  # Delete
        del_goal()
        menu()
    else:
        print("wrong option")
    menu()


def array():
    dataframe = pd.DataFrame(data=None)
    for goal in goals_lst:
        df = pd.DataFrame([[goal.name, goal.description, goal.record]], columns=['Goals', 'Description', 'Record'],
                          dtype='float64')
        dataframe = pd.concat([df, dataframe], ignore_index=True)
    print("\n", dataframe, "\n")


def week_view():
    pass


def new_goal():
    print("New goal details")
    name = input('Name: ')
    desc = input('Description: ')
    goals_lst.append(Goals(name, desc))
    save_data()


def view():
    print('-' * 20, " GOALS ", '-' * 20)
    count = 1
    for goal in goals_lst:
        print(str(count) + ".", goal.name, '-', goal.description)
        count += 1
    print('-' * 50)


def del_goal():
    view()
    option = int(input("Goal to delete: "))
    if 0 < option <= len(goals_lst):
        _waste = goals_lst.pop(option - 1)
    save_data()


goals_lst = []
load_data()
menu()
