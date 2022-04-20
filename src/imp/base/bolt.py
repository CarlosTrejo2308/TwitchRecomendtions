from abc import ABC, abstractmethod


class APIBolt(ABC):
    def __init__(self, database):
        self._channels = {}
        self._db = database

    @abstractmethod
    def add_channel(self, user_name):
        pass

    @abstractmethod
    def remove_channel(self, user_name):
        pass

    @abstractmethod
    def block_channel(self, user_name):
        pass

    @abstractmethod
    def show_recommendations(self):
        pass

    @abstractmethod
    def save_session(self):
        # bd.save_list(self.ls_channel)
        pass

    @abstractmethod
    def load_session(self):
        #self.ls_channel = bd.get_list()
        pass
