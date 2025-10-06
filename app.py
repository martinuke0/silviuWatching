from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<html><body><h1 style='text-align: center; margin-top: 20%; color: #007bff;'>Hello World!</h1></body></html>"

if __name__ == "__main__":
    app.run()