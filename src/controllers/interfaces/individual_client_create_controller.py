from typing import Dict
from abc import ABC, abstractmethod


class IndividualClientCreateControllerInterface(ABC):

    @abstractmethod
    def create(self, client_info: Dict) -> None:
        pass
