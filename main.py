from fastapi import FastAPI
from agents import primary_agent
from database import engine, Base
import models
from database import SessionLocal
from models import TrainingSummary, WorkerBatch, Attendance, ExamResult

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/run")
def run_system(input_text: str):
    result = primary_agent(input_text)
    return {"result": result}

@app.get("/records")
def get_records():
    db = SessionLocal()

    summaries = db.query(TrainingSummary).all()
    batches = db.query(WorkerBatch).all()
    attendance = db.query(Attendance).all()
    exams = db.query(ExamResult).all()

    db.close()

    return {
        "summaries": [s.summary for s in summaries],
        "batches": [b.worker_group for b in batches],
        "attendance": [a.worker_name + " - " + a.status for a in attendance],
        "exam_results": [e.worker_name + " - " + e.result for e in exams]
    }