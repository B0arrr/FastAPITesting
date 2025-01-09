from typing import Generator

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from starlette.testclient import TestClient

from app.main import app

engine = create_engine('sqlite:///test.db')


@pytest.fixture(scope="session")
def session() -> Generator:
    with Session(engine) as session:
        yield session


@pytest.fixture(scope="session")
def client() -> Generator:
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="session")
def init(db: Session):
    # things to do before tests

    db.query().all()
    yield
    # things to do after tests
    db.query().delete()
    db.commit()
