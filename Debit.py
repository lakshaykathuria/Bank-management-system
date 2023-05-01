from datetime import date
import connection
import select_data

today_time = date.today()
amt = int(input("Enter amount you want to Debit:"))
new_balance = select_data.bal - amt
id = select_data.uid
trans_type = "withdraw"
date_val = date.today()
if new_balance < 5000:
    print("Minimum balance exceeded")
else:
    res1 = connection.cur.execute(""" UPDATE account SET balance=%s WHERE Account_NO=%s """, (new_balance, id))
    res2 = connection.cur.execute("INSERT INTO transaction (Transaction_No, Account_NO, Debit,Credit, Balance, Date)"
                                  " VALUES (%s,%s, %s, %s, %s, %s)",
                                  (0,id, amt,"-",new_balance, date_val))
    print("New Balance:",new_balance)
    connection.conn.commit()