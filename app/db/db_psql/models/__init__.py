from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .person import Person
from .location import Location
from .device_info import DeviceInfo
from .suspicious_hostage_content import SuspiciousHostageContent
from .suspicious_explosive_content import SuspiciousExplosiveContent