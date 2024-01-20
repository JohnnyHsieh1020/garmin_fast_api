from fastapi import FastAPI, Body
from datetime import datetime
import pytz
import psycopg2
import json
from decouple import config


app = FastAPI()

# Render DB info
host = config("POSTGRESQL_HOST")
port = config("POSTGRESQL_PORT")
user_name = config("POSTGRESQL_USER")
pwd = config("POSTGRESQL_PWD")
db_name = config("POSTGRESQL_DB")

# Set connection parameters
db_connect_params = {
    "host": host,
    "port": port,
    "database": db_name,
    "user": user_name,
    "password": pwd,
}


@app.post("/Activities")
async def add_activities(activities: dict = Body(...)):
    # Connect to Render DB
    con = psycopg2.connect(**db_connect_params)
    cur = con.cursor()
    print("Connect successfully!")

    # Get the type of the data
    data_type = next(iter(activities))

    # Extract the "activities" list
    details = activities["activities"][0]

    # Specify the timezone (Asia/Taipei for Taiwan)
    taipei_timezone = pytz.timezone("Asia/Taipei")

    # Get today's datetime
    now = datetime.now(taipei_timezone).strftime("%Y-%m-%d %H:%M:%S.%f")

    # Merge the data
    data = {"type": data_type, **details, "get_data_datetime": now}

    # Convert to json format
    json_data = json.dumps(data)

    # Insert to DB
    cur.execute(
        """
        INSERT INTO activities (details) VALUES (%s)
    """,
        (json_data,),
    )

    # Commit the changes
    con.commit()
    print("Create successfully!")

    # Close the connection
    cur.close()
    con.close()
    print("Connection closed!")

    return {"result": activities}


@app.post("/Dailies")
async def add_dailies(dailies: dict = Body(...)):
    # Connect to Render DB
    con = psycopg2.connect(**db_connect_params)
    cur = con.cursor()
    print("Connect successfully!")

    # Get the type of the data
    data_type = next(iter(dailies))

    # Extract the "dailies" list
    details = dailies["dailies"][0]

    # Specify the timezone (Asia/Taipei for Taiwan)
    taipei_timezone = pytz.timezone("Asia/Taipei")

    # Get today's datetime
    now = datetime.now(taipei_timezone).strftime("%Y-%m-%d %H:%M:%S.%f")

    # Merge the data
    data = {"type": data_type, **details, "get_data_datetime": now}

    # Convert to json format
    json_data = json.dumps(data)

    # Insert to DB
    cur.execute(
        """
        INSERT INTO dailies (details) VALUES (%s)
    """,
        (json_data,),
    )

    # Commit the changes
    con.commit()
    print("Create successfully!")

    # Close the connection
    cur.close()
    con.close()
    print("Connection closed!")

    return {"result": dailies}


@app.post("/PulseOx")
async def add_pulseox(pulseox: dict = Body(...)):
    # Connect to Render DB
    con = psycopg2.connect(**db_connect_params)
    cur = con.cursor()
    print("Connect successfully!")

    # Get the type of the data
    data_type = next(iter(pulseox))

    # Extract the "pulseox" list
    details = pulseox["pulseox"][0]

    # Specify the timezone (Asia/Taipei for Taiwan)
    taipei_timezone = pytz.timezone("Asia/Taipei")

    # Get today's datetime
    now = datetime.now(taipei_timezone).strftime("%Y-%m-%d %H:%M:%S.%f")

    # Merge the data
    data = {"type": data_type, **details, "get_data_datetime": now}

    # Convert to json format
    json_data = json.dumps(data)

    # Insert to DB
    cur.execute(
        """
        INSERT INTO pulseox (details) VALUES (%s)
    """,
        (json_data,),
    )

    # Commit the changes
    con.commit()
    print("Create successfully!")

    # Close the connection
    cur.close()
    con.close()
    print("Connection closed!")

    return {"result": pulseox}
