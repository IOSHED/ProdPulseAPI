from src.infra.repository.tortoise_repository import TortoiseRepository
from src.infra.database.models.country import Country


class CountriesRepository(TortoiseRepository):
    model = Country
