from typing import List
from app.db.db_psql.models.device_info import DeviceInfo
from app.db.db_psql.models.location import Location
from app.db.db_psql.models.person import Person
from app.db.db_psql.models.suspicious_explosive_content import SuspiciousExplosiveContent
from app.db.db_psql.models.suspicious_hostage_content import SuspiciousHostageContent


def convert_data_to_person_model(data: dict):
    return Person(username=data['username'], email=data['email'], ip_address=data['ip_address'], created_at=data['created_at'])


def convert_data_to_device_info_model(data_di: dict, person_id: int):
    return DeviceInfo(browser=data_di['browser'], os=data_di['os'], device_id=['device_id'], person_id=person_id)


def convert_data_to_location_model(data_l: dict, person_id: int):
    return Location(latitude=data_l['latitude'], longitude=data_l['longitude'], city=data_l['city'], country=data_l['country'], person_id=person_id)


def convert_data_to_suspicious_explosive_content_model(data: List, person_id: int):
    sentences_model = []
    for sentence_data in data:
        sentence = SuspiciousExplosiveContent(sentence=sentence_data, person_id=person_id)
        sentences_model.append(sentence)
    return sentences_model


def convert_data_to_suspicious_hostage_content_model(data: List, person_id: int):
    sentences_model = []
    for sentence_data in data:
        sentence = SuspiciousHostageContent(sentence=sentence_data, person_id=person_id)
        sentences_model.append(sentence)
    return sentences_model
