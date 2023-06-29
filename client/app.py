from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute_code():
    code = request.form['code']
    language = request.form['language']
    
    # Determine the appropriate language executor URL based on the language
    executor_url = ""
    if language == 'java':
        executor_url = 'http://localhost:5001/execute'
    elif language == 'python':
        executor_url = 'http://localhost:5002/execute'
    elif language == 'dart':
        executor_url = 'http://localhost:5003/execute'

    # Send the code to the language executor for execution
    response = requests.post(executor_url, data={'code': code})
    result = response.text

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
