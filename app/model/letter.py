from model.dbQuery import dbQuery
class Letter():
    def __init__(self):
        self.db = dbQuery()

    def read(self, letter):
        print("lettre :", letter)
        query = 'SELECT id FROM letters WHERE  letter="'+letter+'"'

        return self.db.fetchone(query)[0]

    def readAll(self):
        query = 'SELECT * FROM letters'
        return self.db.fetch(query)