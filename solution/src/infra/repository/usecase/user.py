from src.infra.database.models.user import User
from src.infra.repository.tortoise_repository import TortoiseRepository


class UserRepository(TortoiseRepository):
    model = User
