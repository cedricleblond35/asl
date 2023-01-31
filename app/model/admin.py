from model.dbQuery import dbQuery
import hashlib  # MD5
import re

# https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-execute.html
# https://tutswiki.com/read-write-config-files-in-python/

class Admin():
    def __init__(self):
        self.db = dbQuery()

    def identification(self, email, pwd):
        query = "SELECT name, email, role_id FROM user WHERE  email=%s AND password=%s"
        print(query)
        arg = (email, pwd)
        print(arg)
        return self.db.fetch(query, arg)

    def createUser(self,  name, lastname, email, pwd, role):
        name = name.strip()
        lastname = lastname.strip()
        email = email.strip()
        pwd = pwd.strip()

        if self.verifyName(name) and self.verifyEmail(email) and self.verifyPassword(pwd):
            pwd = hashlib.md5(pwd.encode()).hexdigest()
            query = 'INSERT INTO user (name, lastname, email, password, role_id) VALUES (%s, %s, %s, %s, %s)'
            arg = (name,lastname, email, pwd, role)
            return self.db.insert(query, arg)
        
        return False

    def updateUser(self):
        requete = 'UPDATE user SET name="%s", lastname="%s", email="%s", password="%s", role_id="%s" WHERE id ="%s"'
        pass

    def _deleteUser(self):
        query = 'DELETE FROM user WHERE id =%s'
        arg = (id)
        pass

    def selectUser(self):
        query = "SELECT u.name, u.lastname, u.email, r.name FROM user u RIGHT JOIN role r ON r.id = u.role_id"
        print(query)
        return self.db.fetch(query)

    def selectIdByEmail(self, email):
        r = "SELECT id FROM user WHERE email=%s"
        arg = ('adminasl@gmail.com')
        print(r)
        return self.db.fetchone(r,arg)

    def getRole(self):
        return self.db.fetch('SELECT id,name FROM role', '')

    def verifyName(self, name):
        pattern = re.compile("^[a-zA-Z]+(([-][a-zA-Z ])?[a-zA-Z]*)*$")
        return bool(pattern.match(name))
        
    def verifyEmail(self, email):
        pattern = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        return bool(pattern.match(email))
        
    def verifyPassword(self, password):
        pattern = re.compile(r'[A-Za-z0-9@#$%^&+=]{5,}')
        return bool(pattern.match(password))