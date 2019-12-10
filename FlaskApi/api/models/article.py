from .base import db
from .base import BaseModel

class ArticleModel(BaseModel):
    __tablename__ = "article"

    # TODO: id a to_dict je jak u článků, sekcí atd. nedalo by se toto "vytknout" a zobecnit?

    title = db.Column(db.String(250), nullable=False, comment="Article title")
    content = db.Column(db.String(250), nullable=False, comment="HTML content of article")
    section_id = db.Column(
        db.Integer, db.ForeignKey("section.id"), comment="Section id"
    )
    section = db.relationship("SectionModel")
