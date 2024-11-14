from sqlalchemy.orm import joinedload

from app.db.db_psql.database import session_maker
from app.db.db_psql.models.location import Location


def insert_location_to_db(location: Location):
    try:
        with session_maker() as session:
            session.add(location)
            session.commit()
            return location.id
    except Exception as e:
        session.rollback()
        print(f"Error inserting device info: {e}")
    return


def get_all_locations():
    with session_maker() as session:
        return session.query(Location).options(joinedload(Location.person)).all()

