from datetime import datetime, timedelta
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String, DateTime,Float

from ..database import db
from ..mixins import CRUDModel

class Maso(CRUDModel):
    __tablename__ = 'maso'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True )
    typ = Column(Integer, nullable=False, index=False)#1=hovezi,2=vepr,3=kure
    cast = Column(Integer, nullable=False, index=True)#1=predni,2=zadni
    cena = Column(Float, nullable=True,default=0)
    # Use custom constructor
    # pylint: disable=W0231
    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

