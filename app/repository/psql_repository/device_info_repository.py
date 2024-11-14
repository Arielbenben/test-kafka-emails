from app.db.db_psql.database import session_maker
from app.db.db_psql.models.device_info import DeviceInfo


def insert_device_info_to_db(device_info: DeviceInfo):
    try:
        with session_maker() as session:
            session.add(device_info)
            session.commit()
            return device_info.id
    except Exception as e:
        session.rollback()
        print(f"Error inserting device info: {e}")
    return

