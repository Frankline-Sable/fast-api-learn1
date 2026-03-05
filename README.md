mkdir fast-api-learn1
cd ..


# create virtual enviroment
python3 -m venv venv

# activate
source venv/bin/activate

pip install "fastapi[standard]"

uvicorn commands is old, fast api includes the new FastAPICLIE

fastapi dev main.py

OpenApi standard: (test api, directly without any frontend code.)
- Interactive Docs: http://127.0.0.1:8000/docs (Swagger UI)
- Alternative Docs: http://127.0.0.1:8000/redoc


>>>> Pydantic - Data validation
- Validate request bodies
- Validate query parameters.
- Automatically generate API docs
- Convert json to python objects.

Without pydantic we will have to check everything.

Pydantic is a data gate keeper


sqlmodel -> fastapi
perfectly blends sqlalchemy(for databases) and pyndatic for data validation.(less work)


table =true, class also a datatable.
engine - pipe.
Depends(get_session) : opening and closing connection di.

session.commits() -> perm.

Alembic is the tool that tracks changes to the model and db updates.
Docker we dont need to install postgress into the syste,

to run a container -> docker -compose up -d

driver for postgress and migration tool

Alembic is like git for your db, keeps track of the changes u make to tables.