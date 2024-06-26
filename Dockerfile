# Dockerfile
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt requirements.txt

# Install the dependencies
RUN pip install -r requirements.txt
RUN pip install sentencepiece

# Copy the application files
COPY . .

# Expose the port the app runs on
EXPOSE 5000
# New Change 3
# Command to run the application 
CMD ["python", "app.py"]
