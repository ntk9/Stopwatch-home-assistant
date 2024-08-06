FROM python:3.9-slim

# Install necessary packages
RUN pip install flask flask-cors

# Add the app code
COPY timer.py /app/timer.py
COPY run.sh /app/run.sh

# Set the working directory
WORKDIR /app

# Make run.sh executable
RUN chmod +x run.sh

# Run the script
CMD ["/app/run.sh"]
