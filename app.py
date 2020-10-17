import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


# instance of Flask
app = Flask(__name__)

# grab the database name
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
# configure the connection string (uri)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
# grab the secret key
app.secret_key = os.environ.get("SECRET_KEY")

# establishes a propper communication with the MongoDB database
mongo = PyMongo(app)


# Homepage
@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)



@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")


# telling the app how and where to run the application
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)  # Make this False before project submission!!!
