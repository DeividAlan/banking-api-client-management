from abc import ABC, abstractmethod


class ClientInterface(ABC):

    @abstractmethod
    def withdraw_money(self, client_id: int, amount: float) -> None:
        pass

    @abstractmethod
    def check_balance(self, client_id: int) -> float:
        pass
