from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "country" ALTER COLUMN "region" TYPE VARCHAR(8) USING "region"::VARCHAR(8);
        COMMENT ON COLUMN "country"."region" IS 'Europe: Europe
Africa: Africa
Oceania: Oceania
Asia: Asia
Americas: Americas';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        COMMENT ON COLUMN "country"."region" IS 'Europe: Europe
Africa: Africa
Oceania: Oceania
Asia: Asia';
        ALTER TABLE "country" ALTER COLUMN "region" TYPE VARCHAR(7) USING "region"::VARCHAR(7);"""
