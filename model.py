import json
from random import randrange, sample

start=1
end=78

class user:
        def __init__(self,userid,username):
            
            self.userid=userid
            self.username=username
            
        def reg(username):
            userid=randrange(start,end) # creating acc number for every new user between the start and end limits \n",
            with open('user.json','r+') as f:
                data=json.load(f)
            while userid in data: # checks if acc_no already exists \n",
                userid=randrange(start,end)
            u1=user(userid,username)

class librarian:
    
    def __init__(self, lib_name, phone_num):
        self.lib_name = lib_name
        self.phone_num = phone_num

    def Lib_login():
        with open('lib.json', 'r') as f:
            data=json.load(f)
        while Libid in data:
            Libid= randrange(start,end) 
        l1=librarian()

    