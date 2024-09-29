from sqlalchemy import Column, Float, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from src.models.sqlite.settings.base import Base


class IndividualClientTable(Base):
    __tablename__ = "individual_clients"

    id = Column(Integer, ForeignKey("clients.id"), primary_key=True)
    monthly_income = Column(Float, nullable=True)
    age = Column(Integer, nullable=True)
    full_name = Column(String, nullable=False)

    client = relationship("ClientTable", back_populates="individual_client")

    def __repr__(self):
        return (
            f"<IndividualClient [full_name={self.full_name}, monthly_income={self.monthly_income}]>"
        )
