# Garmin_FastAPI Overview

- Create a FastAPI to get data from Garmin.
- Deployed the service on Render.
- Created a cloud database on Render.

## Resources Used

- Python Version: 3.11.5
- IDE: VSCode
- Requirements:
  - Install [requirements](https://github.com/JohnnyHsieh1020/garmin_fast_api/blob/main/requirements.txt)
  ```terminal
  pip install -r requirements.txt
  ```

## Run Code Locally

```terminal
uvicorn main:app --reload
```

# FastAPI

## Endpoints Introduction

1. (POST method) /Activities: For retrieving activites data from Garmin.
2. (POST method) /Dailies: For retrieving daily data from Garmin.
3. (POST method) /PulseOx: For retrieving pulse oxygen data from Garmin.

## Deply to [Render](https://dashboard.render.com/)

1. Push your code on github repository.
2. Go to Render website. Create a new "Web Service" and connect to your github repository.
3. Name for your web service.
4. Choose a region near you.
5. Type below command on "Start Command"
   ```terminal
   uvicorn main:app --host 0.0.0.0 --port $PORT
   ```
6. Choose Free "Instance Type".
7. (Optional) Type Database information on "Environment Variables".(e.g. hostname, port, username, password, database_name)
8. Done! 🎉
9. Open your service URL.
   - My Service: https://garmin-fast-api.onrender.com/docs

# Cloud Database

## Create a PostgreSQL database on [Render](https://dashboard.render.com/)

1. Go to Render website. Create a new "PostgreSQL" database.
2. Name for your PostgreSQL instance.
3. (Optional) Name for your database name.
4. (Optional) Name for your user name.
5. Choose a region near you.
6. Choose Free "Instance Type".
7. Done! 🎉

# References

1. YouTube video:
   - [Python FAST API Tutorial](https://youtu.be/-ykeT6kk4bk?si=7cnaZLGPVCF1GkxH)
2. Articles:
   - [Render Official Documents](https://docs.render.com/)
   - [FastAPI Official Documents](https://fastapi.tiangolo.com/)
   - [Deploying FastAPI application to Render](https://blog.akashrchandran.in/deploying-fastapi-application-to-render#heading-linux-or-mac-os)
