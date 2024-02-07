import pytest
from datetime import datetime, timedelta
from src.services.auth import Auth

@pytest.mark.asyncio
async def test_create_access_token():
    auth = Auth()
    data = {"sub": "test@example.com"}
    expires_delta = 3600  # token expires in 1 hour
    access_token = await auth.create_access_token(data, expires_delta)

    # Ensure that the access token is not None
    assert access_token is not None
