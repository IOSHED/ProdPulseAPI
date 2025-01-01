from tortoise import Model, fields


class User(Model):
    id: int = fields.IntField(pk=True)
    login: str = fields.CharField(max_length=30, unique=True)
    email: str = fields.CharField(max_length=50, min_length=1, unique=True)
    phone: str = fields.CharField(max_length=20, unique=True)
    image: str = fields.CharField(max_length=200, min_length=1)
    country: int = fields.ForeignKeyField("server.Country", related_name="user")
    is_public: bool = fields.BooleanField()

    def __str__(self) -> str:
        return self.login
