import sqlite3

con=sqlite3.connect('library.db')

cursorobj=con.cursor()

con.execute("CREATE TABLE Users(id integer PRIMARY KEY autoincrement, name text, email_id text,phone_num integer, date_of_reg date)")


con.execute("INSERT INTO Users(name, email_id ,phone_num , date_of_reg ) VALUES ( 'HITESH','hitesh@gmail.com',5679877, '17-09-2022')")
con.execute("INSERT INTO Users(name, email_id ,phone_num , date_of_reg ) VALUES ( 'GOPESH','gopesh@gmail.com',5679877, '18-09-2022')")
con.execute("INSERT INTO Users(name, email_id ,phone_num , date_of_reg ) VALUES ( 'KAVISH', 'kavi@gmail.com',98675055, '16-04-2022')")
con.execute("INSERT INTO Users(name, email_id ,phone_num , date_of_reg ) VALUES ( 'Pooja', 'pooju@gmail.com',98987555, '13-04-2022')")
con.execute("INSERT INTO Users(name, email_id ,phone_num , date_of_reg ) VALUES ( 'Dharshni', 'dhars@gmail.com',67667555, '14-04-2022')")


'''data1=con.execute("SELECT * FROM User")
for row in data1:
    print(row)'''
con.execute("CREATE TABLE Book (id integer PRIMARY KEY autoincrement,book_name text, author_name text,publication_name, rent_date date, user_name)")

con.execute("INSERT INTO Book(book_name,author_name, publication_name, rent_date,user_name) VALUES ('C PROGRAMIING', 'BALAGURUSWAMY', 'TATA MC GRAW HILL', '12-04-2022', 'HITESH')")
con.execute("INSERT INTO Book(book_name,author_name, publication_name, rent_date,user_name) VALUES ('JAVA PROGRAMIING', 'BALAGURUSWAMY', 'TATA MC GRAW HILL', '22-04-2022', 'GOPESH')")

con.execute("CREATE TABLE Librarians(id integer PRIMARY KEY autoincrement, lib_name text, phone_num integer) ")

con.execute("INSERT INTO Librarians (lib_name,phone_num)VALUES ('Pradeep', 89898989)")
con.execute("INSERT INTO Librarians (lib_name,phone_num)VALUES ('jithesh',6754689)")

con.commit()

