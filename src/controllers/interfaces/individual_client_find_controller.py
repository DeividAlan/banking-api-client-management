from typing import Dict, Optional
from abc import ABC, abstractmethod


class IndividualClientFindControllerInterface(ABC):

    @abstractmethod
    def find_by_id(self, client_id: int) -> Optional[Dict]:
        pass
