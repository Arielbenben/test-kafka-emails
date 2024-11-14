from typing import List
from sqlalchemy.exc import SQLAlchemyError
from app.db.db_psql.database import session_maker
from app.db.db_psql.models.person import Person
from app.db.db_psql.models import SuspiciousHostageContent


def insert_hostage_sentence_to_db(sentences: List[SuspiciousHostageContent]):
    try:
        with session_maker() as session:
            for sentence in sentences:
                session.add(sentence)
                session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error inserting suspicious hostage content sentences info: {e}")



def get_suspicious_hostage_content_by_email(email: str):
    try:
        with session_maker() as session:
            person = session.query(Person).filter(Person.email == email).first()
            if not person:
                return None

            suspicious_content = session.query(SuspiciousHostageContent.sentence) \
                .join(Person, SuspiciousHostageContent.person_id == Person.id) \
                .filter(Person.id == person.id) \
                .all()
            return [content.sentence for content in suspicious_content]
    except SQLAlchemyError as e:
        print(f'Error: {e}')
        return


def get_all_hostage_sentences():
    with session_maker() as session:
        return session.query(SuspiciousHostageContent).all()