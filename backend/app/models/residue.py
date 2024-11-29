from app import db

class Residue(db.Model):
    __tablename__ = 'tb_rds_residue'

    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(120), nullable=False)
    type = db.Column(db.String(120), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    current_total = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    user_id = db.Column(db.Integer, db.ForeignKey('tb_rds_user.id'), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('tb_rds_company.id'), nullable=False)

    def to_dict(self):
        return{
            "id": self.id,
            "item": self.item,
            "type": self.type,
            "capacity": self.capacity,
            "current_total": self.current_total,
            "created_at": self.created_at,
            "user_id": self.user_id,
            "company_id": self.company_id
        }
def __repr__(self):
    return f'<Residue {self.name}>'