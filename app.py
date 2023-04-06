# import the Flask dependency
from flask import Flask

# Create a New Flask App Instance
app = Flask(__name__)

# define the starting point (also known as the root)
@app.route('/')
def hello_world():
    return 'Hello world'