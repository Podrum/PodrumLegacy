from abc import ABC, abstractmethod


class Command(ABC):

    name: str
    description: str

    @abstractmethod
    def __init__(self, server) -> None:
        self.server = server

    @abstractmethod
    def execute(self, args: list, sender) -> None:
        pass
