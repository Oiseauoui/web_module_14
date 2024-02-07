import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from unittest.mock import Mock, patch
from src.repository.users import (
    get_user_by_email,
    create_user,
    update_token,
    confirmed_email,
    update_avatar_url,
)
from src.entity.models import User
from src.schemas.user import UserSchema
from src.database.db import get_db

# Мокований об'єкт бази даних для використання в тестах
@pytest.fixture
def mock_db():
    return Mock(spec=AsyncSession)

# Тест для функції отримання користувача по email
@pytest.mark.asyncio
async def test_get_user_by_email(mock_db):
    email = "test@example.com"
    expected_user = User(email=email)
    mock_db.execute.return_value.fetchone.return_value = expected_user

    user = await get_user_by_email(email, db=mock_db)

    assert user == expected_user

# Тест для функції створення користувача
@pytest.mark.asyncio
async def test_create_user(mock_db):
    user_data = {"email": "test@example.com", "username": "testuser", "password": "password"}
    user_schema = UserSchema(**user_data)
    avatar_url = "http://example.com/avatar.jpg"

    with patch("src.repository.users.Gravatar") as mock_gravatar:
        mock_gravatar_instance = mock_gravatar.return_value
        mock_gravatar_instance.get_image.return_value = avatar_url

        created_user = await create_user(body=user_schema, db=mock_db)

    assert created_user.email == user_data["email"]
    assert created_user.avatar == avatar_url

# Тест для функції оновлення токена
@pytest.mark.asyncio
async def test_update_token(mock_db):
    user = User(email="test@example.com")
    token = "new_token"

    await update_token(user, token, db=mock_db)

    assert user.refresh_token == token

# Тест для функції підтвердження email
@pytest.mark.asyncio
async def test_confirmed_email(mock_db):
    email = "test@example.com"
    user = User(email=email, confirmed=True)

    await confirmed_email(email, db=mock_db)

    assert user.confirmed  # Перевіряємо, що властивість confirmed у користувача тепер True


# Тест для функції оновлення URL аватару
@pytest.mark.asyncio
async def test_update_avatar_url(mock_db):
    email = "test@example.com"
    url = "http://example.com/avatar.jpg"
    user = User(email=email)

    updated_user = await update_avatar_url(email, url, db=mock_db)

    assert updated_user.avatar == url
