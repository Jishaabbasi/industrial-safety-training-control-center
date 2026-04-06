from sqlalchemy import Column, Integer, String
from database import Base


class TrainingSummary(Base):
    __tablename__ = "training_summary"

    id = Column(Integer, primary_key=True, index=True)
    topic = Column(String)
    summary = Column(String)


class WorkerBatch(Base):
    __tablename__ = "worker_batch"

    id = Column(Integer, primary_key=True, index=True)
    worker_group = Column(String)
    topic = Column(String)


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    worker_name = Column(String)
    status = Column(String)


class ExamResult(Base):
    __tablename__ = "exam_result"

    id = Column(Integer, primary_key=True, index=True)
    worker_name = Column(String)
    score = Column(Integer)
    result = Column(String)