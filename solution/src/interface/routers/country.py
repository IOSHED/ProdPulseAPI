from typing import Any, List
from fastapi import APIRouter, Depends, Path
from fastapi.params import Query

from src.domain.services.country import CountriesService
from src.domain.shemas.database.country import CountrySchema
from src.infra.database.models.country import Regions


router_country = APIRouter(prefix="/countries", tags=["countries"])


@router_country.get(
    "", summary="Получить список стран", response_model=List[CountrySchema]
)
async def _get_countries(
    сountries_service: CountriesService = Depends(CountriesService),
    region: List[Regions] = Query(None),
) -> Any:
    match region:
        case None:
            countries = await сountries_service.get_countries()
        case _:
            countries = await сountries_service.get_countries_by_region(region)
    return countries


@router_country.get(
    "/{alpha2}", summary="Получить страну по alpha2 коду", response_model=CountrySchema
)
async def _get_country_by_alpha2(
    сountries_service: CountriesService = Depends(CountriesService),
    alpha2: str = Path(example="RU"),
) -> Any:
    country = await сountries_service.get_country_by(alpha2=alpha2)
    return country
