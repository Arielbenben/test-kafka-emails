from typing import List
from app.db.db_psql.database import session_maker
from app.db.db_psql.models.suspicious_explosive_content import SuspiciousExplosiveContent


def insert_explosive_sentence_to_db(sentences: List[SuspiciousExplosiveContent]):
    try:
        with session_maker() as session:
            for sentence in sentences:
                session.add(sentence)
                session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error inserting explosive sentence: {e}")

