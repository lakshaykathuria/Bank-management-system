import connection

class phone:
    import name
    def phone(self):
        connection.cur.execute("select Phone_NO from account where Account_No=%s", phone.name.uid)
        res = connection.cur.fetchall()
        for cur in res:
            phn = list(cur)
            Phone = phn[0]
            return Phone

b=phone()
number=b.phone()

