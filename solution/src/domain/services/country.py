from typing import Any, List
from src.infra.database.exception import DBDoesNotExistException
from src.domain.exception.service_exception import CountryDoesNotExists
from src.infra.repository.usecase.country import CountriesRepository
from domain.shemas.database.country import CountrySchema


class CountriesService:
    def __init__(self) -> None:
        self.repo = CountriesRepository()

    async def get_countries(
        self, order_by: str = "alpha2", order_desc: bool = False
    ) -> List[CountrySchema]:
        countries = await self.repo.find_all(order_by=order_by, order_desc=order_desc)
        return [await CountrySchema.from_tortoise_orm(country) for country in countries]

    async def get_countries_by_region(
        self,
        regions: List[str],
        order_by: str = "alpha2",
        order_desc: bool = False,
    ) -> List[CountrySchema]:
        countries = await self.repo.find_where(
            order_by=order_by, order_desc=order_desc, region__in=regions
        )
        return [await CountrySchema.from_tortoise_orm(country) for country in countries]

    async def get_country_by(
        self,
        **filters: Any,
    ) -> List[CountrySchema]:
        try:
            country = await self.repo.find_one(**filters)
        except DBDoesNotExistException:
            raise CountryDoesNotExists
        return await CountrySchema.from_tortoise_orm(country)
