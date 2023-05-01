import connection

uid = (input("Enter Your Account No:"))
connection.cur.execute("select balance from account where Account_NO=%s", uid)
res = connection.cur.fetchall()
for cur in res:
        bal_list = list(cur)
bal = bal_list[0]
print("Current balance: ",bal)
