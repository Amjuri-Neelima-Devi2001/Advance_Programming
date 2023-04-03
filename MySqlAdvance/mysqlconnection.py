import mysql.connector
class Connection():
    def __init__(self, host, username, password, database, port):
        self.hostname = host
        self.username = username
        self.password = password
        self.database = database
        self.port = port
        self.connect = mysql.connector.Connect(host=self.hostname, username=self.username, password=self.password,
                                               database=self.database, port=self.port)
        # self.cur=self.connect.cursor()
# try:
#     obj=Connection('localhost','root','Neelima@2001','myhcl',3306)
# except Exception as e:
#     print(e)
