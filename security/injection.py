# security/injection.py

import mysql.connector  # type: ignore # 기본 MySQL 연결
from sqlalchemy import createengine, Column, Integer, String, Float, DateTime  # type: ignore 
from sqlalchemy.ext.declarative import declarativebase # type: ignore
from sqlalchemy.orm import sessionmaker # type: ignore

def createconnection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="rootpassword",
        database="StudyApp"
    )


DATABASEURL = "mysql+mysqlconnector://root:rootpassword@127.0.0.1/StudyApp"


engine = createengine(DATABASEURL)


Base = declarativebase()


class Subject(Base):
    tablename = 'subjects'

    id = Column(Integer, primarykey=True, autoincrement=True)
    name = Column(String(50))
    age = Column(Integer)

    def repr(self):
        return f"<Subject(name={self.name}, age={self.age})>"

class EEGData(Base):
    __tablename = 'eeg_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    subject_id = Column(Integer)
    data = Column(String(255))
    timestamp = Column(DateTime)

class FocusScore(Base):
    __tablename = 'focus_scores'

    id = Column(Integer, primary_key=True, autoincrement=True)
    subject_id = Column(Integer)
    score = Column(Float)
    timestamp = Column(DateTime)

class HRVData(Base):
    __tablename = 'hrv_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    subject_id = Column(Integer)
    hrv = Column(Float)
    timestamp = Column(DateTime)

class StudyLog(Base):
    __tablename = 'study_logs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    subject_id = Column(Integer)
    log = Column(String(255))
    timestamp = Column(DateTime)

class User(Base):
    __tablename = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50))
    password = Column(String(255))

Session = sessionmaker(bind=engine)