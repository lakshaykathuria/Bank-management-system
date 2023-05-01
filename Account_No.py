import connection
import Create_Account
connection.cur.execute("select Account_NO from account where Phone_NO=%s", Create_Account.phone)
res = connection.cur.fetchall()
for cur in res:
        Account_No = list(cur)
acc = Account_No[0]
print("Your Account No:",acc)
