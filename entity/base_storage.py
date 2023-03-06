from typing import Dict

from abstract_storage import AbstractStorage
from exceptions import NotEnoughSpace, NotEnoughProduct


class BaseStorage(AbstractStorage):

    def __init__(self, items: Dict[str, int], capacity):
        self.__items = items
        self.__capacity = capacity

    def add(self, name, amount):
        if self.get_free_space() < amount:
            raise NotEnoughSpace

        if name in self.__items:
            self.__items[name] += amount
        else:
            self.__items[name] = amount

    def remove(self, name, amount):
        if name not in self.__items or self.__items[name] < amount:
            raise NotEnoughProduct

        self.__items[name] -= amount
        if self.__items[name] == 0:
            self.__items.pop(name)

    def get_free_space(self):
        return self.__capacity - sum(self.__items.values())

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, data):
        self.__items = data

    def get_unique_item_count(self):
        return len(self.__items)
