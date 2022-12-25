import asyncio

import databases
import orm

database = databases.Database("sqlite:///orm.sqlite")
models = orm.ModelRegistry(database=database)


class Note(orm.Model):
    tablename = "notes"
    registry = models
    fields = {
        "id": orm.Integer(primary_key=True),
        "text": orm.String(max_length=100),
        "completed": orm.Boolean(default=False),
    }


async def bootstrap():
    # Create the database and tables
    await models.create_all()
    await Note.objects.create(text="Buy the groceries.", completed=False)
    print(await Note.objects.get(id=1))


if __name__ == "__main__":
    asyncio.run(bootstrap())
