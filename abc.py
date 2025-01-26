import pandas as pd
import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="demo",
)
table_name = "sample"
query = f"SELECT * FROM {table_name}"

df= pd.read_sql(query, connection)

print(df)