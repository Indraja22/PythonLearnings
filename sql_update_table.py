import pandas as pd
from sqlalchemy import create_engine

conn_string = "postgresql://postgres:admin@localhost:5433/paintings"
db = create_engine(conn_string)
conn = db.connect()

files = ["artist","work","canvas_size","image_link",
        "museum_hours","museum","product_size","subject"]

for file in files:
    df = pd.read_csv(f"/Users/indrajanaik/Developer/DataSet_Famous_Paintings/{file}.csv")
    df.to_sql(f"{file}",con=conn,if_exists="replace",index=False)