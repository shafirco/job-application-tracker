# Job Application Tracker

A professional RESTful API backend for tracking job applications built with modern Python technologies and best practices.

## Tech Stack

- **FastAPI** - Modern Python web framework with automatic API documentation
- **SQLAlchemy** - Async ORM with declarative models
- **PostgreSQL 17** - Latest stable PostgreSQL with psycopg3 async driver
- **Poetry** - Modern Python dependency management with lock files
- **Docker** - Containerization for consistent deployment
- **Pydantic** - Data validation and serialization with type hints

## Project Structure

This project follows professional Python packaging standards with a clean, scalable architecture:

```
job-tracker/
├── src/
│   └── job_tracker/                 # Main application package
│       ├── __init__.py              # Package exports
│       ├── main.py                  # FastAPI app factory
│       ├── api/                     # API endpoints
│       │   ├── deps.py              # Shared dependencies
│       │   └── v1/                  # API version 1
│       │       └── applications.py  # Application endpoints
│       ├── core/                    # Core functionality
│       │   ├── config.py            # Application settings
│       │   └── database.py          # Database connection
│       ├── models/                  # SQLAlchemy models
│       │   ├── base.py              # Base model class
│       │   └── application.py       # Application model
│       └── schemas/                 # Pydantic schemas
│           └── application.py       # Application schemas
├── tests/                          # Test suite (future)
├── docker-compose.yml              # Multi-service setup
├── Dockerfile                      # Container definition
├── pyproject.toml                  # Poetry configuration
└── poetry.lock                     # Locked dependencies
```

## Architecture Benefits

- **Scalable**: Easy to add new models, endpoints, and features
- **Maintainable**: Clear separation of concerns
- **Testable**: Each component can be tested independently
- **Professional**: Follows Python packaging best practices
- **Type-Safe**: Full type hints throughout

## Environment Configuration

The application uses environment-based configuration with sensible defaults:

```env
DATABASE_URL=postgresql+psycopg://postgres:password@db:5432/jobtracker
SECRET_KEY=your-secret-key-here
```

**Note**: The `.env` file is not committed to version control for security.

## Local Development

### Prerequisites

- Python 3.11+
- Poetry (install from https://python-poetry.org/docs/#installation)
- PostgreSQL 17 (or use Docker)

### Quick Start

1. **Clone and setup:**
   ```bash
   git clone <repository-url>
   cd job-tracker
   poetry install
   ```

2. **Configure environment:**
   ```bash
   cp .env.example .env  # Edit with your settings
   ```

3. **Start development server:**
   ```bash
   poetry run uvicorn src.job_tracker.main:app --reload
   ```

### Dependency Management

Poetry provides deterministic builds and easy dependency management:

```bash
# Install dependencies
poetry install

# Add new dependency
poetry add package-name

# Add development dependency  
poetry add --group dev pytest

# Update dependencies
poetry update

# Enter virtual environment
poetry shell
```

## Docker Deployment

### Development Environment

Start the entire stack (API + PostgreSQL):

```bash
docker compose up --build
```

This provides:
- **FastAPI API**: http://localhost:8000
- **PostgreSQL 17**: localhost:5432
- **Persistent data**: Named volume for database

### Production Deployment

```bash
# Build production image
docker build -t job-tracker-api .

# Run with external database
docker run -e DATABASE_URL="postgresql+psycopg://..." job-tracker-api
```

## API Documentation

### Interactive Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI Schema**: http://localhost:8000/api/v1/openapi.json

### API Endpoints

**Base URL**: `http://localhost:8000/api/v1`

#### Job Applications

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/applications/` | Create new job application |
| `GET` | `/applications/` | List all job applications |
| `PUT` | `/applications/{id}` | Update job application (partial updates supported) |
| `DELETE` | `/applications/{id}` | Delete job application |

#### Health Check

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | API status and version info |

### Example Usage

```bash
# Create application
curl -X POST "http://localhost:8000/api/v1/applications/" \
  -H "Content-Type: application/json" \
  -d '{
    "company_name": "Tech Company",
    "position": "Senior Developer",
    "status": "Applied",
    "applied_date": "2024-12-22",
    "notes": "Interesting opportunity"
  }'

# Get all applications
curl "http://localhost:8000/api/v1/applications/"

# Partial update (only update status)
curl -X PUT "http://localhost:8000/api/v1/applications/1" \
  -H "Content-Type: application/json" \
  -d '{"status": "Interview"}'
```

## Development Features

- **Async/Await**: Full async support with psycopg3
- **Type Safety**: Complete type hints with Pydantic validation
- **Auto-reload**: Development server watches for changes  
- **API Versioning**: Built-in support for API evolution
- **Partial Updates**: PATCH-style updates for efficiency
- **Field Documentation**: Auto-generated API docs with field descriptions
- **Error Handling**: Consistent error responses with proper HTTP status codes

## Testing

```bash
# Run tests (when implemented)
poetry run pytest

# Run with coverage
poetry run pytest --cov=src/job_tracker
```

## Database Schema

### Applications Table

| Column | Type | Description |
|--------|------|-------------|
| `id` | Integer | Primary key (auto-increment) |
| `company_name` | String | Company name (required) |
| `position` | String | Job position title (required) |
| `status` | String | Application status (required) |
| `applied_date` | Date | Application date (required) |
| `notes` | Text | Additional notes (optional) |

## Contributing

1. Follow the existing code structure
2. Add type hints to all functions
3. Include docstrings for public methods
4. Update tests for new features
5. Use conventional commits

## License

[Add your license here]

---

Built with ❤️ using modern Python best practices.