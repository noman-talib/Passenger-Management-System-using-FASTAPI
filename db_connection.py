from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///passengers.db')
Base = declarative_base()

mysession = sessionmaker(bind=engine)

def get_db():
    db = mysession()
    try:
        yield db
    finally:
        db.close()