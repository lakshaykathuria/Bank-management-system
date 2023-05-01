import connection

name = input("Enter Your Name:")
phone = input("Enter Your Phone NO:")
add = input("Enter Your Address:")
type = input("Enter The Type Of Account:")
balance = input("Enter The Opening Balance(Min=5000):")
sql = "insert into Account(Account_Holder_Name,Phone_NO,Account_NO,Address,Type_Of_Account,Balance) " \
      "Values(%s,%s,%s,%s,%s,%s)"
val = (name,phone,0,add,type,balance)
connection.cur.execute(sql,val)
connection.conn.commit()
print("Account Created Successfully")
