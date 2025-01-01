from pydantic import constr
from tortoise.contrib.pydantic import pydantic_model_creator

from src.infra.database.models.country import Country


_CountryBaseSchema = pydantic_model_creator(Country, exclude=["id"])


class CountrySchema(_CountryBaseSchema):
    alpha3: constr(pattern=r"[a-zA-Z]{3}")  # type: ignore
    alpha2: constr(pattern=r"[a-zA-Z]{2}")  # type: ignore
