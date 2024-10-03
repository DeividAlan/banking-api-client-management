from abc import ABC, abstractmethod


class IndividualClientWithdrawControllerInterface(ABC):

    @abstractmethod
    def withdraw(self, client_id: int, amount: float) -> None:
        pass
