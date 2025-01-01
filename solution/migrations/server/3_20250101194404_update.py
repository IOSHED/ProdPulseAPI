from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        COMMENT ON COLUMN "country"."region" IS 'Europe: Europe
Africa: Africa
Oceania: Oceania
Asia: Asia
Americas: Americas
Unknow: ';
        CREATE TABLE IF NOT EXISTS "user" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "login" VARCHAR(30) NOT NULL UNIQUE,
    "email" VARCHAR(50) NOT NULL UNIQUE,
    "phone" VARCHAR(20) NOT NULL UNIQUE,
    "image" VARCHAR(200) NOT NULL,
    "is_public" BOOL NOT NULL,
    "country_code_id" INT NOT NULL REFERENCES "country" ("id") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        COMMENT ON COLUMN "country"."region" IS 'Europe: Europe
Africa: Africa
Oceania: Oceania
Asia: Asia
Americas: Americas';
        DROP TABLE IF EXISTS "user";"""
