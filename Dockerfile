# Use an official Python image as the base
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app


# Copy all files from your project to the container
COPY . .


# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Expose the port (if your app runs on port 5000)
EXPOSE 5000


# Run the application
CMD ["python", "app.py"]

