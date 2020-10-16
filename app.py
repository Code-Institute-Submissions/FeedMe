import os
from flask import Flask
if os.path.exists("env.py"):
    import env


# instance of Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return ("Hello world ... again!")


# telling the app how and where to run the application
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)  # Make this False before project submission!!!
