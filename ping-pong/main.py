from fastapi import FastAPI

app = FastAPI()
app.state.pings = 0

@app.get("/pingpong")
async def do_something():
    app.state.pings += 1
    return {"pings": app.state.pings }
