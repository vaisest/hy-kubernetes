from fastapi import FastAPI, Form, Request
from typing import Annotated
from fastapi.responses import RedirectResponse, JSONResponse

app = FastAPI()

app.state.todos = []


@app.get("/todos")
async def do_something() -> JSONResponse:
    return app.state.todos


@app.post("/todos")
async def add_something(content: Annotated[str, Form()]) -> RedirectResponse:
    app.state.todos.append({"content": content})
    return RedirectResponse(url="/", status_code=303)
