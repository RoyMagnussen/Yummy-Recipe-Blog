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
    - [Features Left to Implement](#features-left-to-implement)
      - [Recipe Sorter](#recipe-sorter)
  - [Technologies Used](#technologies-used)
  - [Testing](#testing)
  - [Deployment](#deployment)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Acknowledgements](#acknowledgements)
 
## UX

### User Stories

| **User Story ID** |  **AS A/AN**   |           **I WANT TO BE ABLE TO…**            |                                         **SO THAT I CAN…**                                          | **DONE** |
| :---------------: | :------------: | :--------------------------------------------: | :-------------------------------------------------------------------------------------------------: | :------: |
|         1         | Potential User |         Easily sign up for an account          |                       Have a personal account and be able to view my profile                        |    ✔     |
|         2         | Potential User | Receive an email confirmation after signing up |                            Verify that my account sign up was successful                            |    ✔     |
|         3         |   Site User    |             Easily login or logout             |                               Access my personal account information                                |    ✔     |
|         4         |   Site User    | Easily recover my password in case I forget it |                                    Recover access to my account                                     |   ✔      |
|         5         |   Site User    |        Have a personalised user profile        |    View and edit my personal details such as name, username, profile picture, email and password    |    ❌     |
|         6         |   Site User    |                View my profile                 |          Look at all of the recipes that I have created, my liked recipes and my comments           |    ❌     |
|         7         |   Site User    |             View my liked recipes              |                             Find a specific recipe in my liked recipes                              |    ❌     |
|         8         |   Site User    |             Remove a liked recipe              |                                Remove it from the liked recipes list                                |    ❌     |
|         9         |   Site User    |             View a list of recipes             |                                     Select some recipes to use                                      |    ✔     |
|        10         |   Site User    |       Sort a specific category of recipe       |           Find the most liked recipe in the specific category or sort the recipes by name           |    ❌     |
|        11         |   Site User    |    Search for a recipe by name or category     |                               Find a specific recipe I'd like to use                                |    ❌     |
|        12         |   Site User    |          View the details of a recipe          |                  Find more information about it such as the ingredients and steps                   |    ❌     |
|        13         |   Site User    |          Visit another users' profile          |           Find more information about them and look at the recipes that they have created           |    ❌     |
|        14         |   Site User    |                Create a recipe                 |                                      Share it with other users                                      |    ❌     |
|        15         |   Site User    |                 Edit a recipe                  | Change the details of the recipe such as the name, the servings, ingredients, steps and the picture |    ❌     |
|        16         |   Site User    |                Delete a recipe                 |                                       Remove it from the site                                       |    ❌     |
|        17         |   Site User    |                 Like a recipe                  |       Support the author and save the recipe to my liked recipes list so I can find it easier       |    ❌     |

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

The page also has a button to the `login` page where they are able to log in after they recieve the email.

#### 4. Login Page

The `login` page allows the user to easily log in by them providing their username and password.

After they log in, the user is then redirected to the `home` page.

#### 5. Reset Password

The `reset password` page allows users to change their password by having an email sent to them with a one-time encoded link where they are then able to change their password and updated it by getting the user to provide their email address.

#### 6. Home Page

The `home` page allows users to view all of the recipes on the site. It currently only shows the recipes in order from oldest to newest. (Please view the features left to implement section).

### Features Left to Implement

#### Recipe Sorter

The recipe sorter will allow the users to sort the recipes by name (ascending and descending) and by age (ascending and descending).

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.


## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X
