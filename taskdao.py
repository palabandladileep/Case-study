from service.dbconnection import connectdb
from service import task
import time
from prettytable import PrettyTable
def welcome():
    t=PrettyTable(['WELCOME TO TASK TRACKER'])
    t.add_row(['Database Connection Status:Connected'])
    t.add_row([''])
    t.add_row(['USER==root DATABASE==casestudy'])
    print(t)

def run(op):#getting object as para
    welcome()
    if (op==1):
        taskid = 1020
        taskname = 'web'
        description = 'js'
        status = 'completed'
        priority = 2
        notes = 'some notes'
        bookmark = 'bookm1'
        ownerid = 115
        creatorid = 225
        createdon = '2021-02-03'
        modifiedon = '2021-02-14'
        tsk = task.Task(taskid, taskname, description, status, priority, notes, bookmark, ownerid, creatorid, createdon,modifiedon)
        dbconnect.insert(tsk)
    elif(op==2):
        print("DELETION")
        x=int(input("Enter Task id to delete: "))
        dbconnect.deleterow(x)
    elif(op==3):
        dbconnect.showtableval()
    elif(op==4):
        id=int(input("Enter taskid(Int): "))
        pr=int(input("Enter Priority(Range[1-5]): "))
        dbconnect.prioritize(pr,id)
    elif(op==5):
        id = int(input("Enter taskid(Int): "))
        note=str(input("Enter Notes to add: "))
        bm=str(input("Enter Bookmark to add: "))
        dbconnect.addbooknotes(note,bm,id)
    elif(op==6):
        id = int(input("Enter taskid(Int): "))
        dbconnect.searchtasks(id)
    elif(op==7):
        dbconnect.trackcomp()
    else:
        print("Invalid Input.\nTry again...")
        return 0
def takeinput():
    print("""
+=========================================================================================================================================================================+    
        """)
    t=PrettyTable(['Select Your Choice '])
    t.add_row(['  1]Add Values           '])
    t.add_row(['  2]Delete Value         '])
    t.add_row(['  3]Display Table        '])
    t.add_row(['  4]Prioritize           '])
    t.add_row(['  5]Add Notes & Bookmarks'])
    t.add_row(['  6]Search Tasks         '])
    t.add_row(['  7]Track Completion     '])
    t.add_row(['  0]Exit/close           '])
    print(t)
    op = int(input("Enter your choice: "))
    return op


