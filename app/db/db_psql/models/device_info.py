from sqlalchemy import Column, Integer, String, ForeignKey,Float
from sqlalchemy.orm import relationship
from app.db.db_psql.models import Base



class DeviceInfo(Base):
    __tablename__ = 'device_info'
    id = Column(Integer, primary_key=True, autoincrement=True)
    browser = Column(String, nullable=False)
    os = Column(String, nullable=False)
    device_id = Column(String, nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))

    person = relationship('Person', back_populates='device_info', uselist=False)

    def __repr__(self):
        return (f"""DeviceInfo: (id={self.id}, browser='{self.browser}', os='{self.os}',
                "device_id='{self.device_id}', person_id={self.person_id}, person={self.person})"""
        )


