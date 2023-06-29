# Use Alpine Linux as the base image
FROM alpine:latest

# Install required packages
RUN apk update && apk add python3 python3-dev py3-pip

# Set the working directory
WORKDIR /Docker & Flask Ex

# Copy the application files
COPY router.py .

# Install dependencies
RUN pip3 install flask

# Expose the port for communication with language executors
EXPOSE 5001 5002 5003

# Set the entrypoint command
CMD ["python3", "router.py"]
