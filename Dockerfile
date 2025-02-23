# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt to the working directory
COPY requirements.txt .

# Update pip to the latest version
RUN pip install --no-cache-dir --upgrade pip

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
# COPY src /app
# COPY .env /app

COPY src .
COPY .env .

# Expose the port FastAPI runs on
EXPOSE 8000

# Command to run the application
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

#CMD ["python", "main.py"]
CMD ["python", "kafka_producer.py"]