import pandas as pd
from sqlalchemy import create_engine

conn_string = "postgresql://postgres:admin@localhost:5433/olympics"
db = create_engine(conn_string)
conn = db.connect()

files = ["athlete_events","noc_regions"]

for file in files:
    df = pd.read_csv(f"/Users/indrajanaik/Developer/data_set/{file}.csv",)
    df.columns = df.columns.str.lower()
    df.to_sql(f"{file}",con=conn,if_exists="replace",index=False)