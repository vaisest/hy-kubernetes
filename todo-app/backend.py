import logging
import os
from typing import Annotated, Sequence

from fastapi import Depends, FastAPI, Form, HTTPException
from fastapi.logger import logger
from fastapi.responses import RedirectResponse
from sqlmodel import Field, Session, SQLModel, create_engine, select
from pydantic import ValidationError

logger = logging.getLogger("uvicorn.error")


app = FastAPI()

pg_user = os.environ["POSTGRES_USER"]
pg_pass = os.environ["POSTGRES_PASSWORD"]
psql_url = f"postgresql://{pg_user}:{pg_pass}@pg-svc"

engine = create_engine(psql_url)


class Todo(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None)
    content: str = Field(nullable=False, max_length=140)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


@app.get("/")
async def health():
    return "ok"


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/todos")
async def return_something(session: SessionDep) -> Sequence[Todo]:
    return session.exec(select(Todo)).all()


@app.post("/todos")
async def add_something(
    content: Annotated[str, Form()], session: SessionDep
) -> RedirectResponse:
    try:
        todo = Todo.model_validate(Todo(content=content))
    except ValidationError:
        raise HTTPException(status_code=400, detail="Validation of the Todo failed.")
    session.add(todo)
    session.commit()
    logger.info(f"Adding todo with content: '{content}'")
    return RedirectResponse(url="/", status_code=303)
