#! /usr/bin/python3

def update_expenses(expense_list, expenses_dict):
    expenses_dict = {'food' : 500, 'rent': 750, 'travel': 370}
    print("Recorded expenses: ", expenses_dict)
    for items in expense_list:
          if not items.isnumeric():
            string = str(items)
          elif items.isnumeric() and string not in expenses_dict:
            expenses_dict.update({string:items})
          elif items.isnumeric() and string in expenses_dict:
              expenses_dict[string] = expenses_dict.get(string, 0)+int(items)
           
             
    print_expenses(expenses_dict)
            

def print_expenses(expenses_dict):
    print("Modified expenses: \n")
    for items in expenses_dict:
        if not items.isnumeric():
            string = str(items)
        print(f"{string}: {expenses_dict[items]} \n" )

expenses_dict = {}
expense_list = tuple(input("Please enter the expense categories and values separated by a blank space: ").split())

update_expenses(expense_list, expenses_dict)



