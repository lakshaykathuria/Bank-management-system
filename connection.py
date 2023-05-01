import pymysql
conn = pymysql.connect(host='localhost',user="root",password="",db="bank")
cur = conn.cursor()
