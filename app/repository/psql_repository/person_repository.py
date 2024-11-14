from app.db.db_psql.database import session_maker
from app.db.db_psql.models.person import Person


def insert_person_to_db(person: Person):
    try:
        with session_maker() as session:
            session.add(person)
            session.commit()
            return person.id
    except Exception as e:
        session.rollback()
        print(f"Error inserting device info: {e}")
    return


def update_all_id_to_person(location_id: int, device_info_id: int, person_id: int):
    try:
        with session_maker() as session:
            person = session.query(Person).filter(Person.id == person_id).first()
            if person is None:
                raise Exception(f"Person with id {person_id} not found.")
            person.location_id = location_id
            person.device_info_id = device_info_id
            session.commit()
            session.refresh(person)
            return person
    except Exception as e:
        session.rollback()
        print(f"Error updating person: {e}")