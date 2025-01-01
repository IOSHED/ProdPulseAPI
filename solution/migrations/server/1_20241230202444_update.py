from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "country" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(100) NOT NULL,
    "alpha2" VARCHAR(2) NOT NULL UNIQUE,
    "alpha3" VARCHAR(3) NOT NULL,
    "region" VARCHAR(7) NOT NULL
);
COMMENT ON COLUMN "country"."region" IS 'Europe: Europe\nAfrica: Africa\nOceania: Oceania\nAsia: Asia';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "country";"""
