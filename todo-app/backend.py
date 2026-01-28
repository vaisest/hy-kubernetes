from fastapi import Depends, FastAPI, Form, Request
from typing import Annotated, Sequence
from fastapi.responses import RedirectResponse, JSONResponse
import os

from sqlmodel import Field, Session, SQLModel, create_engine, select

app = FastAPI()

pg_user = os.environ["POSTGRES_USER"]
pg_pass = os.environ["POSTGRES_PASSWORD"]
psql_url = f"postgresql://{pg_user}:{pg_pass}@pg-svc"

engine = create_engine(psql_url)


class Todo(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None)
    content: str = Field(nullable=False)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/todos")
async def do_something(session: SessionDep) -> Sequence[Todo]:
    return session.exec(select(Todo)).all()


@app.post("/todos")
async def add_something(
    content: Annotated[str, Form()], session: SessionDep
) -> RedirectResponse:
    session.add(Todo(content=content))
    session.commit()
    return RedirectResponse(url="/", status_code=303)
