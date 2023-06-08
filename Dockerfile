# Use an official Python runtime as the base image
FROM python:3.8-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files to the working directory
COPY . .

# Expose the port on which the Django development server will run
EXPOSE 8000

# Set the environment variables
ENV DJANGO_SETTINGS_MODULE=weatherapp.settings

# Run the Django development server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
