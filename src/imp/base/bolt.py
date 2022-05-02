from abc import ABC, abstractmethod


class APIBolt(ABC):
    @abstractmethod
    def add_channel(self, username):
        pass

    @abstractmethod
    def remove_channel(self, username):
        pass

    @abstractmethod
    def block_channel(self, username):
        pass

    @abstractmethod
    def show_recommendations(self):
        pass
