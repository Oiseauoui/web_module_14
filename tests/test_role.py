import pytest
from fastapi import HTTPException, status

from src.entity.models import User, Role
from src.services.roles import RoleAccess
from unittest.mock import Mock

@pytest.fixture
def mock_auth_service():
    auth_service = Mock()
    auth_service.get_current_user.return_value = User(role=Role.ADMIN)
    return auth_service



@pytest.mark.asyncio
async def test_role_access_forbidden(mock_auth_service):
    allowed_roles = [Role.MODERATOR.value]
    role_access = RoleAccess(allowed_roles)
    request = Mock()

    # Assuming user with ADMIN role is authenticated
    with pytest.raises(HTTPException) as exc_info:
        await role_access(request, user=mock_auth_service.get_current_user())

    assert exc_info.value.status_code == status.HTTP_403_FORBIDDEN
    assert exc_info.value.detail == "FORBIDDEN"
