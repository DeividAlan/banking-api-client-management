from typing import List, Optional
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.individual_client import IndividualClientTable
from src.models.sqlite.interface.client import ClientInterface
from src.errors.http_invalid_balance import HttpInvalidBalanceError
from src.errors.http_not_found import HttpNotFoundError


class IndividualClientRepository(ClientInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def insert_individual_client(
        self,
        full_name: str,
        monthly_income: float,
        age: int,
        phone: str,
        category: str,
        balance: float,
    ) -> None:
        with self.__db_connection as database:
            try:
                individual_client_data = IndividualClientTable(
                    full_name=full_name,
                    monthly_income=monthly_income,
                    age=age,
                    phone=phone,
                    category=category,
                    balance=balance,
                )

                database.session.add(individual_client_data)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def list_individual_clients(self) -> List[IndividualClientTable]:
        with self.__db_connection as database:
            try:
                individual_clients = database.session.query(IndividualClientTable).all()
                return individual_clients
            except NoResultFound:
                return []

    def find_individual_client(self, individual_client_id: int) -> Optional[IndividualClientTable]:
        with self.__db_connection as database:
            individual_client = database.session.query(IndividualClientTable).get(
                individual_client_id
            )
            return individual_client

    def check_balance(self, client_id: int) -> float:
        with self.__db_connection as database:
            individual_client = database.session.query(IndividualClientTable).get(client_id)

            if not individual_client:
                raise HttpNotFoundError("Client not found.")

            return individual_client.balance

    def withdraw_money(self, client_id: int, amount: float) -> None:
        with self.__db_connection as database:
            try:
                individual_client = database.session.query(IndividualClientTable).get(client_id)

                if not individual_client:
                    raise HttpNotFoundError("Client not found.")

                if individual_client.balance < amount:
                    raise HttpInvalidBalanceError(
                        "Insufficient balance to complete the withdrawal."
                    )

                individual_client.balance -= amount

                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
