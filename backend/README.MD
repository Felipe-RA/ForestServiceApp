# Backend design considerations

---

<br>

## SQL Scripts vs ORM

We will talk about why we decided to use SQL Scripts instead of `ORM` tools like `SQLAlchemy` with `Alembic`. 

Since our app will handle queries, we value alot these benefits provided by using SQL scripts directly:

- SQL Scripts allows us to fine tune our queries, response time is very important for an app on which  queries are the bread and butter.

- Our app schema is very simple, thus making direct SQL scripts enough for our needs.

IN contrast, `ORMs`, while being excellent tools:

- Since our schema is so simple, they introduce a syntactic overhead with no benefit.

- ON our specific case, we do not benefit from the database agnosticism offered by `ORMs`

- We do not see our DB schema evolving regularly, due to the static nature of our source data. Thus, the automatic migrations are not essential.  

One key aspect on which `ORMs` win over direct SQL SCripts is with the **Code Maintainability and Readability**; ORMs allow you to work with database objects in a way that's consistent with the rest of your codebase, which  make the code more maintainable and readable.  

Nonetheless, we decided to use direct sql scripts this time.