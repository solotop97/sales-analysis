#function: Takes a string and checks first and last index for ' ', '\t', or '\n' then strip() is used. Loops until both ends are not ' ', '\t', or '\n'. Returns the stripped string. 
#          Good if whitespaces not on ends wanted. Otherwise replace(" ", "").replace("\t", "").replace("\n", "") works too.
#
#argument(s): string target - To be copied into temp and stripped of whitespaces on ends. Leaves initial string untouched.
#
#return(s): temp string - removed string with no whitespaces on ends.
def remove_all(target):
    trash = [' ', '\t', '\n'] #List of unwanted characters.
    if target is True:
        temp = target #To ensure parameter string is left untouched
        while True: #Loops until break.
            if temp: #To ensure that the while loop won't crash on running strip().
                temp = temp.strip() #Removes whitespace on both ends of string.
                if temp is True:
                    if temp and temp[0] not in trash and temp[-1] not in trash: #Checks if string is empty and if ends are unwanted characters.
                        return temp #Ends the function.
                else:
                    return temp
    else:
        return target #Ends the function.

#function: Takes parameter of string for title of name plus a space. Takes an input string and capitalizes first character and lowwercases rest. Also uses strip_all(). Returns a string.
#
#argument(s): string title - Title of name you want to ask for (e.g. first, middle, last). Defaults to ''.
#
#return(s): string name - All alphabet, only first letter capitalized.
def make_name(title = ''): 
        message = "name: "
        if title: #Runs if title is not empty.
                message = message.rjust(7, ' ') #Adds a space to the left of message.
        while True: #Loops until break.
            print("\nName must be all alphabetic characters.")
            name = remove_all(input("Please enter " + title + message)).lower().capitalize()
            try:
                if name: #Checks if string is empty.
                    if name.isalpha(): #Checks if string is alphabet characters only.
                        return(name) #Ends the function.
                else: #If name is empty.
                    continue #Continues the while loop.
            except AttributeError: #If name.isalpha() fails.
                continue #Continues the while loop.    
      
        
#function: Checks if a string is made of all integers.
#
#argument(s): string target - Checked if is an int. Does not convert to int.
#
#return(s): bool temp - True or False
def number_check(target):  
    try:
        int(target) #Will only work if the string consists of all numbers.
        return True #Ends the function.
    except ValueError: #If int(string) runs into an error
        return False #Ends the function.
    
    
    
import sqlite3
conn = sqlite3.connect("OS_Employee.db") #Connect to database of choice.
cur = conn.cursor() #Shorthand.    
    


