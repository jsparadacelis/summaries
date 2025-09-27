from typing import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from project.app.main import app
from project.app.models.db import Base, get_db
from project.app.models.summary import TextSummary  # Import to register the model
from project.app.tests.factories import TextSummaryFactory


# Test database setup - using StaticPool to share in-memory database across connections
TEST_DATABASE_URL = "sqlite:///:memory:"
test_engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,  # Ensures all connections share the same in-memory database
)


@pytest.fixture(scope="function")
def db_session() -> Generator[Session, None, None]:
    """
    Create a fresh database session for each test.
    This fixture is for tests that need direct database access.
    """
    # Create all tables
    Base.metadata.create_all(bind=test_engine)

    # Create session
    TestingSessionLocal = sessionmaker(
        autocommit=False, autoflush=False, bind=test_engine
    )
    session = TestingSessionLocal()

    # Configure Factory Boy to use this session
    TextSummaryFactory._meta.sqlalchemy_session = session

    try:
        yield session
    finally:
        session.close()
        # Clean up tables
        Base.metadata.drop_all(bind=test_engine)


@pytest.fixture(scope="function")
def client(db_session: Session) -> Generator[TestClient, None, None]:
    """
    Create a test client for API tests.
    This fixture depends on db_session to ensure database is set up.
    """

    def get_test_db():
        """Override the get_db dependency to use our test database session"""
        try:
            yield db_session
        except:
            db_session.rollback()
            raise

    # Override the database dependency
    app.dependency_overrides[get_db] = get_test_db

    try:
        with TestClient(app) as test_client:
            yield test_client
    finally:
        # Clean up dependency override
        app.dependency_overrides.clear()
