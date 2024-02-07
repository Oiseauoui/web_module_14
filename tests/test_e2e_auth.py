from unittest.mock import Mock

import asyncio
import pytest
from sqlalchemy import select
from src.entity.models import User
from tests.conftest import TestingSessionLocal
from src.conf import messages

user_data = {"username": "agent007", "email": "agent007@gmail.com", "password": "12345678"}


async def keyboard_interrupt():
    raise KeyboardInterrupt

async def system_exit():
    raise SystemExit

async def task_groups():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(system_exit())
        tg.create_task(keyboard_interrupt())

def test_validation_error_login(client):
    response = client.post("/api/auth/login",
                           data={"password": user_data.get("password")})
    assert response.status_code == 422, response.text
    data = response.json()
    assert "detail" in data