class Employee():
  
    
    def init(self, EmployeeID, FirstName, LastName, Email, Password):
        self.EmployeeID = EmployeeID
        self.FirstName = FirstName
        self.LastName = LastName
        self.Email = Email
        self.Password = Password
        
        
    def set_EmployeeID(self):
        conn = sqlite3.connect("OS_Employee.db") #Connect to database of choice.
        cur = conn.cursor() #Shorthand. 
        with conn:
            while True: #Loops until break.
                print("\nEmployeeID length must be 4 digits long.")
                EmployeeID = remove_all(input("Please enter EmployeeID: "))
                if True:
                    if len(EmployeeID) == 4 and number_check(EmployeeID):
                        cur.execute("SELECT EmployeeID FROM Employee WHERE (EmployeeID = ?)", (EmployeeID,)) #Finds the information related to the ID.
                        if cur.fetchall(): #If the EmployeeID is not taken, it will return an empty string [], therefore be False.
                            print("\nThis EmployeeID is already registered.")
                        else: # If the EmployeeID is not in use.
                            self.EmployeeID = EmployeeID #Ends the function.
                            break
    
    
    def set_FirstName(self):
        self.FirstName = make_name("first")
    
    
    def set_LastName(self):
        self.LastName = make_name("last")
        
        
    def set_Email(self):
        while True: #Loops until break.
            print("\nThe email should be in the format of: ****@****.com")
            Email = remove_all(input("Please enter email: "))
            if len(Email) >= 7 and Email[-4] == '.' and Email[-3] == 'c' and Email[-2] == 'o' and Email[-1] == 'm': #Length of 7 and ending in ".com" check to pass.
                cur.execute("SELECT Email FROM Employee WHERE (Email = ?)", (Email,))
                if cur.fetchall():
                    print("\nThis Email is already used.")
                else:
                    self.Email = Email #Ends the function.
                    break
    
    def set_Password(self):
        Password = remove_all(input("Please enter password: "))
        self.Password = Password
    
    
    def create_Employee(self):
        self.set_EmployeeID()
        self.set_FirstName()
        self.set_LastName()
        self.set_Email()
        self.set_Password()
        
    
    def register_Employee(self):
        conn = sqlite3.connect("OS_Employee.db") #Connect to database of choice.
        cur = conn.cursor() #Shorthand.  
        with conn:
            while True:
                self.create_Employee()
                cur.execute("SELECT EmployeeID FROM Employee WHERE (EmployeeID = ?)", (self.EmployeeID,)) #For checking the EmployeeID with database.
                if not cur.fetchall(): #If the EmployeeID is not taken, it will return an empty string [], therefore be False.
                    cur.execute("INSERT INTO Employee VALUES (?, ?, ?, ?, ?)", (self.EmployeeID, self.FirstName, self.LastName, self.Email, self.Password,)) #Inserts parameters into database. Order matters. Security risk using concatenations of + +.
                    conn.commit
                    print("\nA new employee was successfully registered.\n")
                    cur.execute("SELECT * FROM Employee WHERE (EmployeeID = ?)", (self.EmployeeID,)) #Used to print out newly registered employee's info. Needs to execute again to pass to new fetchall().
                    print(cur.fetchall())
                    break
                else: #If the EmployeeID is in use.
                    print("\nThis EmployeeID is already used.")
        
        
    def login_Employee(self):
        conn = sqlite3.connect("OS_Employee.db") 
        cur = conn.cursor()    
        with conn:
            while True:
                print("\nWelcome to Office Solutions!\n\nPlease enter your login credentials below")
                #Email
                self.Email = input("Email: ")
                self.Email = self.Email.strip() #Removes crashes due to user inputs of spaces and tabs only
                while not self.Email: #Checks if self.Email is empty, if empty ask for self.Email again
                    self.Email = input("Please enter your email: ")
                    self.Email = self.Email.strip() #Removes crashes due to user inputs of spaces and tabs only
                while self.Email[0] == ' ' or self.Email[0] == '\t' or self.Email[len(self.Email) - 1] == ' ' or self.Email[len(self.Email) - 1] == '\t':
                    self.Email = self.Email.strip() #Loop clears all spaces and tabs before and after self.Email, make into function later
                    
                #Password    
                self.Password = input("Password: ")
                self.Password = self.Password.strip() #Removes crashes due to user inputs of spaces and tabs only
                while not self.Password: #Checks if self.Password is empty, if empty ask for self.Password again   
                    self.Password = input("Please enter your password: ")
                    self.Password = self.Password.strip() #Removes crashes due to user inputs of spaces and tabs only
                while self.Password[0] == ' ' or self.Password[0] == '\t' or self.Password[len(self.Password) - 1] == ' ' or self.Password[len(self.Password) - 1] == '\t':
                    self.Password = self.Password.strip() #Loop clears all spaces and tabs before and after self.Password
                    
                    
                #Email and Password sent to SQL must be surrounded by ''
                #self.Email and self.Password must be given outside of the string sent to SQL
                cur.execute("SELECT COUNT (*) FROM Employee WHERE(Email = '" + self.Email.lower() + "' AND Password = '" + self.Password + "')")
                results = cur.fetchone() #Returns 0 for fail or 1 for success in executing login
                if results[0]==1:
                    print("\n====================Login successful====================")
                    return True
                else:
                    print("\n====================Login unsuccessful, please try again====================") #Shows when login credentials don't match database
    
#def main():
#   with conn: #While connected
#        try:
#            bob = Employee()
#            bob.register_Employee()
#        except Exception as e: #Runs if anything in try fails.
#            #print(e) #Shows error for programmer.
#            print("Connection failed")  
#    
#if __name__ == "__main__":
#    main()