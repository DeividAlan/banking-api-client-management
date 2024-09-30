from sqlalchemy import Column, Float, Integer, String
from src.models.sqlite.settings.base import Base


class IndividualClientTable(Base):
    __tablename__ = "individual_clients"

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String, nullable=False)
    monthly_income = Column(Float, nullable=False)
    age = Column(Integer, nullable=False)
    phone = Column(String, nullable=False)
    category = Column(String, nullable=False)
    balance = Column(Float, nullable=False)

    def __repr__(self):
        return (
            f"<IndividualClient [id={self.id}, full_name={self.full_name}, "
            f"monthly_income={self.monthly_income}, balance={self.balance}]>"
        )
