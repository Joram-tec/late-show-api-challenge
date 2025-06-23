## Features
User registration and login with JWT authentication

View, create, and delete episodes

Manage guest appearances on episodes

View guest details and their appearances

Token-based access protection on endpoints

PostgreSQL database with Flask SQLAlchemy ORM

## Author
Joram Wayane Muya 

##  Getting Started
1. Clone the repo
- git clone git@github.com:Joram-tec/late-show-api-challenge.git

-  cd late-show-api

2. Create and activate a virtual environment
- python3 -m venv venv
- source venv/bin/activate

4. Set up the database

- createdb late_show_db
- flask db init
- flask db revision --autogenerate -m "Initial migration"
- flask db upgrade

5. Seeding the database
- python seed.py

6. Run the server
- flask run 

7.  Authentication
- Register a user via POST /signup

- Login to receive a JWT via POST /login

- Use the JWT as a Bearer token in the Authorization header for protected endpoints

8. Technologies Used
Python 3.8+

Flask

Flask SQLAlchemy

Flask Migrate

Flask JWT Extended

PostgreSQL

Marshmallow for serialization

Postman for API testing

10. License
This project is licensed under the MIT License.

