from database import SessionLocal
from models import TrainingSummary, WorkerBatch


def summary_agent(data):
    db = SessionLocal()

    new_summary = TrainingSummary(
        topic="PPE Safety",
        summary=data
    )

    db.add(new_summary)
    db.commit()
    db.close()

    return "Safety summary saved in database"


from models import WorkerBatch

def batch_agent(data):
    db = SessionLocal()

    topics = [
        "PPE Safety",
        "Fire Safety",
        "Electrical Safety",
        "Machine Safety",
        "Emergency Response"
    ]

    result = []

    worker_number = 1

    for i in range(5):
        batch_name = f"Batch {i+1}"

        batch = WorkerBatch(
            worker_group=batch_name,
            topic=topics[i]
        )

        db.add(batch)

        workers = []

        for j in range(30):
            workers.append(f"Worker {worker_number}")
            worker_number += 1

        result.append({
            "batch": batch_name,
            "topic": topics[i],
            "workers": workers
        })

    db.commit()
    db.close()

    return result

from models import Attendance


def attendance_agent(data):
    db = SessionLocal()

    workers = [
        ("Rahul", "Absent"),
        ("Amit", "Present"),
        ("Priya", "Absent")
    ]

    result = []

    for name, status in workers:
        record = Attendance(
            worker_name=name,
            status=status
        )
        db.add(record)

        if status == "Absent":
            result.append(f"{name} absent - retake required")
        else:
            result.append(f"{name} present")

    db.commit()
    db.close()

    return result


from models import ExamResult


def exam_agent(data):
    db = SessionLocal()

    exam_data = [
        ("Rahul", 82),
        ("Amit", 95),
        ("Priya", 88)
    ]

    result = []

    for name, score in exam_data:
        if score >= 90:
            status = "Pass"
            result.append(f"{name} passed")
        else:
            status = "Fail"
            result.append(f"{name} failed - retake exam required")

        exam = ExamResult(
            worker_name=name,
            score=score,
            result=status
        )

        db.add(exam)

    db.commit()
    db.close()

    return result

def primary_agent(user_input):
    responses = []

    if "summary" in user_input.lower():
        responses.append(summary_agent(user_input))

    if "workers" in user_input.lower():
        responses.append(batch_agent(user_input))

    if "attendance" in user_input.lower():
        responses.append(attendance_agent(user_input))

    if "exam" in user_input.lower():
        responses.append(exam_agent(user_input))

    return responses