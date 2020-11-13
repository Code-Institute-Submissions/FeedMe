# FeedMe

Welcome to my third website!

This website was built as a **development milestone project** for the completion of the Data Centric Development module and it's part of the learning material for [Code Institute's](https://codeinstitute.net/about-us/) Fullstack Web Developer program.

A live **desktop demo** can be found [here](https://fidemi.herokuapp.com/).

The **source code** for this project can be found [here](https://github.com/gaspar91/FeedMe).


# Table of Contents

- [UX](#ux)
- [Design Process](#design-process)
- [User Stories](#user-stories)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Observations](#observations)
- [Deployment](#deployment)
- [Credits](#credits)


# UX

This website was built to be a cookbook in order to help users to find and share recipes, and to inspire them to cook.

The website offers users the opportunity to discover recipes by searching for them in the main recipes page, and sharing their own recipes with useful points of interest such as what type of ingredients are necessary, the preparation time, its difficulty, a photo display to motivate the user to see the recipe, and necessary tools to have in the kitchen.


# Design Process

You'll be able to view the sketches, wireframes, and mockups for this project in the **static** folder in the [Github project repository](https://github.com/gaspar91/FeedMe).

I used [Balsamiq](https://balsamiq.com/) to build the wireframes, so you might need the program in order to view some of the documents.


# User Stories

### User Story One:

As someone who doesn't like to waste time with giving too much detail, filling up a short and quick register or login form is really nice and motivates me to do it.

### User Story Two:

As a user I want to be able to access, search and share recipes.

### User Story Three:

It's important to me to have my own profile page so I can see my own recipes.

### User Story Four:

It's important to know which recipes are mine and which are not, by having an edit button when I see all the recipes in the main page.

### User Story Five:

As a user I would like to add, edit, update or delete my own recipes.

### User Story Six:

It's important that the recipes have photos to help users to have an idea of what the dish looks like.

### User Story Seven:

As a user it is important that I have the necessary information to cook a recipe, such as what ingredients I might need, how long does it take to make it and the steps I need to take.

### User Story Eight:

It's important to me to see what other users have cooked through social media, with images and other people's comments.

### User Story Nine:

Accessibility is fundamental for me, so if I can search for recipes when I'm walking or I'm far away from my computer I can just search for it on my phone or tablet.

### User Story Ten:

It is also important that there is a confirmation of what I'm doing, like when I've registered, logged in, added, edited or deleted a recipe.

### User Story Eleven:

It's important to me to be notified if the recipe I looked for doesn't exist.

### User Story Twelve:

As a user I would like to know more about what cooking tools are necessary to have in the kitchen.


# Features

### Existing Features
- When the user is logged out, all the pages contain a navigation bar with the logo in the top corner left, and the home, login, and register pages.
- The Homepage, when a user is logged out, contains social media icons in case the user wants to browse images and comments about the website.
- When the user is logged in, all the pages contain a navigation bar with the logo in the top corner left and the user can now access the other pages in the top center of the screen.
- In order to ensure that the user first knows what the website has to offer the homepage contains a “Start” button, In the middle of the screen, that leads to the "Login" page.
- In case the user doesn't have an account yet, it can be redirected to the register page and create an account.
- The "Profile" page provides a welcoming message with the user's name and the recipes that the user has added.
- The "Add Recipe" opens up a form where the user can create a new recipe.
- The user can search for its own recipes in the profile page.
- The user can only edit and delete recipes that belong to them.
- The user can only delete its own profile.
- Once In the “Recipes” page the user can browse, search and click on the available recipes.
- The user can search for recipes and if the recipe isn't available, a message will be displayed.
- In the "Recipes" page, it's possible for the user to see which recipe is theirs because it displays an edit button.
- When a recipe is clicked, it redirects the user to the recipe page which contains all the information about it, and encourages the user to check the "Cooking Tools" page.
- The "Cooking Tools" page promotes kitchen tools that are vital to have in order to cook the recipes displayed.
- If the user is the Admin then it can add new Categories and Tools or delete the existing ones.


### Features Left to Implement

- In future versions of the website, I would like to implement an image gallery for each recipe in order to make the recipe process easier to understand.
- I would like it to be possible for users to upload images from their phone or computer instead of inserting a URL.
- I would like it to be possible to add a feature to each recipe in order for the user to share it on social media or with contacts.
- It would be a positive experience for the user if each recipe had a comment section so other users could comment about the recipe.
- In the future I would like to limit the amount of recipes, tools and categories in a page in order to implement pagination.

# Technologies Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
  - The project uses HTML5 to construct the pages within the application.
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
  - The project uses CSS3 in order to style the HTML5 and Bootstrap elements and components.
- [Materialize (ver 1.0.0)](https://materializecss.com/)
  - The project uses the Materialize components for the design framework.
- [Jquery (ver 3.4.1)](https://jquery.com/download/)
  - The project uses the Jquery in order to make it much easier to use JavaScript.
- [Gitpod](https://www.gitpod.io/)
  - The project uses Gitpod as the primary IDE for coding.
- [Github](https://github.com/)
  - The project uses Github for remote storing of code online.
- [Balsamiq](https://balsamiq.com/)
  - The project uses Balsamiq to create wireframes.
- [Adobe Xd CC](https://www.adobe.com/pt/products/xd.html)
  - The project uses Adobe Xd CC to create mockups.
- [Flask (ver 1.1.2)](https://flask.palletsprojects.com/en/1.1.x/)
  - The project uses Flask as a microframework.
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
  - The project uses Jinja for templating with Flask.
- [Werkzeug (ver 1.0.1)](https://werkzeug.palletsprojects.com/en/1.0.x/)
  - The project uses Werkzeug for password hashing, authentication and authorisation.
- [Heroku](https://www.heroku.com/)
  - The project uses Heroku for app hosting.
- [Python](https://www.python.org/)
  - The project uses Python as a programming language.
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
  - The project uses MongoDB Atlas as a cloud database service.


# Testing

**1. Logo:**

   1. If you're logged out, go to a page that is not the homepage.
   2. Try to click on the logo and verify that it leads you to the homepage.
   3. If you're logged in, go to a page that is not the recipes page.
   4. Try to click on the logo and verify that it leads you to the recipes page.

**2. Navigation Bar Pages:**

   1. Go to the navigation bar.
   2. Hover over the pages and verify that their background changes color individualy.
   3. Try to click on them and verify that you are able to go to the page you selected.
   4. Register and login as Admin and verify that "Categories" and "Add Tool" is added to your navigation bar.

**3. Add Recipe:**

   1. Go to the Add Recipe page.
   2. Try to click on categories and verify that the available categories appear.
   3. Try to do the same in difficulty field and verify that the available levels appear.
   4. Try to leave the fields empty and verify that a red line appears, indicating that it's a required field.
   5. Try to cick the clock icon and verify that a pop up shows to select the time.
   6. Try to submit the recipe and verify that a confirmation message appears.
   7. Go to your profile and verify that your recipe was added.

**4. Edit Recipe:**
    
   1. Go to your profile and select a recipe.
   2. Try to click on the edit button and verify that it opens a form with the information about the recipe.
   3. Try to change the information in any field.
   4. Try to click on the cancel button and verify that a pop up message appears asking if you're sure you want to cancel.
   5. Try to click yes and verify that it leads you back to your profile, or click no and verify that you continue to edit the recipe.
   6. Try to click on the save button and verify that a confirmation message appears and you can see the new changes.
   7. Go to your profile and verify that your recipe was edited.

**5. Delete Recipe:**

   1. Go to your profile and select a recipe.
   2. Try to click on the edit button and verify that it opens a form with the information about the recipe.
   3. Try to cick on the delete button and verify that a pop up message appears asking if you're sure you want to delete the recipe.
   4. Try to click no and verify that you continue to edit the recipe, or click yes and verify that it leads you to the recipes page and a confirmation message appears.
   5. Go to your profile and verify that your recipe has been deleted.

**6. Add Categories:**

   1. Register and login as Admin.
   2. Try to click on "Categories" and verify that it leads you to the Categories page.
   3. Try to add a category an verify that it leads you to the add category page with a form to fill.
   4. Press the add category button and verify that the new category is displaying in the Categories page.
   5. Try to add a new recipe and verify that the new category appears when selecting the category in the recipe form.

**7. Delete Categories:**

   1. Register and login as Admin.
   2. Try to click on "Categories" and verify that it leads you to the Categories page.
   3. Try to click the delete button on one of the categories and verify that a pop up message appears asking if you're sure you want to delete the category.
   4. Try to click no and verify that you go back to the categories page, or click yes and verify that it leads you to the categories page and a confirmation message appears.
   5. Verify that the category is no longer in the Categories page.

**8. Add Tools:**

   1. Register and login as Admin.
   2. Try to click on "Cooking Tools" and verify that it leads you to the Tools page.
   3. Try to click on "Add Tool" and verify that it leads you to the add tool page with a form to fill.
   4. Try to leave the form empty and verify that a red line appears, indicating that it is required to fill.
   5. Press the add tool button and verify that the new tool is displaying in the Tools page.

**9. Delete Tools:**

   1. Register and login as Admin.
   2. Try to click on "Cooking Tools" and verify that it leads you to the Tools page.
   3. Try to click on a tool and verify that it leads you to the tool page.
   4. Try to click on the delete button and verify that a pop up message shows up, asking if you're sure you want to delete the tool.
   5. Press no and verify that it leads you back to the tools page, or press yes and verify that it leads you back to the tools page with a confirmation message.
   6. Verify that the tool is no longer in the tools page.

**10. Edit Profile:**

   1. Go to your profile and press the edit button and verify that it leads you to the edit profile with a form containing your information.
   2. Change your password and/or email and press save and verify that it leads you back to your profile with a confirmation message.
   3. Try to login with your username and new password and verify that it confirms it.
   4. Try to login with your old password and verify that a message appears suggesting that your username or password is incorrect.

**11. Delete Profile:**

   1. Go to your profile and press the edit button and verify that it leads you to the edit profile with a form containing your information.
   2. Press the "delete" button and verify that a pop up message appears, asking you if you're sure you want to delete your profile.
   3. Press no and verify that it leads you back to your profile, or press yes and verify that it leads you to the register page and a confirmation message shows up.
   4. Try to login with your information and verify that the username doesn't exist.

**12. Social Media Icons:**
   1. Hover over the social media icons and verify that they change color individualy.
   2. Try to click on any social media icon and verify that it opens a new page.


# Observations

- The website has been checked for responsiveness on a multitude of screen sizes from PC to portable devices, such as tablets and mobile phones.

- All HTML code was run through the [W3C HTML Validator](https://validator.w3.org/) and returned some errors about the pages not starting with a document type declaration.


# Deployment

The website is hosted via [GitHub](https://github.com/), with the source code being available on [my repository](https://github.com/gaspar91/FeedMe).

### Requirements

- **Python3** to run your application
- **PIP** to install all app requirements
- **IDE** of your choice - I used Gitpod
- A **MongoDB Atlas** account for database development


### How To Access It
- In order to run this project locally you should follow these steps:

    1. Click the green *'clone or download'* button in the [GitHub repository](https://github.com/gaspar91/FeedMe) for the project.

    2. Copy the link provided by clicking the **clipboard button** to the right of the link.

    3. In your terminal, type ***git clone***, paste in the previously copied link, and hit return.

    4. Create a file called ".flaskenv" and add the following:
        - **FLASK_APP=run.py**
        - **FLASK_ENV=development**

    5. Install the required modules with the command **pip -r requirements.txt**.

    6. If you don't have it yet, create a free account on [MongoDB](https://mongodb.com/) and create a new Database called **Database3**.

    7. Then create the following collections in that Database:
        - **categories**
            - **_id:**< ObjectId >
            - **category_name:**< string >
            - **category_image:**< string >
        
        - **difficulty**
            - **_id:**< ObjectId >
            - **level:**< string >
        
        - **recipes**
            - **_id:**< ObjectId >
            - **category_name:**< string >
            - **recipe_name:**< string >
            - **recipe_description:**< string >
            - **recipe_ingredients:**< string >
            - **recipe_method:**< string >
            - **recipe_image:**< string >
            - **time:**< string >
            - **difficulty:**< string >
            - **created_by:**< string >
        
        - **difficulty**
            - **_id:**< ObjectId >
            - **tool_name:**< string >
            - **tool_description:**< string >
            - **tool_details:**< string >
            - **tool_image:**< string >
        
        - **users**
            - **_id:**< ObjectId >
            - **username:**< string >
            - **password:**< string >
            - **email:**< string >
    
    8. You should now be able to run this application locally by typing **flask run**.


### Deployment to Heroku

   1. Create a **requirements.txt** file by typing **pip3 freeze --local > requirements.txt** into the terminal line.

   2. Create a Procfile by typing **echo web: python app.py > Procfile**.

   3. Add, commit and push these changes to Github.

   4. Navigate to the [Heroku](https://heroku.com/).

   5. Create new app and give it a unique name.

   6. Choose the region that is closest to you.

   7. Go to the **Deploy** tab and choose **Github**.

   8. Search for the correct repository and connect.

   9. Go to Heroku **Settings** and navigate to **Config Vars**.

   10. Set the following:
        - **IP = 0.0.0.0**
        - **MONGO_DBNAME = [Name of MongoDB]**
        - **MONGO_URI = mongodb+srv://:@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority**
        - **PORT = 5000**
        - **SECRET_KEY = [Secret key]**


   11. Go to the Deploy tab and **Deploy Branch**, ensuring that the master branch is selected.

# Credits

### Content 

 - The code for the **navigation bar, forms and views** was duplicated from [Code Institute's Task Manager Project](https://github.com/Code-Institute-Solutions/TaskManager/tree/flask-rebuild-2020)
 - The code for the **social media** was duplicated from [Code Institute's Love Running Project](https://github.com/Code-Institute-Org/love-running-rebuild)

### Media

The photos used in this website were obtained from [Unsplash](https://unsplash.com/)

### Acknowledgements

I received inspiration for this project from:

- [Code Institute](https://codeinstitute.net/)
- [Behance](https://www.behance.net/)
- [ww3Schools](https://www.w3schools.com/)
- [Stack Overflow](https://stackoverflow.com/)