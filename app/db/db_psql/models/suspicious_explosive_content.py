from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.db_psql.models import Base



class SuspiciousExplosiveContent(Base):
    __tablename__ = 'suspicious_explosive_content'
    id = Column(Integer, primary_key=True, autoincrement=True)
    sentence = Column(String, nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))

    person = relationship('Person', back_populates='suspicious_explosive_content')

    def __repr__(self):
        return f'Suspicious Explosive Content: id:{self.id}, sentence:{self.sentence}, person_id: {self.person_id}, person: {self.person}'