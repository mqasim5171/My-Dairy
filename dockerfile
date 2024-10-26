# Dockerfile
# Use the official Python image as the base
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the entire project folder, including templates and init_db.py
COPY . .

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development

# Expose the Flask port
EXPOSE 5000

# Run init_db.py first to create tables, then start the Flask app
CMD ["sh", "-c", "python init_db.py && flask run"]
