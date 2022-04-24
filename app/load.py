import psycopg2
import os

host = "postgres"
database = os.environ["db"]
user = os.environ["POSTGRES_USER"]
passwd = os.environ["POSTGRES_PASSWORD"]

def connect():
    conn = None
    try:
        conn = psycopg2.connect(host=host, database=database, user=user, password=passwd)
    except psycopg2.Error as e:
        print(f'Had problem connecting with error {e}.')
    cursor = conn.cursor()
    return cursor,conn


def load_data(data):
    cursor,conn = connect()
    try:
        #Inserting potentially duplicated data into staging table
        cursor.execute(f"""    
            INSERT INTO PUBLIC.posts_staging VALUES ({data["post_id"]}, '{data["text"]}', '{data["image"]}', {data["likes"]}, {data["shares"]}, {data["comments"]});
        """)
        #Merge/upsert staging data into posts table, on conflict we simply don't insert the duplicated row
        cursor.execute(f"""
            INSERT INTO PUBLIC.posts (SELECT * FROM PUBLIC.posts_staging) ON CONFLICT (id) DO NOTHING;
         """)
         #Truncate the staging table for the future inserts
        cursor.execute("""
         TRUNCATE TABLE PUBLIC.posts_staging;
         """)
        conn.commit()
    except psycopg2.Error as e:
        print(f"Failed with error {e}")
    conn.close()

