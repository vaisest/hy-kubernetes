import uuid
from datetime import datetime
import fastapi

unique = str(uuid.uuid1())
app = fastapi.FastAPI()

@app.get("/")
def get_ts():
    return {"timestamp": datetime.now().isoformat(), "uuid": unique}