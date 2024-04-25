from flask import Flask

# Create a Flask app
app = Flask(__name__)

# Define a route for the root URL ('/')
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the app on port 80
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
