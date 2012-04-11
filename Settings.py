import ConfigParser

class Settings:
    def __init__(self):
        cf = ConfigParser.ConfigParser()
        cf.read("db.properties")
        items = cf.items("db_defaults")
        for item in items:
            if item[0] == 'host':
                self.host = item[1]
            elif item[0] == 'user':
                self.user = item[1]
            elif item[0] == 'password':
                self.password = item[1]
            elif item[0] == 'schema':
                self.schema = item[1]
            elif item[0] == 'version':
                self.version = item[1]

