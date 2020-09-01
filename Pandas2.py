# -*- coding: utf-8 -*-
"""
Created on Sun May  5 12:55:40 2019

@author: zhaoy
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def number_check(target):  
    try:
        int(target) #Will only work if the string consists of all numbers.
        return True #Ends the function.
    except ValueError: #If int(string) runs into an error
        return False #Ends the function.

def bar_chart(col_1 = False, col_2 = False, col_3 = False, data = False):
    if col_3:
        barchart = sns.barplot(x = col_1, y = col_3, hue = col_2, data = data)
        barchart.set_title(col_2 + " in " + col_1 + " by " + col_3)
        plt.xticks(rotation = 270)
        plt.show()
    else:
        barchart = sns.barplot(x = col_1, y = col_2, data = data)
        barchart.set_title(col_1 + " by " + col_2)
        plt.xticks(rotation = 270)
        plt.show()

def P_Func(col_1, col_2, order, amount):
    data = pd.ExcelFile("SP19SalesData.xlsx").parse("Orders")[[col_1, col_2]].groupby([col_1]).sum().sort_values(by=[col_2])   
    if order == "head":   
        data = data.head(amount)
        print(data)
        bar_chart(col_1, col_2, data = data.reset_index())
    if order == "tail":
        data = data.tail(amount)
        print(data)
        bar_chart(col_1, col_2, data = data.reset_index())
        
def P_Func_Plus(col_1, col_2, col_3, order, amount):   
    data = pd.ExcelFile("SP19SalesData.xlsx").parse("Orders")[[col_1, col_2, col_3]].groupby([col_1, col_2]).sum().sort_values(by=[col_3])
    if order == "head":  
        data = data.head(amount)
        print(data)
        #bar_chart(col_1, col_2, col_3, data)
    if order == "tail":
        data = data.tail(amount)
        print(data)
        #bar_chart(col_1, col_2, col_3, data)

def col_one_func():
    while True:
        select = input("1) Customer" + "\n2) Region" + "\n3) Product" + "\n4) Return to Main Menu" + "\n5) Logout and exit program\n" + "\nPlease select a sort type: ")
        if select == '1':
            return col_one_customer()
        elif select == '2':
            return col_one_region()
        elif select == '3':
            return col_one_product()
        elif select == '4':
            return 'main'
        elif select == '5':
            return 'exit'
        else:
            print("Invalid input. Please try again.")

def col_one_customer():
    while True:
        select = input("1) Customer Name" + "\n2) Customer ID" + "\n3) Customer Segment" + "\n4) Return to Main Menu" + "\n5) Logout and exit program\n" + "\nPlease select a customer type: ")
        if select == '1':
            return "Customer Name"
        elif select == '2':
            return "Customer ID"
        elif select == '3':
            return "Segment"
        elif select == '4':
            return 'main'
        elif select == '5':
            return 'exit'    
        else:
            print("Invalid input. Please try again.")

def col_one_region():
    while True:
        select = input("1) Country" + "\n2) Cardinal Region" + "\n3) State" + "\n4) Postal Code" + "\n5) City" + "\n6) Return to Main Menu" + "\n7) Logout and exit program\n" + "\nPlease select a region type: ")
        if select == '1':
            return "Country"
        elif select == '2':
            return "Region"
        elif select == '3':
            return "State"
        elif select == '4':
            return "Postal Code"
        elif select == '5':
            return "City"
        elif select == '6':
            return 'main'
        elif select == '7':
            return 'exit'
        else:
            print("Invalid input. Please try again.")

def col_one_product():
    while True:
        select = input("1) Category" + "\n2) Sub-Category" + "\n3) Product Name" + "\n4) Product ID" + "\n5) Return to Main Menu" + "\n6) Logout and exit program\n" + "\nPlease select a region type: ")
        if select == '1':
            return "Category"
        elif select == '2':
            return "Sub-Category"
        elif select == '3':
            return "Product Name"
        elif select == '4':
            return "Product ID"
        elif select == '5':
            return 'main'
        elif select == '6':
            return 'exit'
        else:
            print("Invalid input. Please try again.")

def col_two_func():
    while True:
        select = input("1) Sales" + "\n2) Profit" + "\n3) Quantity" + "\n4) Return to Main Menu" + "\n5) Logout and exit program\n" + "\nPlease select a sort type: ")
        if select == '1':
            return "Sales"
        elif select == '2':
            return "Profit"
        elif select == '3':
            return"Quantity"
        elif select == '4':
            return 'main'
        elif select == '5':
            return 'exit'    
        else:
            print("Invalid input. Please try again.")

def h_or_t():
    while True:
        select = input("1) Sort from highest" + "\n2) Sort from lowest" + "\n3) Return to Main Menu" + "\n4) Logout and exit program\n" + "\nPlease select a sort order: ")
        if select == '1':
            return "tail"
        elif select == '2':
            return "head"
        elif select == '3':
            return 'main'
        elif select == '4':
            return 'exit'    
        else:
            print("Invalid input. Please try again.") 
            
def sales_menu_one_var():
    while True:
        print("\n====================Variable One====================")
        col_one = col_one_func()
        if col_one == 'main':
            return True
        elif col_one == 'exit':
            return False
        else:
            print("\n====================Variable Two====================")
            col_two = col_two_func()
            if col_two == 'main':
                return True
            elif col_two == 'exit':
                return False
            else:
                print("\n====================Order====================")
                order = h_or_t()
                if order == 'main':
                    return True
                elif order == 'exit':
                    return False
                else:
                    while True:
                        amount = int(input("\n====================Amount====================\n" + "\nPlease enter the number of entries to view: "))
                        if not number_check(amount):
                            print("Invalid input. Please try again.") 
                        else:
                            P_Func(col_one, col_two, order, amount)
                            return True

def sales_menu_two_var():
    while True:
        print("\n====================Variable One====================")
        col_one = col_one_func()
        if col_one == 'main':
            return True
        elif col_one == 'exit':
            return False
        else:
            print("\n====================Variable Two====================")
            col_two = col_one_func()
            if col_two == 'main':
                return True
            elif col_two == 'exit':
                return False
            else:
                print("\n====================Variable Three====================")
                col_three = col_two_func()
                if col_three == 'main':
                    return True
                elif col_three == 'exit':
                    return False
                else:
                    print("\n====================Order====================")
                    order = h_or_t()
                    if order == 'main':
                        return True
                    elif order == 'exit':
                        return False
                    else:
                        while True:
                            amount = int(input("====================Amount====================\n" + "\nPlease enter the number of entries to view: "))
                            if not number_check(amount):
                                print("Invalid input. Please try again.") 
                            else:
                                P_Func_Plus(col_one, col_two, col_three, order, amount)
                                return True