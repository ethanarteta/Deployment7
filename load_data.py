import sys
import csv
import os
from database import Base,Accounts,Customers,Users,CustomerLog,Transactions
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_bcrypt import Bcrypt
from flask import Flask
app = Flask(__name__)
#engine = create_engine('sqlite:///database.db',connect_args={'check_same_thread': False},echo=True)
#Base.metadata.bind = engine
DATABASE_URL = 'mysql+mysqldb://admin:abcd1234@mydatabase.c9y2f8njm0jk.us-east-1.rds.amazonaws.com/banking?charset=utf8mb4'
engine = create_engine(DATABASE_URL, pool_pre_ping=True, echo=True)
Base.metadata.bind = engine
db = scoped_session(sessionmaker(bind=engine))
bcrypt = Bcrypt(app)



if __name__ == "__main__":
    accounts()
