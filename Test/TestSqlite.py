import sqlite3 as sqlite


class Employee:

    def __init__(self,first,last,pay):
        self.first_name=first
        self.last_name=last
        self.pay=pay


connection = sqlite.connect("emplyee.db")
cursor=connection.cursor()

def insert_query(emp_obj):
    with connection:
        cursor.execute("Insert into employees values(:first,:last,:pay)",
                       {'first':emp_obj.first_name,'last':emp_obj.last_name,'pay':emp_obj.pay})

def select_values(emp_obj):
    cursor.execute("select * from employees where firstname=:first",{'first':emp_obj.first_name})
    return cursor.fetchall()

emp1=Employee('pk','yd',123)
insert_query(emp1)
print(select_values(emp1))

connection.close()