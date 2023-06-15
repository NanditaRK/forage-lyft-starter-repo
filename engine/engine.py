from abc import ABC, abstractmethod

class Engine(ABC):

    @abstractmethod
    def needs_Service(self):
        pass