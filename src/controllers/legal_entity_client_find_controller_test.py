import pytest
from src.errors.errors_types.http_not_found import HttpNotFoundError
from src.models.sqlite.entities.legal_entity_client import LegalEntityClientTable
from .legal_entity_client_find_controller import LegalEntityClientFindController


class MockClientRepository:
    def __init__(self, client_data: dict):
        self.client_data = client_data

    def find_legal_entity_client(self, client_id: int):
        return self.client_data.get(client_id)


mock_clients = {
    1: LegalEntityClientTable(
        id=1,
        business_name="Tech Corp",
        revenue=500000.0,
        corporate_email="info@techcorp.com",
        phone="+12345678901",
        category="Tech",
        balance=10000.0,
    ),
    2: LegalEntityClientTable(
        id=2,
        business_name="Biz Solutions",
        revenue=300000.0,
        corporate_email="contact@bizsolutions.com",
        phone="+98765432100",
        category="Consulting",
        balance=20000.0,
    ),
}


def test_find_existing_legal_entity_client():
    controller = LegalEntityClientFindController(MockClientRepository(mock_clients))

    response = controller.find_by_id(1)

    assert response["id"] == 1
    assert response["business_name"] == "Tech Corp"
    assert response["revenue"] == 500000.0
    assert response["corporate_email"] == "info@techcorp.com"
    assert response["phone"] == "+12345678901"
    assert response["category"] == "Tech"
    assert response["balance"] == 10000.0


def test_find_non_existing_legal_entity_client():
    controller = LegalEntityClientFindController(MockClientRepository(mock_clients))

    with pytest.raises(HttpNotFoundError, match="Client not found."):
        controller.find_by_id(999)
