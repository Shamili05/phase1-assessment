import model
import view 
import logging # tracking of events 

def onboard():
    menu1='''
    1. user registration
    2. user login
    3. Librarian login
    4. Exit 

    '''
    choice = int(input("Enter Choice:"))
    
    while choice!='3': # None!= 3 --> True # create account 
        choice=view.start()
        logging.info(f"The choice selected by the user is {choice}")
        if choice=='1':
            view.user_reg()
            view.success_reg()
            
        elif choice=='2':
            username,password=view.user_login()
            logging.info(f"User name entered for login is  {username} and password is {password}")
            u1=model.user.reg(username)
            while u1==False:
                logging.error(f"Invalid credentials entered: username-->{username} and password --> {password}")
                view.incorrect_credentials()
                userid,password=view.prompt()
                u1=model.user.login(userid,password)
                view.success_login()
                logging.info(f"Successful login with userid {userid}")
                u1=model.user.user_login()
        else:
            view.exit()


def library():
    menu='''
        1. librarian login
        2. addbooks
        3.exit
    
    '''
    choice=None
    while choice!=4:
        choice=view.start_lib()
        if choice=='1':
            view.lib_login()
        elif choice=='2':
            view.addbooks()
        elif choice=='3':
            view.exit()
        else:
            view.invalid()
            


if __name__=="__main__":
    onboard()         
    library()