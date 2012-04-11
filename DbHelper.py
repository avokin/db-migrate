import pymssql

def createConnection(settings):
    pymssql.connect(host=settings.host, user=settings.user, password=settings.password, database=settings.schema)

def getDbVersion(conn):
        cur = conn.cursor()
        cur.execute("SELECT TOP 1 * FROM VERSION")

        row = cur.fetchone()
        if row:
            return row[0]
        else:
            raise RuntimeError("No data in the 'version' table")

def execute(conn, query):
    conn.cursor().execute(query)

