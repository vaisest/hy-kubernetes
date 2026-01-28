from fastapi import APIRouter, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from datetime import datetime, timedelta
import requests
import base64
import os


app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.state.placeholder_img = Path("./cache/placeholder.jpg")
app.state.placeholder_ts = Path("./cache/placeholder.txt")

backend_url = os.environ["BACKEND_URL"]
picsum_url = os.environ["PICSUM_URL"]


def update_img():
    req = requests.get(picsum_url)
    app.state.placeholder_img.write_bytes(req.content)
    app.state.placeholder_ts.write_text(datetime.now().isoformat())


def check_img():
    if not app.state.placeholder_img.exists():
        update_img()
    ts = datetime.fromisoformat(app.state.placeholder_ts.read_text())
    time_since = datetime.now() - ts
    if time_since > timedelta(minutes=10):
        update_img()


check_img()


def get_todos():
    req = requests.get(f"http://{backend_url}/todos")
    return req.json()


@app.get("/", response_class=HTMLResponse)
async def do_something(request: Request):
    todos = get_todos()

    page = templates.TemplateResponse(
        request=request,
        name="main.j2",
        context={
            "image_data": base64.b64encode(
                app.state.placeholder_img.read_bytes()
            ).decode("utf-8"),
            "todos": [todo["content"] for todo in todos],
        },
    )
    check_img()
    return page
