from flask_app import app


@app.route('/')
def hello(): 
    return 'Hello World'
