from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def do_something():
    print("hello from /")
