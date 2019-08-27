# Final Milestone Full Stack with Django called Organize.now

A digital To Do list to help your life get more organized!

[![Build Status](https://travis-ci.org/codingbas/organize.now.svg?branch=master)](https://travis-ci.org/codingbas/organize.now)

## UX 
This web application is a simple ToDo app made in Django. You can have a trial version where you can make 10 ToDo's. When you buy the premium version you have unlimited ToDo's. It is designed to allow users to make any todo what they normally write down on paper. You will have the user whom wants to use the trial version and make sure the 10 ToDo's are finished on time. 
The premium user will have all their ToDo's online to have a great overview what to do per day, week or month. 

General User Stories:

* As a user type, I want to be able to create an account with my own username and password, and login with these credentials each time I want to access the application.
* As a user type, I would like to be able to login and make a ToDo.
* As a user type, I would like to be able to login and delete a ToDo.
* As a user type, I would like to be able to login and add a ToDo.

Real Life User Stories:

* User 1: I'd like my username to be 'USER1' and would also like to have my own password when logging in.
* User 2: I would like to be able to add a Task whenever I want. 
* User 3: I would like to be able to make a ToDo on my mobile.
* User 4: I would like to be able to delete a ToDo whenever possible.
* User 5: I would love to make as much ToDo's as I would like too in the Premium version.
* User 6: I would like to see all the ToDo's i have in my account. 

Wireframes:

* Wireframes have been created using Balsamiq Mockups 3. These can be viewed in ......

# Features
* Login/Register form - this will allow the user to either log into an existing account or create a new account, inserting them into the database.
* Password reset - this will allow the user to choose a different password when its lost or for security reasons.
* Add Todo - this will add a Todo to the list of Todo's.
* Delete Todo - this will delete an existing Todo.
* Buy Premium - This will allow the user to go for unlimited Todo's.
* Trial version - This is for free and will allow the user to make a maximum of 10 Todo's.
* Max 10 todod's - A warning comes up when a free trial user wants to make their 11th Todo.
* But Premium - This will allow the user to buy a premium version with Stripe and their creditcard. Inserting them in the database. 
* Profile - This will allow the user to see their own made profile whom is inserted in the database. 

## Existing Features
* Login/Register form - allows User 1 to have their username as 'USER1' and also their own password.
* Add Todo - allows trial user to make a maximum of 10 Todo's.
* Add Todo Premium - allows trial user to make unlimited Todo's.
* Stripe - allows user to pay 30 euro for the Premium version.
* Trial user and Premium user - user is premium then unlimited todo's.
* Log out - allows signed up user to log out after using the application (if they wish).
* Reset password - user will get an email with a link to reset their password. 

## Features Left to Implement
* Unlimited sharing - share your Todo's on different platforms and connect with Google Agenda.
* Add subcategories and priority to a Todo.
* Newsletter Subscription - there could be a newsletter subscription to keep users motivated and using the Todo app.
* Give your tags a color
* Advanced sorting todos
* Connect with Dropbox and Google Drive
* On your watch with Apple Watch
* Synch with Microsoft Outlook

# Technologies Used
* HTML
This project uses HTML to build the foundation of the web application and includes links to Bootstrap 4, Bootstrap JS, CSS, and Font Awesome.
* CSS
This project uses CSS to style the features of the web application, including the header, footer and each page of the issue tracker. It is also used to modify Bootstrap 4 styles.
* JavaScript
This project uses JavaScript to provide the functionality for the Stripe API and for the back-to-top button.
* Python
This project uses Python to provide the backend functionality of the issue tracker, including functions to report bugs and request features.
* Django
This project uses Django, a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
* Stripe
This project uses the Stripe payment API, providing a secure payment form for the application.
* JQuery
The project uses JQuery to simplify DOM manipulation.
* Font Awesome
This project uses Font Awesome to provide icons for the application.
* WhiteNoise
This project uses WhiteNoise to hose the staticfiles for Heroku. It provides radically simplified static file serving for Python web apps.
* Balsamiq Mockups 3
This project uses Balsamiq Mockups 3 for the Skeleton and Surface Plan, providing views of the web application.
