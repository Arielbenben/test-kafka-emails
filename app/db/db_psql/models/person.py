from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.db_psql.models import Base



class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    ip_address = Column(String, nullable=False)
    created_at = Column(String, nullable=False)
    # location_id = Column(Integer, ForeignKey('location.id'))
    # device_info_id = Column(Integer, ForeignKey('device_info.id'))

    suspicious_explosive_content = relationship('SuspiciousExplosiveContent', back_populates='person')
    suspicious_hostage_content = relationship('SuspiciousHostageContent', back_populates='person')
    location = relationship('Location', back_populates='person', uselist=False)
    device_info = relationship('DeviceInfo', back_populates='person', uselist=False)


    def __repr__(self):
        return f"""Person: id:{self.id}, username:{self.username}, email: {self.email}, ip_address: {self.ip_address},
                    created_at:{self.created_at}, location_id:{self.location_id}, device_info_id:{self.device_info_id} """