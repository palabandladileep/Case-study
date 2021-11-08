
from service.dbconnection import getdbconnection

def create_task(task):
    mydb = getdbconnection()
    mycursor = mydb.cursor()
    sql = "insert into task(t_name, t_desc, t_status, t_priority, t_notes, t_bm, t_own_id, t_cr_id, crt_on, mod_on) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (task.t_name,task.t_desc,task.t_status, task.t_priority, task.t_notes, task.t_own_id, task.t_cr_id,task.crt_on,task.mod_on)
    mycursor.executed(sql,val)
    mydb.commit()
    mydb.close()

