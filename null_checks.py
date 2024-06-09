from sqlalchemy import create_engine

conn_string = "postgresql://postgres:admin@localhost:5433/olympics"
db = create_engine(conn_string)
conn = db.connect()

height_null_check_sql = conn.exec_driver_sql("select * from athlete_events where height is null")
row_count_null_heights = height_null_check_sql.rowcount
try:
    assert row_count_null_heights == 0
except AssertionError:
    print(f"row_count_null_heights should be zero but was : {row_count_null_heights}")

# print(height_null_check_sql.rowcount)
conn.close()
