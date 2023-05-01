from datetime import date
import connection
import select_data

today_time = date.today()
amt = int(input("Enter amount you want to Credit:"))
new_balance = select_data.bal + amt
id = select_data.uid
res1 = connection.cur.execute(""" UPDATE account SET balance=%s WHERE Account_NO=%s """, (new_balance, id))
date_val = date.today()

res2 = connection.cur.execute("INSERT INTO transaction (Transaction_No,Account_NO, Debit, Credit, Balance,Date) "
                              "VALUES (%s, %s, %s, %s, %s, %s)",
                              (0, id,"-",amt, new_balance, date_val))
print("New Balance:",new_balance)
connection.conn.commit()