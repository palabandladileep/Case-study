from service import task
from dao import taskdao
from prettytable import PrettyTable

while(1):
    x=taskdao.takeinput()
    if(x):
        taskdao.run(x)
    else:
        break
print("Exiting.....\nAll changes are commited successfully..")