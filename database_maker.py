import mysql.connector as db
def connection(x):
    database=""
    con=db.connect(host="localhost",user="root",passwd="2468")
    cur=con.cursor()
    cur.execute("show databases")
    q=cur.fetchall()
    if x in q:
        database=x
    else:    
        try:
            cur.execute("create database "+x)    
            con.commit()
            cur.execute("use "+x)
        except Exception:
            print("Database alredy exist")    
connection("manas")    
manass was a good boy
gsj was jhlhdjl 