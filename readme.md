
# Personal Finance Manager

Api to manage personal finances, with user authentication, transaction handling, and a domain-driven design inspired architecture. Built to be scalable and easily integrable with a frontend.

## Main Structure
- src/auth: authentication (login, token generation, password hashing)

- src/users: user management

- src/transactions: transaction creation and management

- src/shared: shared utilities and components

- tests: unit and integration tests

## Features

- Incomes and expenses management

- Balance calculations

- Clean architecture

- Tests with pytest

## REQUIREMENTS

- python 3.11+

- pipenv or venv (optional)

- dependencies: fastapi, uvicorn, pydantic, pytest, bcrypt, python-jose, python-dotenv 

## INSTALLATION

1. clone the repository

2. create a virtual environment
- python -m venv venv
- source venv/bin/activate (linux/mac)
- venv\Scripts\activate (windows)

3. install dependencies
pip install -r requirements.txt

4. create a .env file in the project root with:
JWT_SECRET_KEY=your_secret_key

## RUNNING THE APP
uvicorn app:app --reload

### MAIN ENDPOINTS

- POST /auth/register: register a new user

- POST /auth/login: log in and get jwt token

- POST /transactions: create a new transaction

- GET /transactions: list all user transactions

## TESTING
run tests with:
pytest -v