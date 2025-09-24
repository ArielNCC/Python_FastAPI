import os
from sqlalchemy import create_engine, MetaData
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
meta = MetaData()
conn = engine.connect()