from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.db_psql.models import Base



class SuspiciousHostageContent(Base):
    __tablename__ = 'suspicious_hostage_content'
    id = Column(Integer, primary_key=True, autoincrement=True)
    sentence = Column(String, nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))

    person = relationship('Person', back_populates='suspicious_hostage_content')

    def __repr__(self):
        return f'Suspicious Hostage Content: id:{self.id}, sentence:{self.sentence}, person_id: {self.person_id}'

    def to_dict(self):
        return {
            'id': self.id,
            'sentence': self.sentence,
            'person_id': self.person_id
        }