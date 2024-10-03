from typing import Dict, List
from abc import ABC, abstractmethod


class LegalEntityClientListControllerInterface(ABC):

    @abstractmethod
    def list(self) -> List[Dict]:
        pass
