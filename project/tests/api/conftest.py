import pytest
from testcontainers.postgres import PostgresContainer
from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI
from httpx import AsyncClient

from yourapp.main import app as fastapi_app

@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"

@pytest.fixture(scope="session")
def postgres_container():
    with PostgresContainer("postgres:15") as postgres:
        yield postgres  # starts/stops container automatically

@pytest.fixture(scope="function")
async def test_app(postgres_container):
    db_url = postgres_container.get_connection_url().replace("postgresql://", "postgres://")  # Tortoise expects this

    register_tortoise(
        fastapi_app,
        db_url=db_url,
        modules={"models": ["yourapp.models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )

    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        yield ac

    # Cleanup: truncate all tables
    from tortoise import Tortoise
    for model in Tortoise.apps.get("models").values():
        await model.all().delete()
