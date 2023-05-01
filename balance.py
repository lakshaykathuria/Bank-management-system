import connection

class balance:
    import name
    def balance(self):
        connection.cur.execute("select Balance from account where Account_No=%s", balance.name.uid)
        res = connection.cur.fetchall()
        for cur in res:
            bal = list(cur)
            Bal = bal[0]
            return Bal

e=balance()
balance=e.balance()

