from sqlalchemy import Column, Integer, String, ForeignKey,Float
from sqlalchemy.orm import relationship
from app.db.db_psql.models import Base



class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))

    person = relationship('Person', back_populates='location', uselist=False)

    def __repr__(self):
        return f""" Location: (id={self.id}, latitude={self.latitude}, longitude={self.longitude}, city='{self.city}',
                    country='{self.country}', person_id={self.person_id})"""

    def to_dict(self):
        return {
            'id': self.id,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'city': self.city,
            'country': self.country,
            'person_id': self.person_id,
        }