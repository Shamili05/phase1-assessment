import sqlite3

con=sqlite3.connect('library.db')

cursorobj=con.cursor()
def start():
    menu='''
    Welcome to the Library 
    Please enter an option:
    1.New user rregistration
    2.Login
    3.Exit
    '''
    choice=input(menu)
    return choice 

def start_lib():
    menu='''
    Welcome to the Library 
    Please enter an option:
    1.librarian login
    2.add books
    3.Exit
    '''
    choice=input(menu)
    return choice 
def user_reg():
    u_name = input('User Name:')
    u_emailid = input('Email id:')
    u_phone = input('Phone num:')
    reg_date = input('Registration date:')
    print("Registration successful")
    print ("Your User id:" , u_name)
    print ("user password:", u_phone)
    con.execute("""INSERT INTO Users(name, email_id, phone_num,date_of_reg) VALUES (?,?,?,?)""", (u_name, u_emailid, u_phone,reg_date))

def user_login():
    username =str(input("Enter the username:   "))
    password_1=int(input("Enter the password: "))
    password_2=int(input("Enter the password again: "))
    if password_1==password_2:
        print("Passwords match")
        return username,password_1
    
    else:
        print("Passwords do not match: RETRY!")
        user_login()

def success_reg():
    print("User registered successfully")


def success_login():
    print("User logged in sucessfully")

def invalid():
    print("Invalid choice")    

def prompt():
    print("Not logged in")

def exit():
    print("logged out")

def addbooks():

    b_name = input('Book Name:')
    a_name = input('Author name:')
    publi_name = input('Publication name:')
    rentdate = input('Rented date:')
    username=input('user name:')
    con.execute("""INSERT INTO Book(book_name,author_name, publication_name, rent_date,user_name) VALUES (?,?,?,?,?)""", (b_name, a_name, publi_name,rentdate, username))

def lib_login():
    Lname =str(input("Enter the username:   "))
    Lpassword_1=int(input("Enter the password: "))
    Lpassword_2=int(input("Enter the password again: "))
    if Lpassword_1==Lpassword_2:
        print("Passwords match")
        print("Your are logged in")
        return Lname,Lpassword_1