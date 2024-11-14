from typing import List
from app.db.db_psql.database import session_maker
from app.db.db_psql.models.suspicious_hostage_content import SuspiciousHostageContent


def insert_hostage_sentence_to_db(sentences: List[SuspiciousHostageContent]):
    try:
        with session_maker() as session:
            for sentence in sentences:
                session.add(sentence)
                session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error inserting suspicious hostage content sentences info: {e}")
