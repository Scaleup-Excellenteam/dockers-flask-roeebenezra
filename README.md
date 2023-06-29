# dockers-flask-roeebenezra


```markdown
# Code Execution Application

This is a Flask application that allows you to execute code written in different programming languages. It consists of a router and language executors for Java, Python, and Dart.

## Features

- Accepts code files via POST requests and saves them to a temporary directory.
- Executes the code files based on the selected language using the corresponding language executor.
- Returns the execution result to the client.

## Prerequisites

- Docker
- Python 3
- Java Development Kit (JDK)
- Dart SDK

## Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   ```

2. Build the Docker images for the router and language executors:

   - Router:

     ```bash
     cd router/
     docker build -t router-image .
     ```

   - Java Executor:

     ```bash
     cd java-executor/
     docker build -t java-executor-image .
     ```

   - Python Executor:

     ```bash
     cd python-executor/
     docker build -t python-executor-image .
     ```

   - Dart Executor:

     ```bash
     cd dart-executor/
     docker build -t dart-executor-image .
     ```

3. Run the Docker containers:

   - Router:

     ```bash
     docker run -d -p 5000:5000 --name router-container router-image
     ```

   - Java Executor:

     ```bash
     docker run -d -p 5001:5001 --name java-executor-container java-executor-image
     ```

   - Python Executor:

     ```bash
     docker run -d -p 5002:5002 --name python-executor-container python-executor-image
     ```

   - Dart Executor:

     ```bash
     docker run -d -p 5003:5003 --name dart-executor-container dart-executor-image
     ```

4. Start the Flask client application:

   - Install the dependencies:

     ```bash
     pip install flask requests
     ```

   - Run the Flask application:

     ```bash
     cd client/
     python app.py
     ```

5. Access the client application by opening a web browser and navigating to `http://localhost:5000`.

## Usage

1. Select the programming language from the dropdown menu.
2. Enter the code you want to execute in the provided textarea.
3. Click the "Execute" button.
4. The execution result will be displayed on the page.
