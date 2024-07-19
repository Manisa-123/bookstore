# FastAPI Bookstore

This is a simple bookstore application built with FastAPI, SQLAlchemy, and Alembic.

## Features

- User registration and authentication
- Book listing and management
- Order creation and management

## Requirements

- Python 3.7+
- FastAPI
- SQLAlchemy
- Alembic
- Uvicorn

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/bookstore.git
   cd bookstore

2. Create and activate a virtual environment

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install the dependencies:
   
    ```bash
   pip install -r requirements.txt

4. Initialize the database:
    
    ```bash
   alembic upgrade head

5. Run the application:
    ```bash
   uvicorn main:app --reload  

6. Open your browser and go to http://127.0.0.1:8000/docs to see the API documentation.

   