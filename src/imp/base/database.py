from abc import ABC, abstractmethod


class AbstactClassDB(ABC):
    @abstractmethod
    def save_list(self, lisofchannels, bool):
        pass

    @abstractmethod
    def get_list(self, bool):
        pass
