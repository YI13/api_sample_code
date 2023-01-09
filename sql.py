# https://github.com/GoogleCloudPlatform/cloud-sql-python-connector

from google.cloud.sql.connector import Connector
import sqlalchemy
import pymysql


# initialize Connector object
connector = Connector()

# function to return the database connection
def getconn() -> pymysql.connections.Connection:
    conn: pymysql.connections.Connection = connector.connect(
        "your-project-123456789:asia-east1:admin ",
        "pymysql",
        user="user_name",
        password="your_password",
        db="db_name"
    )
    return conn

# create connection pool
pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)

def insert_data(id, title):
    # insert statement
    insert_stmt = sqlalchemy.text(
        "INSERT INTO parking (id, title) VALUES (:id, :title)",
    )

    # interact with Cloud SQL database using connection pool
    with pool.connect() as db_conn:
        # insert into database
        db_conn.execute(insert_stmt, id=id, title=title)

        # query database
        result = db_conn.execute("SELECT * from parking").fetchall()

        # Do something with the results
        for row in result:
            print("+++++++++", row)