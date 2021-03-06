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

## Hosting
This project has been deployed using Heroku and can be found at this URL: https://capstonend.herokuapp.com/

## Identity and Auth
Auth0 login: https://auth0.com/

Recieve Token: 
https://fsbenfranklin.auth0.com/authorize?audience=Capstone&response_type=token&client_id=lLapC5LQ5Um6fyGxLS8qwDOBwQRMrg3W&redirect_uri=http://localhost:8080/login-results

Token check: https://jwt.io/

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

## API reference
```bash 
GET 
- /actors (get:movies) permissions required
- /movies (get:movies) permissions required
```
```bash 
POST
- /movies/create (post:movies) permission required
- /actors/create (post:actors) permission required
```
```bash
PATCH
- /movies/<int:id> (patch:movie) permission required
- /actors/<int:id> (patch:actor) permission required
```
```bash
DELETE
- /actors/<int:id> (delete:actor) permission required
- /movies/<int:id> (delete:movie) permission required
```
# Testing
Testing with unittest library
```bash
dropdb Capstone
createdb Capstone
python test_app.py
```
