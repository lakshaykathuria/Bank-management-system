import connection

class address:
    import name
    def address(self):
        connection.cur.execute("select Address from account where Account_No=%s", address.name.uid)
        res = connection.cur.fetchall()
        for cur in res:
            add = list(cur)
            Add = add[0]
            return Add

c=address()
address=c.address()

