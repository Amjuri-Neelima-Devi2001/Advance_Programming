import mysql.connector
from MySqlAdvance.mysqlconnection import Connection
class CRUD_Operation(Connection):
    def __init__(self):
        super().__init__('localhost','root','Neelima@2001','myhcl',3306)
        self.cur=self.connect.cursor()
    def create_table(self):
        # self.data=data
        sql="create table mytable3(name varchar(50),age int,place varchar(100));"
        self.cur.execute(sql)
        self.connect.commit()
    def insert(self,data):
        self.data = data
        sql = "insert into mytable3 values(%s,%s,%s);"
        self.cur.execute(sql, (self.data))
        self.connect.commit()
        print("Data inserted successfully")
    def delete(self,data):
        self.data = data
        sql="delete from mytable3 where name=%s;"
        self.cur.execute(sql, (self.data,))
        self.connect.commit()
        print("Data deleted successfully")
    def selectrecord(self):
        # self.data = data
        sql="select * from mytable3;"
        self.cur.execute(sql,)
        result=self.cur.fetchall()
        return result
        print("selected")
    def update(self,data):
        self.data = data
        sql="update mytable3 set name=%s where age=%s;"
        self.cur.execute(sql, (self.data))
        self.connect.commit()
        print("Updated successfully")
try:
    obj=CRUD_Operation()
    print(obj.connect.is_connected())
except Exception as e:
    print(e)