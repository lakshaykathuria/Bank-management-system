#creating database
import pymysql
conn = pymysql.connect(host='localhost',user="root",password="")
cur = conn.cursor()
cur.execute("CREATE DATABASE bank")




account= "CREATE TABLE account (Account_NO bigint(20) PRIMARY KEY ,Account_Holder_Name varchar(30) ,Phone_NO bigint(20) ,Address longtext ,Type_Of_Account varchar(20) ,Balance int(11) );"

account_data="INSERT INTO account (Account_NO, Account_Holder_Name, Phone_NO, Address, Type_Of_Account,Balance) VALUES (%s, %s, %s, %s, %s,%s)" 

account_data_valuee=[
    ("58888263", "Lakshay", "9138229069", "Arya Nagar,Rohtak", "Saving", "45000"),
    ("58888264", "Anita", "9138536824", "Arya Nagar,Rohtak", "Saving", "21000"),
    ("58888265", "hgfhf", "574", "hgfj", "saving", "10000")]

transaction = "CREATE TABLE transaction ( Transaction_No int(11) NOT NULL, Account_NO bigint(20) NOT NULL,Debit int(11) NOT NULL, Credit int(11) NOT NULL, Balance int(11) NOT NULL, Date date DEFAULT NULL);"

transaction_data= "INSERT INTO transaction (Transaction_No, Account_NO, Debit, Credit, Balance, Date) VALUES(%s, %s, %s, %s, %s,%s)"

transaction_data_value=[
    ('0','58888263','10000','0','35000','2023-05-01'),
    ('0','58888265','0','20050','30050','2023-05-01'),
    ('0','58888264','0','5000','26000','2023-05-01'),
    ('0','58888263','4000','0','31000','2023-05-01'),
    ('0','58888264','0','6352','32352','2023-05-01')
    ]

import connection
connection.cur.execute(account)
connection.cur.executemany(account_data,account_data_valuee)
connection.cur.execute(transaction)
connection.cur.executemany(transaction_data,transaction_data_value)
connection.conn.commit()
