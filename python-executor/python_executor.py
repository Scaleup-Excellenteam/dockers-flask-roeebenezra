import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def execute_python_code():
    code = request.form.get('code')

    # Execute the code using Python interpreter
    try:
        result = subprocess.run(['python', '-c', code], capture_output=True)
        output = result.stdout.decode().strip()
        error = result.stderr.decode().strip()
        return f'Output: {output}\nError: {error}' if error else f'Output: {output}'
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr.decode()}'

if __name__ == '__main__':
    app.run()
