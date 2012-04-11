import sys
import DbHelper
from Settings import Settings

class MigrateAction:

    def readFile(self, number):
        f = open(str(number).zfills(5) + ".sql", 'r')
        return f.read()

    def perform(self, args):
        settings = Settings()
        try:
            conn = DbHelper.createConnection(settings)
            start = DbHelper.getDbVersion(conn)
            max = sys.maxint

            if settings.version != 'last':
                max = int(settings.version)

            current = start
            while current <= max:
                query = readFile(current)
                DbHelper.execute(conn, query)
                current += 1
            print max
        finally:
            conn.close()


ma = MigrateAction()
ma.perform(None)