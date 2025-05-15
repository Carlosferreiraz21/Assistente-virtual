from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()
engine = create_engine('sqlite:///finance.db')
Session = sessionmaker(bind=engine)

class Transaction(Base):
    __tablename__ = 'transactions'
    
    id = Column(Integer, primary_key=True)
    type = Column(String)
    amount = Column(Float)
    description = Column(String)
    date = Column(DateTime, default=datetime.now)

Base.metadata.create_all(engine)

class DatabaseOperations:
    def __init__(self):
        self.session = Session()

    def insert_transaction(self, type: str, amount: float, description: str):
        transaction = Transaction(type=type, amount=amount, description=description)
        self.session.add(transaction)
        self.session.commit()
        return transaction

    def get_transactions(self):
        return self.session.query(Transaction).all()

    def get_balance(self):
        transactions = self.get_transactions()
        return sum(t.amount if t.type == "income" else -t.amount for t in transactions) 