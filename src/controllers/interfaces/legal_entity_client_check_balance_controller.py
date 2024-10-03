from abc import ABC, abstractmethod


class LegalEntityClientCheckBalanceControllerInterface(ABC):

    @abstractmethod
    def check_balance(self, client_id: int) -> float:
        pass
