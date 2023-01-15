# https://github.com/GoogleCloudPlatform/cloud-sql-python-connector

from google.cloud.sql.connector import Connector
import sqlalchemy
import pymysql


# initialize Connector object
connector = Connector()

# function to return the database connection
def getconn() -> pymysql.connections.Connection:
    conn: pymysql.connections.Connection = connector.connect(
        "your_project:zone:db_cluster",
        "pymysql",
        user="user_name",
        password="password",
        db="db_name"
    )
    return conn

# create connection pool
pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)

# query parking_space table
def query_all_parking():
    r = []
    with pool.connect() as db_conn:
        result = db_conn.execute("SELECT * from parking.parking_space").fetchall()
        
        # Do something with the results
        for row in result:
            r.append({
                "floor": row[0],
                "zone": row[1],
                "parking_number": row[2],
                "license_plate": row[3],
                "is_available": row[4]
            })
    return r

# insert into parking_space table
def insert_parking(floor, zone, parking_number, l_p):
    # insert statement
    insert_stmt = sqlalchemy.text(
        "INSERT INTO parking.parking_space (floor, zone, parking_number, license_plate) "
        + "VALUES (:floor, :zone, :parking_number, :license_plate)")

    with pool.connect() as db_conn:
        db_conn.execute(
            insert_stmt,
            floor=floor,
            zone=zone,
            parking_number=parking_number,
            license_plate=l_p)

