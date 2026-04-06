# AI-Based Industrial Safety Training Control Center

## Problem Statement

Industrial safety training is often managed manually, making attendance tracking, worker assessment, and retraining difficult when worker count is high.

## Solution

This project uses a multi-agent workflow to automate safety training coordination.

## Agents Used

* Summary Agent: stores training summary
* Batch Agent: divides workers into batches
* Attendance Agent: records attendance
* Exam Agent: evaluates pass/fail

## Technology Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite

## How to Run

1. Install dependencies
   pip install -r requirements.txt

2. Start server
   python -m uvicorn main:app --reload

3. Open browser
   http://127.0.0.1:8000/docs
