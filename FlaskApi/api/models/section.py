from .base import db
from .base import BaseModel

class SectionModel(BaseModel):
    __tablename__ = "section"

    name = db.Column(db.String(250), nullable=False, comment="Section name")
    description = db.Column(db.Text(), default="", nullable=True, comment="Section description")
    parent_section_id = db.Column(
        db.Integer, db.ForeignKey("section.id"), comment="Parent section id"
    )
    parent_section = db.relationship("SectionModel")
