import psycopg2
import pytest
import logging

curr = None
conn = None

@pytest.fixture
def connect_to_db():
    global conn
    global curr
    conn = psycopg2.connect(database="olympics",user="postgres",
                            password="admin",host="localhost",port=5433)
    curr = conn.cursor()

    yield
    conn.close()
    curr.close()
    

@pytest.mark.usefixtures("connect_to_db")
def test_table_row_count(caplog):
    caplog.set_level(logging.INFO)
    curr.execute("select * from athlete_events")
    table_row_count = curr.rowcount
    print(table_row_count)
    assert table_row_count > 0
    logging.info("Table Row Count: %s ", table_row_count)
