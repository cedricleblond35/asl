from model.admin import Admin

# https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-execute.html
# https://tutswiki.com/read-write-config-files-in-python/
class User(Admin):
    def __init__(self):
        Admin.__init__(self)        
    
    def create(self,  name, lastname, email, pwd, role):
        return super().createUser(self,  name, lastname, email, pwd, role)
    
    def updateUser(self,  name, lastname, email, pwd):
        return super().updateUser(self,  name, lastname, email, pwd, 2)
