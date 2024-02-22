from typing import Dict, List, TypeVar
from peewee import ModelSelect
from database.common.models import ModelBase
from database.common.models import db

T = TypeVar('T')

def _store_date(db: db, model: T, *data: List[Dict]) -> None:
    """
    Добавление записи в базу данных
    """
    with db.atomic():
        model.insert_many(*data).execute()


def _retrieve_all_data(db: db, model: T, *columns: ModelBase) -> ModelSelect:
    """
    Считать данные из базы данных
    """
    with db.atomic():
        response = model.select(*columns)
    return response

def _print_ten(db: db, model: T, *columns: ModelBase) -> ModelSelect:
    with db.atomic():
        response = model.select().limit(10).order_by(*columns)
    return response

class CRUDInterface():
    @staticmethod
    def create():
        return _store_date

    @staticmethod
    def retrieve():
        return _retrieve_all_data

    @staticmethod
    def last_ten():
        return _print_ten


if __name__ == '__main__':
    _store_date()
    _retrieve_all_data()
    _print_ten()
    CRUDInterface()