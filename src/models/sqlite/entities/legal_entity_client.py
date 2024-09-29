from sqlalchemy import Column, Float, Integer, String
from src.models.sqlite.settings.base import Base


class LegalEntityClientTable(Base):
    __tablename__ = "legal_entity_clients"

    id = Column(Integer, primary_key=True, autoincrement=True)
    business_name = Column(String, nullable=False)
    revenue = Column(Float, nullable=True)
    corporate_email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    category = Column(String, nullable=True)
    balance = Column(Float, nullable=True)

    def __repr__(self):
        return (
            f"<LegalEntityClient [id={self.id}, business_name={self.business_name}, "
            f"revenue={self.revenue}, balance={self.balance}]>"
        )
