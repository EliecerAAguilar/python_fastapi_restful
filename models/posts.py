from datetime import datetime
from config.desencrypt import DbConnection
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, Text
from sqlalchemy import Table, Column

Base = declarative_base()
connection = DbConnection()
engine = connection.engine_connection()
meta = connection.meta

# ---- pydantic model----------------------
# id: Optional[str]
# title: str
# author: str
# content: Text
# created_at: datetime = datetime.now()
# published_at: Optional[datetime]
# published: bool = False
#-------------------------------------------


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer(), primary_key=True)
    title = Column(String(50), nullable=True)
    author = Column(String(50), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(), default=datetime.now())
    published_at = Column(DateTime(), default=datetime.now())
    published = Column(DateTime(), default=datetime.now())

    def __str__(self):
        return self.author


Session = sessionmaker(engine)
session = Session()

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
