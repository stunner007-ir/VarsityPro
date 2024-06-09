# Text Summarizer Backend

This project is a backend application built using Django and Django Rest Framework (DRF). It provides APIs for user management, text summarization, and user search functionality. The project uses Celery to handle text summarization tasks asynchronously.

# Prerequisites

- Python 3.7 or higher
- Django 3.2 or higher
- Postman (For API Testing)
- Django REST Framework 3.12 or higher
- pip (Python package manager)
- celery
- translator

## Features

1. **User Management:**

   - User registration, login, and logout.
   - APIs to edit, delete, and create a user.
   - API to search for users by username and return combined name and email.

2. **Text Summarization:**

   - API to ingest a large text field and summarize it using a third-party API.
   - Celery is used to handle the summarization task in a task queue.

3. **Permissions and Security:**
   - APIs are secured using Django Rest Framework's permissions.
   - Appropriate permissions are implemented to ensure secure access.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/text-summarizer-backend.git
   cd text-summarizer-backend
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  
   # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run database migrations:**

    ```bash
    python manage.py migrate
    ```

4. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

5. **Start the development server:**

    ```bash
    python manage.py runserver
    ```

6. **Start Celery worker:**

    ```bash
    celery -A text_summarizer worker --loglevel=info
    ```

### Access the API at http://localhost:8000/

## API Endpoints

### User Management API Endpoints

#### User Registration

- **URL:** `/api/users/register/`
- **Method:** `POST`

#### User Details

- **URL:** `/api/users/<int:pk>/`
- **Method:** `GET`

#### Update User

- **URL:** `/api/users/<int:pk>/`
- **Method:** `PUT`

#### Delete User

- **URL:** `/api/users/<int:pk>/`
- **Method:** `DELETE`

#### List Users

- **URL:** `/api/users/`
- **Method:** `GET`

### Text Summarization API Endpoints

#### Summarize Text

- **URL:** `/api/summarize/`
- **Method:** `POST`

#### Summarization Result

- **URL:** `/api/summarize/result/<task_id>/`
- **Method:** `GET`

### Authentication Endpoints

#### Obtain Auth Token

- **URL:** `/api-token-auth/`
- **Method:** `POST`

#### Logout

- **URL:** `/api-auth/logout/`
- **Method:** `POST`
