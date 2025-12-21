# Job Application Tracker

A RESTful API backend for tracking job applications built with FastAPI, SQLAlchemy, and PostgreSQL.

## Tech Stack

- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - Python SQL toolkit and ORM
- **PostgreSQL** - Production-grade relational database
- **Docker** - Containerization for easy deployment
- **Pydantic** - Data validation and serialization

## Environment Variables

The application uses environment variables for configuration. Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://postgres:password@db:5432/jobtracker
```

**Note**: The `.env` file is not committed to version control for security reasons.

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
