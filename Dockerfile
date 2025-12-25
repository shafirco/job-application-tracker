# Use official Python runtime as base image
FROM python:3.12-slim

# Set working directory in container
WORKDIR /app

# Install Poetry
RUN pip install --no-cache-dir poetry

# Configure Poetry to not create virtual environment
ENV POETRY_NO_INTERACTION=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

# Copy Poetry configuration files
COPY pyproject.toml poetry.lock* ./

# Install dependencies using Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --only main \
    && rm -rf $POETRY_CACHE_DIR

# Copy application code
COPY app/ ./app/

# Expose port 8000
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
