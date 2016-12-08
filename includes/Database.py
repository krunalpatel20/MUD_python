#
# Krunal Patel
# Database wrapper
#

# TODO find a python mysql dbc library and implement it here
class Database:
    db = None

    def __init__(self):
        self.con = None

    def getInstance(self):
        if Database.db==None:
            Database.db = Database()
        return Database.db

    def ExecQuery(self, sql):
        return sql

    def getObject(self):
        return self

    def getAssoc(self):
        return self

