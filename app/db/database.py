from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker



DATABASE_URL = (
   'postgresql://postgres:1512@localhost:5432/menu_app'
)

engine = create_engine(DATABASE_URL)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    session = Session()
    Base.metadata.create_all(engine)
    try:
        yield session
    finally:
        session.close()