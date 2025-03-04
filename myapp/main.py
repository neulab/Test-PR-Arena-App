# myapp/main.py
import os
from flask import Flask, render_template
from myapp.utils import format_message

app = Flask(__name__)

@app.route('/')
def index():
    name = 'User'
    timezone = os.getenv('APP_TIMEZONE', 'UTC')
    greeting = format_message(f"Hello, {name}!", timezone)
    return render_template('index.html', greeting=greeting)

if __name__ == '__main__':
    app.run(port=5000)

