from app import db

class Company(db.Model):
    __tablename__ = 'tb_rds_company'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    workers = db.relationship('User', backref = 'Company', lazy=True)

def __repr__(self):
    return f'<Company {self.name}>'