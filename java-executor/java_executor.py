import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def execute_java_code():
    code = request.form.get('code')
    file_name = 'Main.java'
    file_path = f'/path/to/java/files/{file_name}'

    # Save the code to a file
    with open(file_path, 'w') as file:
        file.write(code)

    # Compile and execute the code using JDK
    try:
        subprocess.run(['javac', file_path], check=True)
        result = subprocess.run(['java', '-classpath', '/path/to/java/files', 'Main'], capture_output=True)
        output = result.stdout.decode().strip()
        error = result.stderr.decode().strip()
        return f'Output: {output}\nError: {error}' if error else f'Output: {output}'
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr.decode()}'

if __name__ == '__main__':
    app.run()
