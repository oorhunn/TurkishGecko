from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:mt98mxb9r2@localhost:5432/duruh')
Session = sessionmaker(bind=engine)

Base = declarative_base()
