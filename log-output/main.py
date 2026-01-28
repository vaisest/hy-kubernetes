import uuid
import fastapi
import pathlib
import requests

unique = str(uuid.uuid1())
app = fastapi.FastAPI()
dest_file = pathlib.Path("./files/data.txt")


def get_ping_count():
    req = requests.get("http://ping-pong-svc:1234/pings")
    return req.json()["pings"]


@app.get("/")
def get_ts():
    pings = get_ping_count()
    return {"data": dest_file.read_text(), "ping-pongs": pings}
