import connection
uid = (input("Enter Your Account Number:"))
class name:
    def name(self):
        connection.cur.execute("select Account_Holder_Name from account where Account_No=%s", uid)
        res = connection.cur.fetchall()
        for cur in res:
            name = list(cur)
            Name = name[0]
            return Name

a=name()
Holder_Name=a.name()
# print(Holder_Name)

print(connection.cur.execute("select Account_Holder_Name from account where Account_No=%s", uid))
