from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from datetime import datetime, timedelta
import requests
import base64


app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.state.placeholder_img = Path("./cache/placeholder.jpg")
app.state.placeholder_ts = Path("./cache/placeholder.txt")


def update_img():
    req = requests.get("https://picsum.photos/450")
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


@app.get("/", response_class=HTMLResponse)
async def do_something(request: Request):
    res = templates.TemplateResponse(
        request=request,
        name="main.j2",
        context={
            "image_data": base64.b64encode(
                app.state.placeholder_img.read_bytes()
            ).decode("utf-8")
        },
    )
    check_img()
    return res
