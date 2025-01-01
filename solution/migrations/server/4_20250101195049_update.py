from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" DROP CONSTRAINT IF EXISTS "fk_user_country_273fa9f9";
        COMMENT ON COLUMN "country"."region" IS 'EUROPE: Europe
AFRICA: Africa
OCEANIA: Oceania
ASIA: Asia
AMERICAS: Americas
UNKNOWN: ';
        ALTER TABLE "user" RENAME COLUMN "country_code_id" TO "country_id";
        ALTER TABLE "user" ADD CONSTRAINT "fk_user_country_3c9b2b9d" FOREIGN KEY ("country_id") REFERENCES "country" ("id") ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" DROP CONSTRAINT IF EXISTS "fk_user_country_3c9b2b9d";
        ALTER TABLE "user" RENAME COLUMN "country_id" TO "country_code_id";
        COMMENT ON COLUMN "country"."region" IS 'Europe: Europe
Africa: Africa
Oceania: Oceania
Asia: Asia
Americas: Americas
Unknow: ';
        ALTER TABLE "user" ADD CONSTRAINT "fk_user_country_273fa9f9" FOREIGN KEY ("country_code_id") REFERENCES "country" ("id") ON DELETE CASCADE;"""
