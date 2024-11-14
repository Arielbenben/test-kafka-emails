from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.db_psql.models import Base
from app.settings.psql_config import PSQL_DB_URL


engine = create_engine(PSQL_DB_URL)

session_maker =sessionmaker(bind=engine)


def init_db():
    Base.metadata.create_all(engine)