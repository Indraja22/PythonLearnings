import psycopg2

conn = psycopg2.connect(database="olympics",
                        user="postgres",
                        password="admin",
                        host="localhost",
                        port=5433)
curr = conn.cursor()

curr.execute("select * from athlete_events where 1=2")
cols_all = curr.description
col_list = [col[0] for col in cols_all]
total_num_of_cols = len(col_list)
print(f"Total number of columns in the table : {total_num_of_cols}")
cols_with_null_values = []
cols_without_null_values = []
for col_name in col_list:
    curr.execute(f"select * from athlete_events where {col_name} is null")
    count_of_null_rows_in_col = curr.rowcount
    try:
        assert count_of_null_rows_in_col == 0
        cols_without_null_values.append(col_name)
    except AssertionError:
        cols_with_null_values.append(col_name)

print(f"Columns with null values : {cols_with_null_values}")
print(f"Columns without null values : {cols_without_null_values}")

curr.close()
conn.close()
