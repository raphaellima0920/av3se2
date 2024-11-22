from app import db

class User(db.Model):
    __tablename__ = 'tb_rds_user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    company_id = db.Column(db.Integer, db.ForeignKey('tb_rds_company.id'), nullable=False)
def __repr__(self):
    return f'<User {self.name}>'