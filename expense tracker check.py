#IMPORTING THE LIBRARIES REQUIRED

import numpy as py
import pandas as pd
from datetime import date


#CREATING EMPTY LISTS

GOODS_OR_SERVICES = []
PRICES = []
DATES = []
EXPENSE_TYPES = []


#CREATING A FUNCTION TO ADD THE EXPENSES TO THE LISTS AND ORGANISE THE DATA

def add_expense(good_or_service,price,date,expense_type):
    GOODS_OR_SERVICES.append(good_or_service)
    PRICES.append(price)
    DATES.append(date)
    EXPENSE_TYPES.append(expense_type)


#MAIN CODE

option=-1 #THIS WILL BE THE USERS CHOICE OR INPUT
while(option!=0):

    #CREATING THE OPTION MENU

    print("Welcome to the expense tracker:")
    print("1. Add Food Expense")
    print("2. Add Household Expense")
    print("3. Add Transportation expense")
    print("4. Add Extra Expense")
    print("5. Show And Save The Expense Report")
    print("0. Exit")
    option=int(input("Choose an option:\n" ))


    #PRINTING A NEW LINE

    print()

    #CHECKING FOR THE USERS INPUT OR CHOICE

    if option == 0:
        print('Exiting The Program')
        break
    elif option == 1:
        print('Adding Food')
        expense_type = 'FOOD'
    elif option == 2:
        print('Addding Household')
        expense_type = 'HOUSEHOLD'
    elif option == 3:
        print('Adding Transportation')
        expense_type = 'TRANSPORTATION'
    elif option == 4:
        print('Adding Extra')
        expense_type = 'EXTRAS'
    elif option == 5:

        #CREATING A DATA FRAME AND ADDING THE EXPENSES

        expense_report = pd.DataFrame()
        expense_report['GOODS_OR_SERVICES'] = GOODS_OR_SERVICES
        expense_report['PRICES'] = PRICES
        expense_report['DATES'] = DATES
        expense_report['EXPENSE_TYPES'] = EXPENSE_TYPES

        #SAVE THE EXPENSE REPORT

        expense_report.to_csv('expenses.csv')

        #SHOW THE EXPENSE REPORT

        print(expense_report)
    else:
        print('You Chose An Incorrect Option.Please Choose An Option From 0 To 5')

    #ALLOW THE USER TO ENTER THE GOOD OR SERVICE AND THE PRICE

    if option == 1 or option == 2 or option == 3 or option == 4:
        good_or_service = input('Enter The Good Or Service For The Expense Type '+ expense_type+':\n')
        price = float(input('Enter The Price Of The Good Or Service:\n'))
        today = date.today()
        add_expense(good_or_service,price,today,expense_type)

    #PRINTING A NEW LINE
    print()
