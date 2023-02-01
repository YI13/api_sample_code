# python_gcp_sample_code

Just some python code to play with GCP SDK, include storage, vision and cloud SQL.

1. Login your compute engine and clone the repo.\
```$ git clone https://github.com/YI13/python_gcp_sample_code.git```

2. Install pip in your compute engine (vm)

3. Install dependency\
```$ pip install -r requirements.txt```

4. Set your environment variables, overweite "/your/path/file.json"
```os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/your/path/file.json"```

5. Create folder before you download image from bucket, 
    overwrite ```"/your/download/path/"```

6. Using pymysql to create db connection
    ```
    def getconn() -> pymysql.connections.Connection:
        conn: pymysql.connections.Connection = connector.connect(
            "your_project:zone:db_cluster",
            "pymysql",
            user="user_name",
            password="password",
            db="db_name"
        )
        return conn
    ```

7. Run fast-api server\
```$ uvicorn main:app --reload --host 0.0.0.0 --port 8000```