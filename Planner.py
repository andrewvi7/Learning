import pandas as pd


class Goals:
    def __init__(self, name, description, record=None):
        self.name = name
        self.description = description
        self.record = record


def menu():
    options = {'0': " - View planner for current weak",
               '1': " - View goals:",
               '2': " - New goal",
               '3': " - Delete Goal"}
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
    desc = input('Description')
    goals_lst.append(Goals(name, desc))


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


goals_lst = []
goals_lst.append(Goals("Running", "Forest fields and back"))
goals_lst.append(Goals("Gym", "Weights session"))
goals_lst.append(Goals("Reading", "1h each session"))
print(goals_lst)
menu()
