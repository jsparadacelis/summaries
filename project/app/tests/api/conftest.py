import pytest
from testcontainers.core.waiting_utils import wait_for_logs
from testcontainers.postgres import PostgresContainer

POSTGRES_IMAGE = "postgres:14"
POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "test_password"
POSTGRES_DATABASE = "test_database"
POSTGRES_CONTAINER_PORT = 5432


@pytest.fixture(scope="session")
def postgres_container() -> PostgresContainer:
    """
    Setup postgres container
    """
    postgres = PostgresContainer(
        image=POSTGRES_IMAGE,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        dbname=POSTGRES_DATABASE,
        port=POSTGRES_CONTAINER_PORT,
    )
    with postgres:
        wait_for_logs(
            postgres,
            r"UTC \[1\] LOG:  database system is ready to accept connections",
            10,
        )
        yield postgres
