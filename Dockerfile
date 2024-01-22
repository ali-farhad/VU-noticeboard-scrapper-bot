# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container to /app
WORKDIR /app


ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install requests beautifulsoup4

# Make port 80 available to the world outside this container
EXPOSE 80

# Run scraper.py when the container launches
CMD ["python", "scraper.py"]
