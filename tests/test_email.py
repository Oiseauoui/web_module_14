import pytest
from unittest.mock import MagicMock

from fastapi_mail import MessageSchema, MessageType

from src.services.email import FastMail, send_email, send_password_reset_email


@pytest.fixture
def mock_fastmail(monkeypatch):
    mock_instance = MagicMock(spec=FastMail)
    mock_instance.conf = MagicMock()
    monkeypatch.setattr("src.services.email.FastMail", lambda conf: mock_instance)
    return mock_instance


async def test_send_email(mock_fastmail):
    email = "test@example.com"
    username = "testuser"
    host = "example.com"
    token = "test_token"

    await send_email(email, username, host)

    mock_fastmail.send_message.assert_called_once_with(
        MessageSchema(
            recipients=[email],
            template_body={"host": host, "username": username, "token": token},
            subtype=MessageType.html
        ),
        template_name="verify_email.html"
    )


async def test_send_password_reset_email(mock_fastmail):
    email = "test@example.com"
    username = "testuser"
    host = "example.com"
    token = "test_token"

    await send_password_reset_email(email, username, host, token)

    mock_fastmail.send_message.assert_called_once_with(
        MessageSchema(
            recipients=[email],
            template_body={"host": host, "username": username, "token": token},
            subtype=MessageType.html
        ),
        template_name="reset_password.html"
    )
