from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_categories():
    
    return "Hello World!"

if __name__ == "__main__":

    app.run()  # Replace YOUR_PORT with your specified port
