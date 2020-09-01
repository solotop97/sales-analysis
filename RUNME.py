#Main Menu

from Class_Testing2 import Employee
from Pandas2 import sales_menu_one_var


test = Employee()
flag_menu = test.login_Employee() 

while flag_menu:
    select = input("====================Main Menu====================\n" + "\n1) View Sales Data with Two Variables"  + "\n2) Register New User" + "\n3) Logout and return to login" + "\n4) Logout and exit program\n" + "\nPlease enter a number: " ) 
    if select == '1':
        flag_menu = sales_menu_one_var()  
    elif select == '2':
            test.register_Employee()
    elif select == '3':
        flag_menu = test.login_Employee()
    elif select == '4':
        break
    else:
        print("Invalid input. Please try again.")

print("\n====================Program terminated====================")