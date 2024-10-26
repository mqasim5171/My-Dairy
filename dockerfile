# Use the official Python image as the base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to install dependencies
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files to the container
COPY . /app/

# Expose both Flask and Django ports
EXPOSE 5000 8000

# Run both Django and Flask apps using a process manager (supervisord)
CMD ["supervisord", "-c", "/app/supervisord.conf"]

