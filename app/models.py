from .extensions import db
from passlib.hash import bcrypt

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    def set_password(self, password):
        # Hash the password using bcrypt
        self.password_hash = bcrypt.hash(password)

    def check_password(self, password):
        # Verify password against stored hash
        return bcrypt.verify(password, self.password_hash)
