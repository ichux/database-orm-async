import asyncio

import aiosqlite

SQL = "SELECT 1;"


async def bootstrap():
    async with aiosqlite.connect("async_sqlite.sqlite") as db:
        cursor = await db.execute(SQL)
        result = (await asyncio.create_task(cursor.fetchone()))[0]
        print(f"v1: {result}")

        async with db.execute(SQL) as cursor1:
            async for row in cursor1:
                print(f"v2: {row[0]}")

        async with db.execute(SQL) as cursor2:
            rs = [row async for row in cursor2][0][0]
            print(f"v3: {rs}")


if __name__ == "__main__":
    asyncio.run(bootstrap())
