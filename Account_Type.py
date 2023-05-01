import connection

class type:
    import name
    def type(self):
        connection.cur.execute("select Type_Of_Account from account where Account_No=%s", type.name.uid)
        res = connection.cur.fetchall()
        for cur in res:
            acc = list(cur)
            Type = acc[0]
            return Type

d=type()
type=d.type()

