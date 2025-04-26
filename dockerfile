# Use Python base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy dependencies first and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into the container
COPY . .

# Set environment variables
ENV FLASK_APP=app.py

# Expose the port your Flask app runs on
EXPOSE 5000

# Run init_db.py first, then start Flask
CMD ["sh", "-c", "python init_db.py; flask run --host=0.0.0.0"]
