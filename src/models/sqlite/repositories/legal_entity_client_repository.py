from typing import List, Optional
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.legal_entity_client import LegalEntityClientTable
from src.models.sqlite.interface.client import ClientInterface
from src.errors.errors_types.http_invalid_balance import HttpInvalidBalanceError
from src.errors.errors_types.http_not_found import HttpNotFoundError


class LegalEntityClientRepository(ClientInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def insert_legal_entity_client(
        self,
        business_name: str,
        revenue: float,
        corporate_email: str,
        phone: str,
        category: str,
        balance: float,
    ) -> None:
        with self.__db_connection as database:
            try:
                legal_entity_client_data = LegalEntityClientTable(
                    business_name=business_name,
                    revenue=revenue,
                    corporate_email=corporate_email,
                    phone=phone,
                    category=category,
                    balance=balance,
                )

                database.session.add(legal_entity_client_data)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def list_legal_entity_clients(self) -> List[LegalEntityClientTable]:
        with self.__db_connection as database:
            try:
                legal_entity_clients = database.session.query(LegalEntityClientTable).all()
                return legal_entity_clients
            except NoResultFound:
                return []

    def find_legal_entity_client(self, client_id: int) -> Optional[LegalEntityClientTable]:
        with self.__db_connection as database:
            legal_entity_client = database.session.query(LegalEntityClientTable).get(client_id)
            return legal_entity_client

    def check_balance(self, client_id: int) -> float:
        with self.__db_connection as database:
            legal_entity_client = database.session.query(LegalEntityClientTable).get(client_id)

            if not legal_entity_client:
                raise HttpNotFoundError("Client not found.")

            return legal_entity_client.balance

    def withdraw_money(self, client_id: int, amount: float) -> None:
        with self.__db_connection as database:
            try:
                legal_entity_client = database.session.query(LegalEntityClientTable).get(client_id)

                if not legal_entity_client:
                    raise HttpNotFoundError("Client not found.")

                if legal_entity_client.balance < amount:
                    raise HttpInvalidBalanceError(
                        "Insufficient balance to complete the withdrawal."
                    )

                legal_entity_client.balance -= amount

                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
