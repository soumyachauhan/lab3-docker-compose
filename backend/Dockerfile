# Use official Python 3 base image
FROM python:3

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Run the Flask app
CMD ["python", "app.py"]
