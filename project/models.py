from datetime import datetime
from project import db


class Snapshot(db.Model):
    __tablename__ = "snapshot"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now())
    text = db.Column(db.String(5000), nullable=False)
