# import psycopg2
# import os
# from dotenv import load_dotenv

# load_dotenv()
# #db_url = os.getenv("DB_URL")

# query = "SELECT version();"
# # conn = psycopg2.connect(
# #     host="pg-1c15d494-deba4camp-cd77.h.aivencloud.com",
# #     port="25892",
# #     database="defaultdb",
# #     user="avnadmin",
# #     password="AVNS_n6hMk1GlTczrHMAWf-a"
# # )
# with conn.cursor() as cur:
#     cur.execute(query)
#     result = cur.fetchone()
#     print(result)
# # 
# cur = conn.cursor()
# cur.execute(query)
# version_sql = cur.fetchone()[0]
# print(f"PostgreSQL version: {version_sql}")

# # create table
# create_table_query = """
# CREATE TABLE IF NOT EXISTS ZTABLE_DEBA (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(50) NOT NULL,
#     age INT NOT NULL
# );
# """
# cur.execute(create_table_query)
# conn.commit()
# # INSERT data
# insert_query = """
# INSERT INTO ZTABLE_DEBA (name, age) VALUES (%s, %s);
# """
# cur.execute(insert_query, ("Alice", 30))
# cur.execute(insert_query, ("Bob", 25))
# conn.commit()

# cur.close()