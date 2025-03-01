# Stage 1: Dependency Installation
FROM python:3.12-slim AS builder

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_DEFAULT_TIMEOUT=100 \
    VENV_PATH="/opt/venv"

# Install required system dependencies first (to leverage caching)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment (separate from system Python)
RUN python -m venv $VENV_PATH
ENV PATH="$VENV_PATH/bin:$PATH"

# Copy only requirements file first for better caching
COPY requirements.txt requirements.txt

# Install dependencies *before* copying source code
RUN pip install --upgrade pip && pip install -r requirements.txt

# Stage 2: Runtime Environment
FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PATH="/opt/venv/bin:$PATH"

# Copy virtual environment from builder stage
COPY --from=builder /opt/venv /opt/venv

# Set the working directory
WORKDIR /app

# Expose the port FastAPI runs on
EXPOSE 8000

# Copy the application code *after* dependencies (to maximize caching)
#COPY . .
COPY src .
COPY .env .

# Default command
CMD ["python", "main.py"]
