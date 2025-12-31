from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base, Session

DATABASE_URL = "postgresql://vote:vote123@localhost:5435/votedb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class Vote(Base):
    __tablename__ = "votes"
    choice = Column(String, primary_key=True)
    count = Column(Integer, default=0)


Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_votes(db: Session):
    for choice in ["짜장면", "짬뽕"]:
        if not db.query(Vote).filter(Vote.choice == choice).first():
            db.add(Vote(choice=choice, count=0))
    db.commit()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class VoteRequest(BaseModel):
    choice: str


@app.on_event("startup")
def startup():
    db = SessionLocal()
    init_votes(db)
    db.close()


@app.get("/api/votes")
def get_votes(db: Session = Depends(get_db)):
    rows = db.query(Vote).all()
    return {row.choice: row.count for row in rows}


@app.post("/api/vote")
def cast_vote(req: VoteRequest, db: Session = Depends(get_db)):
    vote = db.query(Vote).filter(Vote.choice == req.choice).first()
    if vote:
        vote.count += 1
        db.commit()
        return {"success": True}
    return {"success": False, "error": "Invalid choice"}
