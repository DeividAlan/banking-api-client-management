from abc import ABC, abstractmethod


class LegalEntityClientWithdrawControllerInterface(ABC):

    @abstractmethod
    def withdraw(self, client_id: int, amount: float) -> None:
        pass
