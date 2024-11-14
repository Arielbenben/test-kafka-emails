from typing import List
from sqlalchemy.exc import SQLAlchemyError
from app.db.db_psql.database import session_maker
from app.db.db_psql.models.person import Person
from app.db.db_psql.models import SuspiciousExplosiveContent


def insert_explosive_sentence_to_db(sentences: List[SuspiciousExplosiveContent]):
    try:
        with session_maker() as session:
            for sentence in sentences:
                session.add(sentence)
                session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error inserting explosive sentence: {e}")



def get_suspicious_explosive_content_by_email(email: str):
    try:
        with session_maker() as session:
            person = session.query(Person).filter(Person.email == email).first()
            if not person:
                return None

            suspicious_content = session.query(SuspiciousExplosiveContent.sentence) \
                .join(Person, SuspiciousExplosiveContent.person_id == Person.id) \
                .filter(Person.id == person.id) \
                .all()
            return [content.sentence for content in suspicious_content]
    except SQLAlchemyError as e:
        print(f'Error: {e}')
        return


def get_all_explosive_sentences():
    with session_maker() as session:
        return session.query(SuspiciousExplosiveContent).all()


