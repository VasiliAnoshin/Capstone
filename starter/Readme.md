# Capstone Project
Casting Agency Specifications
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


#### PIP Dependencies

Install dependencies 

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

## Running the server
Create the database:
createdb Capstone

To run the server, execute:

```bash
export FLASK_ENV=development
python app.py
```
Setting the FLASK_ENV variable to development will detect file changes and restart the server automatically.

## Roles
#### Casting Assistant
- Can view actors and movies
#### Casting Director
- All permissions a Casting Assistant has and…
- Add or delete an actor from the database
- Modify actors or movies
#### Executive Producer
- All permissions a Casting Director has and…
- Add or delete a movie from the database


# Testing
- dropdb Capstone
- createdb Capstone
- python test_app.py
