#this is db file
from prettytable import PrettyTable
import mysql.connector
import time
def connectdb():
    try:
        db = mysql.connector.connect(host="localhost", user="root", password="asus", database="python")
        curzor = db.curzor()
        return db,curzor
    except:print("Not Connected..\nTry Again")
db,curzor=connectdb()

def showtableval():
    print("Table Task>")
    y=curzor.execute("select * from task")
    x=curzor.fetchall()
    t = PrettyTable(['taskid','taskname','description','status','priority','notes','bookmark','ownerid','creatorid','createdon','modifiedon'])
    for i in x:
        t.add_row([i[0], i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]])
    print(t)
    curzor.execute("select Count(*) from task")
    x=str(curzor.fetchall())
    t1=PrettyTable(['Row count'])
    t1.add_row([x[2:len(x)-3]])
    print(t1)



def prioritize(priority,taskid):
    #db,curzor=connectdb()
    print("Prioritizing the tasks......")
    time.sleep(1)
    curzor.execute("update task set priority=%s where taskid=%s",(priority,taskid))
    db.commit()
    print("Successfully set the priority.\ntaskid:"+str(taskid)+"-->priority:"+str(priority))
    showtableval()

def addbooknotes(notes,bookmark,taskid):
    #db,curzor = connectdb()
    print("Adding Notes and Bookmarks")
    time.sleep(1)
    curzor.execute("UPDATE task SET notes=%s,bookmark=%s WHERE taskid=%s",(notes,bookmark,taskid))
    db.commit()
    print("Successfully added notes,bookmarks. ")
    showtableval()

def searchtasks(taskid):
    print("searching the Tasks.......")
    time.sleep(2)
    command=("select taskname from task where taskid=%s"%(taskid))
    data=(taskid)
    curzor.execute(command,data)
    x=str(curzor.fetchall())
    time.sleep(1)
    t=PrettyTable(['Task Name'])
    t.add_row([x[3:len(x)-4]])
    print(t)

def trackcomp():
    print("COMPLETED TASKS")
    curzor.execute("select taskname,taskid from task where stats='completed'")
    x=curzor.fetchall()
    t=PrettyTable(['Taskname','Task ID'])
    for i in x:
        t.add_row([i[0],i[1]])
    print(t)

def insert(tk):
    #db,curzor = connectdb()
    command = ("insert into task(taskid,taskname,descript,stats,priority,notes,bookmark,ownerid,creatorid,createdon,modifiedon)""values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    data = (tk.taskid, tk.taskname, tk.description, tk.status, tk.priority,tk.notes,tk.bookmark,tk.ownerid,tk.creatorid,tk.createdon,tk.modifiedon)
    curzor.execute(command, data)
    db.commit()
    time.sleep(2)
    print("Inserted Successfully..")
    showtableval()
