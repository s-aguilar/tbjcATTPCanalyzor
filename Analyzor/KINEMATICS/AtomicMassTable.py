import sqlite3 as lite
def GetElement(tbjcZ=0, tbjcA=0):
    con = lite.connect('Analyzor/KINEMATICS/AtomicMassTable.db')

    with con:
        cur = con.cursor()
        SQLquery = "select * from AtomicMassTable where A="+str(tbjcA)+" and Z="+str(tbjcZ)+";"
        try:
            cur.execute(SQLquery)
            row = cur.fetchone()
            return row
        except Exception:
            print ("********************************")
            print (SQLquery)
            print ("SQL query error, try again")
            print ("********************************")
