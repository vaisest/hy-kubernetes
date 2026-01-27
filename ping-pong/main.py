from fastapi import FastAPI
from pathlib import Path

app = FastAPI()
state_file = Path("./files/pings.txt")
if not state_file.exists() or not state_file.read_text():
    state_file.write_text("0")

@app.get("/pingpong")
async def do_something():
    pings = int(state_file.read_text())
    state_file.write_text(str(pings + 1))
    return {"pings": pings }
