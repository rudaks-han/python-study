from fastapi import FastAPI  # FastAPI import

app = FastAPI()
@app.get("/")
def home():
    return "home"

@app.get("/users/{user_id}")
def printJson():
    return "path variable"

@app.get("/users/hong")
def printJson():
    return "hong"

