from sqlalchemy import Column, Float, Integer, String
from src.models.sqlite.settings.base import Base


class IndividualClientTable(Base):
    __tablename__ = "individual_clients"

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String, nullable=False)
    monthly_income = Column(Float, nullable=True)
    age = Column(Integer, nullable=True)
    phone = Column(String, nullable=True)
    category = Column(String, nullable=True)
    balance = Column(Float, nullable=True)

    def __repr__(self):
        return (
            f"<IndividualClient [id={self.id}, full_name={self.full_name}, "
            f"monthly_income={self.monthly_income}, balance={self.balance}]>"
        )
