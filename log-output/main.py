import uuid
from datetime import datetime
import fastapi
import pathlib

unique = str(uuid.uuid1())
app = fastapi.FastAPI()
dest_file = pathlib.Path("./files/data.txt")
pings_file = pathlib.Path("./files/pings.txt")

@app.get("/")
def get_ts():
    return {"data": dest_file.read_text(), "ping-pongs": pings_file.read_text()}