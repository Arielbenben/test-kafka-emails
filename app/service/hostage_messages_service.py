from app.repository.psql_repository.device_info_repository import insert_device_info_to_db
from app.repository.psql_repository.locatoin_repository import insert_location_to_db
from app.repository.psql_repository.messages_hostage_repository import insert_hostage_sentence_to_db
from app.repository.psql_repository.person_repository import insert_person_to_db, update_all_id_to_person
from app.utils.psql_sentences_utils import convert_data_to_person_model, \
    convert_data_to_location_model, convert_data_to_device_info_model, \
    convert_data_to_suspicious_hostage_content_model


def insert_hostage_messages_db(data: dict):
    person_model = convert_data_to_person_model(data)
    person_id = insert_person_to_db(person_model)
    location_model = convert_data_to_location_model(data['location'], person_id)
    location_id = insert_location_to_db(location_model)
    device_info_model = convert_data_to_device_info_model(data['device_info'], person_id)
    device_info_id = insert_device_info_to_db(device_info_model)
    sentences_model = convert_data_to_suspicious_hostage_content_model(data['sentences'], person_id)
    insert_hostage_sentence_to_db(sentences_model)
    update_all_id_to_person(location_id, device_info_id, person_id)
    return
