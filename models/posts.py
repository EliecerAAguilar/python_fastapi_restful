from datetime import datetime
from config.desencrypt import DbConnection
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, Text, Boolean
from sqlalchemy import Table, Column

Base = declarative_base()
connection = DbConnection()
engine = connection.engine_connection()
meta = connection.meta


class Post(Base):
    __tablename__ = 'posts'
    id = Column(String(50), primary_key=True)
    title = Column(String(50), nullable=True)
    author = Column(String(50), nullable=True)
    content = Column(Text, nullable=True)
    created_at = Column(DateTime(), default=datetime.now())
    published_at = Column(DateTime(), default=datetime.now())
    published = Column(Boolean, default=False)

    def __str__(self):
        return self.author


Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
