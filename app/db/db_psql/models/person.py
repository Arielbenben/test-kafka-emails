from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.db_psql.models import Base



class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    ip_address = Column(String, nullable=False)
    created_at = Column(String, nullable=False)

    suspicious_explosive_content = relationship('SuspiciousExplosiveContent', back_populates='person')
    suspicious_hostage_content = relationship('SuspiciousHostageContent', back_populates='person')
    location = relationship('Location', back_populates='person', uselist=False)
    device_info = relationship('DeviceInfo', back_populates='person', uselist=False)


    def __repr__(self):
        return f"""Person: id:{self.id}, username:{self.username}, email: {self.email}, ip_address: {self.ip_address},
                    created_at:{self.created_at}, location: {self.location}, device_info: {self.device_info} """

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'ip_address': self.ip_address,
            'created_at': self.created_at,
            'suspicious_explosive_content': [content.to_dict() for content in self.suspicious_explosive_content],
            'suspicious_hostage_content': [content.to_dict() for content in self.suspicious_hostage_content],
            'location': self.location.to_dict(),
            'device_info': self.device_info.to_dict()
        }