# Use Alpine Linux as the base image
FROM alpine:latest

# Set the working directory
WORKDIR /Docker & Flask Ex

# Copy the application files
COPY python_executor.py .

# Install dependencies
RUN apk add --no-cache python3 python3-dev py3-pip && \
    pip3 install flask

# Expose the port for communication with the router
EXPOSE 5002

# Set the entrypoint command
CMD ["python3", "python_executor.py"]
