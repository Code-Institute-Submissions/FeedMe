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
@app.route("/home")
def home():
    return render_template("home.html")


# All Recipes
@app.route("/get_recipes")
def get_recipes():
    # convert the cursor object into a list
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


# Search for Recipes
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


# Register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if the username already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already in use.")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "email": request.form.get("email").lower()
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("You have been successfully registrated!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# Log In
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}!".format(request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # if the password is incorrect
                flash("Incorrect Username and/or Password!")
                return redirect(url_for('login'))

        else:
            # username doesn't exist/is incorrect
            flash("Incorrect Username and/or Password")
            return redirect(url_for('login'))

    return render_template("login.html")


# Profile
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # this will grab the session's user username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    recipes = list(mongo.db.recipes.find({"created_by": username.lower()}))

    # making sure that a user can't force into other users profile
    if session["user"]:
        return render_template("profile.html", username=username, recipes=recipes)

    return redirect(url_for("login"))


# Log Out
@app.route("/logout")
def logout():
    # informing the user that they've been logged out
    flash("You're now logged out")
    # removing session cookies
    session.pop("user")
    return redirect(url_for("login"))


# Add Recipe
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        favorite = "on" if request.form.get("favorite") else "off"
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_ingredients": request.form.getlist("recipe_ingredients"),
            "recipe_method": request.form.get("recipe_method"),
            "favorite": favorite,
            "date": request.form.get("date"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("You're recipe was successfully added")
        return redirect(url_for("get_recipes"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipe.html", categories=categories)


# Edit a Recipe
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        favorite = "on" if request.form.get("favorite") else "off"
        submit = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_ingredients": request.form.getlist("recipe_ingredients"),
            "recipe_method": request.form.get("recipe_method"),
            "favorite": favorite,
            "date": request.form.get("date"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("You're recipe was successfully updated")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_recipe.html", recipe=recipe, categories=categories)


# Delete a Recipe
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("You're recipe has been deleted")
    return redirect(url_for("get_recipes"))


# single recipe
@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipe.html", recipe=recipe)


# Categories
@app.route("/categories")
def categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


# Add Category
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("categories"))

    return render_template("add_category.html")


# Edit a Category
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("You're Category Has Been Updated")
        return redirect(url_for("categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


# Delete a Category
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("categories"))


# telling the app how and where to run the application
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)  # Make this False before project submission!!!
