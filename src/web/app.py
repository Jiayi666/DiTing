from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to DiTing - Your customizable news aggregator!"

if __name__ == '__main__':
    app.run(debug=True)