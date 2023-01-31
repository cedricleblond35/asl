class User(db.Model, UserMixin):
    # Existing app uses email_address instead of email
    email_address = db.Column(db.String(255), nullable=False, unique=True)
    # Map email property to email_address column
    email = db.Column('email', db.String(255), nullable=False, unique=True)

    # define email getter
    @property
    def email(self):
        return self.email_address   # on user.email: return user.email_address

    # define email setter
    @email.setter
    def email(self, value):
        self.email_address = value  # on user.email='xyz': set user.email_address='xyz'