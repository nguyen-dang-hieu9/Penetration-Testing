FROM python:3.9-slim-buster

# Copy the Python application code
COPY challenge /app

# Copy the flag
COPY flag.txt /flag.txt

# Install Python dependencies
RUN pip install  -r /app/requirements.txt

# Set the working directory
WORKDIR /app

# Add a test user
RUN adduser svc

# Change permissions 
RUN chown -R svc:svc /app

# Switch to svc user
USER svc

# Expose port 1337
EXPOSE 1337

# Start the Python application
CMD python app.py
