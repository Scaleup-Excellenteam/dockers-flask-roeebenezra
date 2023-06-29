# Use Alpine Linux as the base image
FROM alpine:latest

# Install required packages
RUN apk update && apk add openjdk11

# Set the working directory
WORKDIR /app

# Copy the application files
COPY java_executor.py .

# Install dependencies
RUN apk add --no-cache python3 && \
    pip3 install flask

# Expose the port
EXPOSE 5000

# Set the entrypoint command
CMD ["python3", "java_executor.py"]
