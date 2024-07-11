from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import os


load_dotenv()
uri = os.getenv('DATABASE_URI')



def query_data(query):
    """Executa uma query SQL no banco de dados e retorna os resultados como um DataFrame."""
    engine = create_engine(uri)
    df = pd.read_sql_query(query, engine)
    return df