from typing import Type, List, Any, Optional
from tortoise import Model
from tortoise.exceptions import DoesNotExist, IntegrityError
from src.infra.database.exception import DBDoesNotExistException, DBUniqueException


class TortoiseRepository:
    model: Type[Model]

    async def add_one(self, **kwargs: Any) -> Model:
        """
        Добавляет одну запись в базу данных.

        :param kwargs: Поля и значения для создания новой записи.
        :return: Созданная запись.
        :raises DBUniqueException: Если возникает ошибка уникальности.
        """
        try:
            instance = await self.model.create(**kwargs)
            return instance
        except IntegrityError as error:
            raise DBUniqueException(details=error.args)

    async def edit_one(self, **kwargs: Any) -> Model:
        """
        Обновляет запись в базе данных на основе переданных параметров.

        :param kwargs: Поля для фильтрации и обновления.
        :return: Обновленная запись.
        :raises DBUniqueException: Если возникает ошибка уникальности.
        :raises DBDoesNotExist: Если запись не найдена.
        """
        filter_by = {
            k: v for k, v in kwargs.items() if k in self.model._meta.fields_map
        }
        data = {k: v for k, v in kwargs.items() if k not in self.model._meta.fields_map}

        try:
            await self.model.filter(**filter_by).update(**data)
            return await self.model.get(**filter_by)
        except IntegrityError as error:
            raise DBUniqueException(details=error.args)
        except DoesNotExist as error:
            raise DBDoesNotExistException(details=error.args)

    async def find_all(
        self, order_by: Optional[str] = None, order_desc: bool = False
    ) -> List[Model]:
        """
        Находит все записи в базе данных.

        :param order_by: Поле для сортировки.
        :param order_desc: Если True, сортировка по убыванию.
        :return: Список записей.
        """
        queryset = self.model.all()
        if order_by:
            queryset = queryset.order_by(f"-{order_by}" if order_desc else order_by)
        return await queryset

    async def find_where(
        self, order_by: Optional[str] = None, order_desc: bool = False, **kwargs: Any
    ) -> List[Model]:
        """
        Находит записи по заданным условиям.

        :param order_by: Поле для сортировки.
        :param order_desc: Если True, сортировка по убыванию.
        :param kwargs: Условия для фильтрации.
        :return: Список найденных записей.
        """
        queryset = self.model.filter(**kwargs)
        if order_by:
            queryset = queryset.order_by(f"-{order_by}" if order_desc else order_by)
        return await queryset

    async def remove_where(self, **kwargs: Any) -> None:
        """
        Удаляет записи по заданным условиям.

        :param kwargs: Условия для фильтрации записей, подлежащих удалению.
        """
        await self.model.filter(**kwargs).delete()

    async def get_where(self, **kwargs: Any) -> Model:
        """
        Получает одну запись по заданным условиям.

        :param kwargs: Условия для фильтрации.
        :return: Запись.
        :raises DBDoesNotExist: Если запись не найдена.
        """
        try:
            return await self.model.get(**kwargs)
        except DoesNotExist as error:
            raise DBDoesNotExistException(details=error.args)

    async def get_count(self, **kwargs: Any) -> int:
        """
        Получает количество записей, соответствующих заданным условиям.

        :param kwargs: Условия для фильтрации.
        :return: Количество найденных записей.
        """
        return await self.model.filter(**kwargs).count()

    async def pagination_get(
        self, limit: int, offset: int, order_by: Optional[str] = None, **kwargs: Any
    ) -> List[Model]:
        """
        Получает записи с поддержкой пагинации.

        :param limit: Максимальное количество записей для получения.
        :param offset: Смещение для пагинации.
        :param order_by: Поле для сортировки.
        :param kwargs: Условия для фильтрации.
        :return: Список найденных записей.
        """
        queryset = self.model.filter(**kwargs).limit(limit).offset(offset)
        if order_by:
            queryset = queryset.order_by(order_by)
        return await queryset

    async def find_one(self, **kwargs: Any) -> Model:
        """
        Находит одну запись по заданным условиям.

        :param kwargs: Условия для фильтрации.
        :return: Запись.
        :raises DBDoesNotExist: Если запись не найдена.
        """
        try:
            return await self.model.get(**kwargs)
        except DoesNotExist as error:
            raise DBDoesNotExistException(details=error.args)
