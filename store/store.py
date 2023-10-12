
import sqlite3

def load_database () :
    global con
    global cur
    con = sqlite3.connect ("store\storeDatabase.db")
    cur = con.cursor ()

def show_menue () :
    print ("\n 1- Show store's products")
    print (" 2- Add new product ")
    print (" 3- Edit a products information ")
    print (" 4- Delete a product ")
    print (" 5- Exit \n")

def add () :
    global cur
    global con
    name = input (" Enter the name of new product : ")
    price = int ( input (" Enter price of new product : "))
    count = int ( input (" Enter number of new product : "))
    cur.execute (f"INSERT INTO products (Name , Price , Count) VALUES ('{name}' , {price} , {count})")
    con.commit ()

def edit () :
    ...

def delete () :
    ...

print ("\n Hello! Welcome to my store 😊")
print (" Loading ... ⏳")
load_database ()
print (" Data loaded ⌛")

while True :
    show_menue ()
    choice = input (" Enter what you want to do from the menue : ")
    if choice == "1" or choice == "Show store's products" :
        for data in cur.execute ("SELECT * FROM products ") :
            print ( data )
    
    elif choice == "2" or choice == "Add new product" :
        add ()

    elif choice == "3" or choice == "Edit a products information" :
        edit ()

    elif choice == "4" or choice == "Delete a product" :
        delete ()
    
    elif choice == "5" or choice == "Exit" :
        exit (0)

    else :
        print (" Your input doen't exist 😐")
        print (" Please enter a number from the menue 🙄")