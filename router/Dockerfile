# Use Alpine Linux as the base image
FROM alpine:latest

# Install required packages
RUN apk update && apk add python3

# Set the working directory
WORKDIR /app

# Copy the application files
COPY router.py .

# Install dependencies
RUN pip3 install flask

# Expose the port
EXPOSE 5000

# Set the entrypoint command
CMD ["python3", "main_app.py"]
