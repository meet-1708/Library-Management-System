# Library Management System API

This is a Library Management System built using Django and Django REST Framework. It provides API endpoints to manage books, members, and loans.

## Installation Instructions

1. **Clone the Repository**:

2. **Set Up Virtual Environment**:
Make sure you have `virtualenv` installed. If not, install it with:

Create a virtual environment:

Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On Mac/Linux:
  ```
  source venv/bin/activate
  ```

3. **Install Dependencies**:

4. **Set Up PostgreSQL Database**:
Make sure you have PostgreSQL installed and running. You can download and install PostgreSQL from [here](https://www.postgresql.org/download/).

- Create a new database for the project:
  ```sql
  CREATE DATABASE library_db;
  ```

- Create a new user for the project:
  ```sql
  CREATE USER library_user WITH PASSWORD 'yourpassword';
  ```

- Grant all privileges to the user:
  ```sql
  GRANT ALL PRIVILEGES ON DATABASE library_db TO meet_patel;
  ```

- Update your `settings.py` to configure PostgreSQL as the database engine:
  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': 'library_db',
          'USER': 'meet_patel',
          'PASSWORD': '1243',
          'HOST': 'localhost',
          'PORT': '5432',
      }
  }
  ```

5. **Run Migrations**:
Run the migrations to set up your database schema:

6. **Create a Superuser** (optional, to access the Django admin panel):

7. **Run the Server**:
To start the development server, run:

The server should be running at `http://localhost:8000`.

API Endpoints

1. Book Management
GET http://localhost:8000/api/books/ - Retrieve all books.
GET http://localhost:8000/api/books/{id}/ - Retrieve details of a specific book.
POST http://localhost:8000/api/books/ - Add a new book (requires authentication).
PUT http://localhost:8000/api/books/{id}/ - Update book details (requires authentication).
DELETE http://localhost:8000/api/books/{id}/ - Remove a book (requires authentication).

2. Member Management
GET http://localhost:8000/api/members/ - Retrieve all members (requires authentication).
GET http://localhost:8000/api/members/{id}/ - Retrieve details of a specific member (requires authentication).
POST http://localhost:8000/api/members/ - Register a new member (requires authentication).
PUT http://localhost:8000/api/members/{id}/ - Update member details (requires authentication).
DELETE http://localhost:8000/api/members/{id}/ - Remove a member (requires authentication).

3. Loan Management
POST http://localhost:8000/api/loans/ - Borrow a book (requires authentication).
PUT http://localhost:8000/api/loans/{id}/return-book/ - Return a book (requires authentication).
GET http://localhost:8000/api/loans/ - Retrieve all loans (requires authentication).
GET http://localhost:8000/api/loans/{id}/ - Retrieve details of a specific loan (requires authentication).
