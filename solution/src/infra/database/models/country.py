from enum import Enum

from tortoise import Model, fields

from src.infra.database.models.user import User  # noqa: F401


class Regions(Enum):
    EUROPE = "Europe"
    AFRICA = "Africa"
    OCEANIA = "Oceania"
    ASIA = "Asia"
    AMERICAS = "Americas"
    UNKNOWN = ""


class Country(Model):
    id: int = fields.IntField(pk=True)
    name: str = fields.CharField(max_length=100)
    alpha2: str = fields.CharField(max_length=2, unique=True)
    alpha3: str = fields.CharField(max_length=3)
    region: str = fields.CharEnumField(Regions)

    user: type = fields.ForeignKeyRelation["User"]

    def __str__(self) -> str:
        return self.title
