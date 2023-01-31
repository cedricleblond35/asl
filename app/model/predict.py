from model.dbQuery import dbQuery
from model.letter import Letter
class Predict():
    def __init__(self):
        self.db = dbQuery()

    def create(self, letter, score,email , imageUpload, landmarks):
        print('**************************************predict model')
        user_id = self.selectIdByEmail(email)
        print('user_id :', user_id)
        l = Letter()
        letters_id = l.read(letter)
        print('letters_id :', letters_id)

        query = 'INSERT INTO prediction (letter, score, user_id, letters_id) VALUES (%s, %s, %s, %s)'
        arg = (letter, score, user_id, letters_id)
        return self.db.insert(query, arg)

    def selectIdByEmail(self, email):
        requet = 'SELECT id FROM user WHERE email="' + email + '"'
        r = self.db.fetchone(requet)
        return r[0]