from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from core.database import SessionLocal

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def main():
    return {"message": "Hello World."}
