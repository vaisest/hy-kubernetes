from fastapi import FastAPI
# from pathlib import Path

app = FastAPI()
# state_file = Path("./pings.txt")
# if not state_file.exists() or not state_file.read_text():
#     state_file.write_text("0")
app.state.pings = 0


@app.get("/")
async def do_something():
    res = {"pings": app.state.pings}
    app.state.pings += 1
    return res


@app.get("/pings")
async def get_pings():
    return {"pings": app.state.pings}


# @app.get("/")
# async def hc():
#     return {"status": "ok"}
