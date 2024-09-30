from sqlalchemy import Column, Float, Integer, String
from src.models.sqlite.settings.base import Base


class LegalEntityClientTable(Base):
    __tablename__ = "legal_entity_clients"

    id = Column(Integer, primary_key=True, autoincrement=True)
    business_name = Column(String, nullable=False)
    revenue = Column(Float, nullable=False)
    corporate_email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    category = Column(String, nullable=False)
    balance = Column(Float, nullable=False)

    def __repr__(self):
        return (
            f"<LegalEntityClient [id={self.id}, business_name={self.business_name}, "
            f"revenue={self.revenue}, balance={self.balance}]>"
        )
