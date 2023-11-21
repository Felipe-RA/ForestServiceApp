# Backend design considerations

---

## Backend Structure

Below you can see a tree structure of this projects backend:

```bash
backend
│   ├── alembic
│   │   ├── env.py
│   │   ├── README
│   │   ├── script.py.mako
│   │   └── versions
│   │       └── 5a049f874777_add_username_index.py
│   ├── alembic.ini
│   ├── app
│   │   ├── alembic
│   │   ├── crud.py
│   │   ├── dependencies.py
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── models
│   │   │   ├── base.py
│   │   │   ├── __init__.py
│   │   │   ├── saved_query.py
│   │   │   └── user.py
│   │   ├── routers
│   │   │   ├── __init__.py
│   │   │   ├── query_router.py
│   │   │   ├── stored_queries_router.py
│   │   │   ├── user_router.py
│   │   │   └── visualization_router.py
│   │   └── schemas
│   │       ├── __init__.py
│   │       ├── saved_query.py
│   │       └── user.py
│   ├── Dockerfile
│   ├── README.MD
│   ├── requirements.txt
│   ├── sonar-project.properties
│   ├── sql
│   │   ├── 01_create_users_table.sql
│   │   ├── 02_create_saved_queries_table.sql
│   │   ├── 03_create_indexes.sql
│   │   └── 04_insert_test_data.sql
│   └── tests
│       ├── __init__.py
│       ├── test_query_router.py
│       ├── test_stored_queries_router.py
│       └── test_user_router.py
├── docker-compose.yml
```

Please take a closer look at some of the most relevant files/directories:

- `backend/app/` contains most of the definitions of our backend.
- `backend/sql` stores sql scripts to initialize the state of the Database.
- `backend/tests` stores the unit tests that were implemented, the test's names mirror the functionality that is being tested.
- `backend/alembic/versions/` stores the automatic migrations.
- `backend/app/models/` stores the ORM models.
- `backend/app/schemas/` stores the `Pydantic` data validation classes.
- `backend/app/routers` manages the `routers`, which are responsible for handling the request and responses.
- `backend/app/main.py` is the entry point of the App, and also lists the *end-points* through the use of `routers`


<br>

## SQL Scripts and ORM

We will talk about why we decided to use SQL Scripts instead of `ORM` tools like `SQLAlchemy` with `Alembic`. 

Since our app will handle queries, we value alot these benefits provided by using SQL scripts directly:

- SQL Scripts allows us to fine tune our queries, response time is very important for an app on which  queries are the bread and butter.

- Our app schema is very simple, thus making direct SQL scripts enough for our needs.

IN contrast, `ORMs`, while being excellent tools:

- Since our schema is so simple, they introduce a syntactic overhead with no benefit.

- ON our specific case, we do not benefit from the database agnosticism offered by `ORMs`

- We do not see our DB schema evolving regularly, due to the static nature of our source data. Thus, the automatic migrations are not essential. But we were asked to make the code easily extendable by other people, so we will config `Alembic`!

One key aspect on which `ORMs` win over direct SQL Scripts is with the **Code Maintainability and Readability**; ORMs allow you to work with database objects in a way that's consistent with the rest of your codebase, which  make the code more maintainable and readable.  

<br>
<br>

## Our Stretegy

<br>

---

<br>

We will use `sql` scripts for the initialization of the database inside our dockerized app, **then** we will model the common operations with `ORMs`, specifically `SQLAlchemy`.


