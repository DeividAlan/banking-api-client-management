from sqlalchemy import Column, String, Integer, Float, Enum
from src.models.sqlite.settings.base import Base


class ClientTable(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, autoincrement=True)
    phone = Column(String, nullable=True)
    category = Column(String, nullable=True)
    balance = Column(Float, nullable=True)
    client_type = Column(
        Enum("individual", "legal_entity", name="client_type_enum"), nullable=False
    )

    def __repr__(self):
        return f"<Client [id={self.id}, client_type={self.client_type}, balance={self.balance}]>"
