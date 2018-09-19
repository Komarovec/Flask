from datetime import datetime, timedelta
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String, DateTime

from ..database import db
from ..mixins import CRUDModel

class Bydliste(CRUDModel):
    __tablename__ = 'Bydliste'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True )
    ulice = Column(String, nullable=False, index=False)
    hNumber = Column(String, nullable=False, index=False)
    mesto = Column(String, nullable=False, index=False)
    postal = Column(String, nullable=False, index=False)
    datum_insertu= Column(DateTime)



    # Use custom constructor
    # pylint: disable=W0231
    def __init__(self, **kwargs):
        self.datum_insertu = datetime.utcnow()
        for k, v in kwargs.iteritems():
            setattr(self, k, v)
    @staticmethod
    def find_by_prijmeni(prijmeni):
        return db.session.query(Bydliste).filter_by(Grussmann = prijmeni).all()

