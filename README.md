# Job Application Tracker

A RESTful API backend for tracking job applications built with FastAPI, SQLAlchemy, and PostgreSQL.

## Tech Stack

- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - Python SQL toolkit and ORM with async support
- **PostgreSQL** - Production-grade relational database
- **psycopg3** - Modern PostgreSQL adapter with async support
- **Docker** - Containerization for easy deployment
- **Poetry** - Modern Python dependency management
- **Pydantic** - Data validation and serialization

## Dependency Management

This project uses **Poetry** for dependency management instead of pip/requirements.txt. Poetry provides:

- **Deterministic builds** with lock files
- **Better dependency resolution** 
- **Virtual environment management**
- **Simplified packaging and publishing**
- **Separation of production and development dependencies**

## Environment Variables

The application uses environment variables for configuration. Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql+psycopg://postgres:password@db:5432/jobtracker
```

**Note**: The `.env` file is not committed to version control for security reasons.

## Local Development

### Prerequisites

- Python 3.12+
- Poetry (install from https://python-poetry.org/docs/#installation)

### Setup

1. **Install dependencies:**
   ```bash
   poetry install
   ```

2. **Activate the virtual environment:**
   ```bash
   poetry shell
   ```

3. **Run the development server:**
   ```bash
   poetry run uvicorn app.main:app --reload
   ```

### Managing Dependencies

- **Add a new dependency:**
  ```bash
  poetry add package-name
  ```

- **Add a development dependency:**
  ```bash
  poetry add --group dev package-name
  ```

- **Update dependencies:**
  ```bash
  poetry update
  ```

## Running with Docker

Start the entire application stack:

```bash
docker compose up --build
```

This will start both the FastAPI backend and PostgreSQL database with persistent storage.

### Manual Docker Build (Optional)

```bash
docker build -t job-tracker-backend .
```

## API Access

- **Swagger UI**: http://localhost:8000/docs
- **API Base URL**: http://localhost:8000

## API Endpoints

### Job Applications CRUD

- `POST /applications/` - Create new job application
- `GET /applications/` - List all job applications  
- `PUT /applications/{id}` - Update existing job application
- `DELETE /applications/{id}` - Delete job application

### Health Check

- `GET /` - API status check