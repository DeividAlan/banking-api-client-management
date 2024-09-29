from sqlalchemy import Column, Float, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from src.models.sqlite.settings.base import Base


class LegalEntityClientTable(Base):
    __tablename__ = "legal_entity_clients"

    id = Column(Integer, ForeignKey("clients.id"), primary_key=True)
    revenue = Column(Float, nullable=True)
    business_name = Column(String, nullable=False)
    corporate_email = Column(String, nullable=True)

    client = relationship("ClientTable", back_populates="legal_entity_client")

    def __repr__(self):
        return f"<LegalEntityClient [business_name={self.business_name}, revenue={self.revenue}]>"
