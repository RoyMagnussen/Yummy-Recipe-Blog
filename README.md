# Yummy! Recipe Blog

Yummy! Recipe Blog is a pay once membership site where food lovers are able to create and share recipes with other users of the site as well as gain inspiration for other dishes to make.

## Table of Content
- [Yummy! Recipe Blog](#yummy-recipe-blog)
  - [Table of Content](#table-of-content)
  - [UX](#ux)
    - [User Stories](#user-stories)
    - [Wireframes](#wireframes)
  - [Features](#features)
    - [Existing Features](#existing-features)
      - [1. Sign Up Page](#1-sign-up-page)
      - [2. Payment Page](#2-payment-page)
      - [3. Sign Up Complete Page](#3-sign-up-complete-page)
      - [4. Login Page](#4-login-page)
      - [5. Reset Password](#5-reset-password)
      - [6. Home Page](#6-home-page)
      - [7. Profile Page](#7-profile-page)
      - [8. Profile Update Page](#8-profile-update-page)
      - [9. Recipe Creation Page](#9-recipe-creation-page)
      - [10. Personal Recipes Page](#10-personal-recipes-page)
      - [11. Liked Recipes Page](#11-liked-recipes-page)
      - [12. Remove Liked Recipes](#12-remove-liked-recipes)
      - [13. Delete Recipe](#13-delete-recipe)
      - [14. Like A Recipe](#14-like-a-recipe)
      - [15. Edit A Recipe](#15-edit-a-recipe)
      - [16. Recipe Details](#16-recipe-details)
      - [17. Search Feature](#17-search-feature)
      - [18. User Page](#18-user-page)
      - [19. Recipe Sorter](#19-recipe-sorter)
    - [Features Left To Implement](#features-left-to-implement)
  - [Technologies Used](#technologies-used)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [Deploying To Heroku](#deploying-to-heroku)
    - [Deploying to a local machine](#deploying-to-a-local-machine)
  - [Credits](#credits)
    - [Media](#media)
 
## UX

### User Stories

| **User Story ID** |  **AS A/AN**   |           **I WANT TO BE ABLE TO…**            |                                         **SO THAT I CAN…**                                          | **DONE** |
| :---------------: | :------------: | :--------------------------------------------: | :-------------------------------------------------------------------------------------------------: | :------: |
|         1         | Potential User |         Easily sign up for an account          |                       Have a personal account and be able to view my profile                        |    ✔     |
|         2         | Potential User | Receive an email confirmation after signing up |                            Verify that my account sign up was successful                            |    ✔     |
|         3         |   Site User    |             Easily login or logout             |                               Access my personal account information                                |    ✔     |
|         4         |   Site User    | Easily recover my password in case I forget it |                                    Recover access to my account                                     |    ✔     |
|         5         |   Site User    |        Have a personalised user profile        |    View and edit my personal details such as name, username, profile picture, email and password    |    ✔     |
|         6         |   Site User    |                View my profile                 |          Look at all of the recipes that I have created, my liked recipes and my comments           |    ✔     |
|         7         |   Site User    |             View my liked recipes              |                             Find a specific recipe in my liked recipes                              |    ✔     |
|         8         |   Site User    |             Remove a liked recipe              |                                Remove it from the liked recipes list                                |    ✔     |
|         9         |   Site User    |             View a list of recipes             |                                     Select some recipes to use                                      |    ✔     |
|        10         |   Site User    |       Sort a specific category of recipe       |           Find the most liked recipe in the specific category or sort the recipes by name           |    ✓     |
|        11         |   Site User    |    Search for a recipe by name or category     |                               Find a specific recipe I'd like to use                                |    ✔     |
|        12         |   Site User    |          View the details of a recipe          |                  Find more information about it such as the ingredients and steps                   |    ✔     |
|        13         |   Site User    |          Visit another users' profile          |           Find more information about them and look at the recipes that they have created           |    ✔     |
|        14         |   Site User    |                Create a recipe                 |                                      Share it with other users                                      |    ✔     |
|        15         |   Site User    |                 Edit a recipe                  | Change the details of the recipe such as the name, the servings, ingredients, steps and the picture |    ✔     |
|        16         |   Site User    |                Delete a recipe                 |                                       Remove it from the site                                       |    ✔     |
|        17         |   Site User    |                 Like a recipe                  |       Support the author and save the recipe to my liked recipes list so I can find it easier       |    ✔     |

### Wireframes

The wireframes for the project can be found [here](docs/wireframes/yummy_recipe_blog_wireframes.pdf).

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features

#### 1. Sign Up Page

The `sign up` page allows users to create an account by getting them to provide the necessary information such as a username, email and password.

If the form is valid it will redirect the user to the `payment` page.

If the form is not valid it will reload the `sign up` page so that the users are able to input the correct details.

#### 2. Payment Page

The `payment` page allows the user to pay for the membership by getting the user to click the pay button which then redirects the user to the stripe checkout page where they are able to enter in their details.

Once they pay the membership, the user is then redirected to the `sign up complete` page.

The payment page is only accessible via POST requests, if the user tries to navigate directly to the `payment` page, it will redirect them to the `sign up` page.

This is to prevent the user from purchasing a membership without creating an account first.

#### 3. Sign Up Complete Page

The `sign up complete` page notifies the user that their account creation has been successful and that an email has been sent to the their email to confirm that it has.

The page also has a button to the `login` page where they are able to log in after they receive the email.

#### 4. Login Page

The `login` page allows the user to easily log in by them providing their username and password.

After they log in, the user is then redirected to the `home` page.

#### 5. Reset Password

The `reset password` page allows users to change their password by having an email sent to them with a one-time encoded link where they are then able to change their password and updated it by getting the user to provide their email address.

#### 6. Home Page

The `home` page allows users to view all of the recipes on the site. It currently only shows the recipes in order from oldest to newest. (Please view the features left to implement section).


#### 7. Profile Page

The `profile` page allows the user to view their information such as their name, username and profile picture by getting the user to navigate to the `profile` page by selecting the dropdown menu for the user ans clicking of the my profile link in the dropdown.

#### 8. Profile Update Page

The `profile update` page allows the user to update their information such as their profile picture, name, username, email and password by getting the user to click on the edit profile button in the `profile` page.

#### 9. Recipe Creation Page

The `recipe creation` page allows the user to create a recipe and share it with the other users of the site by providing the required information for the recipe to be created such as the name, servings, prep time, cook time, categories, ingredients and steps.

#### 10. Personal Recipes Page

The `personal recipes` page allows the user to view all of their personal recipes that they have created. It also allows the user to edit the recipe or delete the recipe.

#### 11. Liked Recipes Page

The `liked recipes` page allows the user to view all of their liked recipes in order for them to quickly find the recipe that they are looking for in order to use it.

#### 12. Remove Liked Recipes

The `remove liked recipe` function allows the user to easily remove a recipe from the users liked recipes just by clicking the delete button on the recipe card.

#### 13. Delete Recipe

The `delete recipe` function allows the user to easily delete a recipe from the users created recipes just by clicking the delete button on the recipe card on the `my recipes` page of the user profile.

#### 14. Like A Recipe

The `like recipe` function allows the user to quickly add the recipe into their liked recipes on their profile page.

#### 15. Edit A Recipe

The `edit recipe` page allows the user to add, remove or update the details of the recipe by getting them to update the form with the pre-populated information from the recipe.

#### 16. Recipe Details

The `recipe` page allows the user to view the details of a recipe such as the image, name, author, servings, prep time, cook time, categories, likes, ingredients and steps.

#### 17. Search Feature

The `search` feature allows the user to search for a specific recipe(s) and displays them on the home page.

#### 18. User Page

The `user page` allows the user to view another users profile and view all of their recipes that they have created.

#### 19. Recipe Sorter

The `recipe sorter` allows the user to sort the displayed recipes by either name in alphabetical order or by the total time it takes to complete the recipe.


### Features Left To Implement

- Cookie Policy Page
- Sitemap Page
- Category links in navigation

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.

- [HTML](https://html.com)
  - The project uses **HTML** for the structure of the web pages.

- [CSS](https://www.w3.org/)
  - The project uses **CSS** for the styling of the website.

- [Django](https://www.djangoproject.com/)
  - The project uses **Django** for the development of the websites.

- [Bootstrap](https://www.getbootstrap.com)
  - The project uses **Bootstrap** for the base styling for the website.)

- [Python](https://www.python.org)
  - The project uses **Python** for the data processing for the website.


## Testing

For this project I have created tests for each app and have divided them into separate files, one file for the views and one for the forms.

To run these tests, run the following command:

- Windows: `python manage.py test`
- Linux and Mac: `python3 manage.py test`

This will then search for all files that begin with test and will run each of the tests within those files.

I have tested the visuals of the website by using the built-in developer tools in browsers that were available to me. These include, Chrome, Edge, Firefox and Opera and I can say that they all displayed correctly on all screen sizes ranging from 320px (Small Mobile) to 2560px (4K).

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.

### Deploying To Heroku

These are the following steps that I had to take in order to deploy my project to Heroku:

1. I had to create a `requirements.txt` file which states which packages should be installed by using this command `pip3 freeze --local > requirements.txt`.
2. I created a `runtime.txt` file which states which version of python Heroku should install and use.
3. I had to create a `Procfile` which is a Heroku specific file which tells Heroku what type of application it should run as. I created this file using this command: `echo web: gunicorn yummy-recipe-blog.wsgi: application > Procfile`.
4. I then had to setup Amazon Web Services (AWS) by creating an account and creating a bucket for the static and media files.
5. I then also had to create a group and set the permissions for this group.
6. I then created a separate branch on github for the deployment.
7. On Heroku, I then configured the environment variables with these following values:
   ```
   AWS_ACCESS_KEY_ID=aws-access-key-id
   AWS_SECRET_ACCESS_KEY=aws-secret-access-key
   DATABASE_URL=postgres-database-url
   DEBUG=False
   EMAIL_HOST_PASSWORD=email-account-password
   EMAIL_HOST_USER=email-address
   SECRET_KEY=django-secret-key
   STRIPE_PUBLIC_KEY=stripe-public-key
   STRIPE_SECRET_KEY-stripe-secret-key
   USE_AWS=True
   ```
8. On Heroku, I then linked the repository for this project.
9. I then installed an addon on Heroku for a Postgres database and changed the settings of the Django project to connect to that database. I then had to run migrations so that the Postgres database has the tables that are used in the project.
10. I then scrolled to the bottom of the deployment page in Heroku and selected the `deployment` branch from the linked github repository and deployed the project to Heroku. Heroku then went and installed all of the required packages from the `requirements.txt` file and also installed the specified version of Python in the `runtime.txt` file.

### Deploying to a local machine

These are the steps that you will need to deploy the project on your computer and run it locally:

1. In this repository, go to the code dropdown menu and download the zipped version of the repository.
2. Once downloaded, unzip the folder and open with your editor of choice.
3. Once open, run the following command in a terminal:
    - Windows: `python -m venv venv`
    - Linux and Mac: `python3 -m venv venv`
   This creates a virtual environment within the project.
4. On Windows, navigate to the virtual environment folder going into the scripts folder and running the `activate.bat` file to activate it. To activate the virtual environment in Linux or Mac run the following command: `source venv/bin/activate`.
5. Once activated, run the following command:`pip install -r requirements.txt` which will read the `requirements.txt` file and install all of the packages that are declared within the file.
6. In the `settings.py` file that is located within the `yummy_recipe_blog` folder, uncomment the databases dictionary that contains the database as an sqlite3 database and comment the other databases dictionary that contains the database as a postgres database.
7. Within the same folder (yummy_recipe_blog) create a `.env` file and create the following variables:
```
DATABASE_NAME=db.sqlite3
EMAIL_HOST_PASSWORD=your-email-address-password
EMAIL_HOST_USER=your-email-address
SECRET_KEY=django-secret-key
STRIPE_PUBLIC_KEY=stripe-public-key
STRIPE_SECRET_KEY-stripe-secret-key
```
8. Once that is done, start the local web server with the following command:
   - Windows: `python manage.py runserver`
   - Linux and Mac: `python3 manage.py runserver`


## Credits

### Media
- The background image was obtained from [here](https://www.istockphoto.com/vector/seamless-pattern-supermarket-grocery-store-food-drinks-vegetables-fruits-fish-meat-gm1173579665-326026761?irgwc=1&esource=AFF_IS_IR_freevector.com_39452_&asid=freevector.com&cid=IS&utm_medium=affiliate&utm_source=freevector.com&clickid=R-KV00yqDxyLU3T0M-0V7wD0UkEQy3S%3AcSvYwc0&utm_term=freevector.com&utm_campaign=SRP&utm_content=718498&asset_type_keyword=_).
