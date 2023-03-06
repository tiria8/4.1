from abc import ABC, abstractmethod

class AbstractStorage(ABC):
    @abstractmethod
    def add(self, name, amount):
        pass

    @abstractmethod
    def remove(self, name, amount):
        pass

    @abstractmethod
    def get_free_space(self):
        pass


    @abstractmethod
    def get_unique_item_count(self):
        pass