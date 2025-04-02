from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return "Hello, Flask!"

# Define a route for another page
@app.route('/demo')
def demo():
    return "<h1>This is a demo page!</h1>"

# Run the app if this script is executed
if __name__ == '__main__':
    app.run(debug=True)
