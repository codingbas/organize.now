# Final Milestone Full Stack with Django called Organize.now

A digital To Do list to help your life get more organized!

[![Build Status](https://travis-ci.org/codingbas/organize.now.svg?branch=master)](https://travis-ci.org/codingbas/organize.now)

To deploy this application with Heroku, click [here](https://organizenow.herokuapp.com)

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
* [HTML5](https://www.w3schools.com/html/html5_intro.asp)
    - This project uses HTML to build the foundation of the web application and includes links to Bootstrap 3, Bootstrap JS, CSS, and Font Awesome.
* [CSS](https://www.w3schools.com/css/)
    - This project uses CSS to style the features of the web application, including the header, footer and each page of the issue tracker. It is also used to modify Bootstrap 4 styles.
* [Javascript](https://www.w3schools.com/js/)
    - This project uses JavaScript to provide the functionality for the Stripe API and for the back-to-top button.
* [Python](https://www.python.org/)
    - This project uses Python to provide the backend functionality of the issue tracker, including functions to report bugs and request features.
* [Django](https://www.djangoproject.com/)
    - This project uses Django, a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
* [Stripe](https://stripe.com/en-nl)
    - This project uses the Stripe payment API, providing a secure payment form for the application.
* [JQuery](https://jquery.com/)
    - The project uses JQuery to simplify DOM manipulation.
* [Font Awesome](https://fontawesome.com/)
    - This project uses Font Awesome to provide icons for the application.
* [WhiteNoise](http://whitenoise.evans.io/en/stable/)
    - This project uses WhiteNoise to hose the staticfiles for Heroku. It provides radically simplified static file serving for Python web apps.
* [Balsamiq Mockups 3](https://balsamiq.com/wireframes/desktop/)
    - This project uses Balsamiq Mockups 3 for the Skeleton and Surface Plan, providing views of the web application.

# Testing

## Manual Testing
Below are scenarios which a user may experience while navigating the website. These have been used to manually test the application's features.

* Log in
    1.Click on 'Log in' in navigation bar
    2.Fill in your username and password
    3.Be presented with the message 'you have successfully logged in'
* Register
    1. Click on 'Register' button in the navigation bar
    2. Fill in the required fields
    3. Click on register button
    4. User has now a profile
    5. Be presented with the message 'you have successfully registered'
* Log out
    1. When a user clicks on 'Log out' when logged in in the navigation bar
    2. A message 'you have successfully logged out' will appear
* Profile
    1. Click on 'Profile' button in the navigation bar
    2. User can see his or her own Profile
    3. User can see if he or she is a premium member or not
    4. If a trial member user has the option the click on buy premium button
* Buy Premium
    1. Click on 'Buy Premium' button in the navigation bar
    2. User will then go to checkout url and be able to press button to buy
    3. User will have to fill in their emailaddress and cc information. Also their telephonenumber for security reasons.
    4. When they click on buy, the button will turn green and will go to premium
* Reset password
    1. When user wants to change their password or dont remember theirs then they can click on 'reset password'
    2. A message with 'Please specify your email address to receive instructions for resetting it' will appear.
    3. Then fill in the emailaddress you have chosen for your account and press 'reset password'
    4. The user will get a unique link in their emailaddress to change their password
* To Do trial version
    1. When user wants to make 11th todo a message appears 'It appears you have run out of your 10 todo's. Click on the button to buy Premium and unlimited ToDo's'
    2. Under that message is a button 'buy premium' to buy a premium version with unlimited todo's.
* Github page of codingbas
    1. When a user wants to see my Github page they can click in the footer on the Github icon.
* Back to top button
    1. Scroll down on the page of todo's or on your mobile and back to top btn appears
    2. A button on the bottom right should appear
    3. When a user clicks on this button he or she returns to the top of the page

## Responsive Testing
This website has been tested on different device screen sizes using Google Chrome Developer Tools and Mozilla Firefox Developer Tools. Minor bugs have been fixed as a result of this testing and I can confirm that this website functions responsively on all device screen sizes.

## Code Validation
HTML code has been passed through the official W3 Validator. Errors within the code have been corrected. CSS code has been passed through the official W3 Validator.

## Continuous Integration
For Continuous Integration I used Travis which constantly tests my app every time I push a new change to github

## Bugs
A lot of bugs have been solved and committed to GitHub every time.
A few examples I came accross:
1. Checkout didn't work for a long time. Got the message 'API key is not working'. Looked on Google for the answers and finally installed a easy Stripe checkout with security and less fields to fill in. 
    Also in my code I had to change to secret key and the publishable key and how they connect.
2. User in trial mode could make more then 10 todo's. Had to fix the issue in count().
3. The reset password didnt work. User didnt get an email to reset their password. Took me a while but the restrictions on the Gmail account weren't set properly.
4. The cart function i deleted because the user only buys 1 product: premium. Took me a long tim to change that.
5. Deployment to Heroku didnt went very well. Had to fix quit a lot of issues. 
6. The app on Heroku didnt work for a long time. Had to do migrate and makemigrations and restart all dynos to get it working.
7. For quit a long i didnt know i had to create a new superuser for database Heroku. 

# Deployment
To run this locally:
1. Create a new workspace in AWS Cloud9 or VSCode with a workspace name and description.
2. Create a virtual environment
3. Activate this virtual environment with mkvirtualenv [name of virtual environment].
4. Install requirements with pip3 install -r requirements.txt.
5. Create an env.py file with the following:
6. import os

os.environ.setdefault('STRIPE_PUBLISHABLE', "")
os.environ.setdefault('STRIPE_SECRET', "")
os.environ.setdefault('SECRET_KEY', '')
os.environ.setdefault('DATABASE_URL', '')

7. Make sure you uncomment #import env in settings.py.
8. You will need to generate your own SECRETKEY. You will need to set up a Stripe account and use their testing API keys. Once you have a database set up (you can use Postgres for database on Heroku) you can uncomment os.environ.setdefault('DATABASE_URL', '') and use the key that PostgreSQL generates for you in Heroku's Config Vars.
9. Make migrations with python3 manage.py makemigrations.
10. Migrate with python3 manage.py migrate.
11. Create a super user with python3 manage.py createsuperuser and follow instructions in your terminal.
12. To run the application locally, type in python3 manage.py runserver $IP:$C9_PORT.

## Heroku
To deploy this application with Heroku, click [here](https://organizenow.herokuapp.com)

1. Initialise a repository in the workspace with git init.
2. Create a repository on GitHub and type git remote add origin https://github.com/[github username]/[repo name].git into the terminal.
3. Use git status to outline all staged and unstaged files. Use git add to stage all files.
4. Add env.py to .gitignore with echo env.py >> .gitignore so that secret keys are not pushed to GitHub or Heroku.
5. Use git commit -m [message] to commit changes.
6. Use git push -u origin master to push these changes to GitHub.
7. Log into Heroku and Create New App. Create a unique name and region (USA or Europe, whichever is closest to you).
8. Navigate to Resources and search for 'PostgreSQL' - choose 'Hobby Dev - Free' and select 'Provision'. 
9. Go to Settings and Reveal Config Vars - copy and paste the SECRETKEY, STRIPEPUBLISHABLE and STRIPESECRET into the fields.
10. In env.py, uncomment DATABASE_URL and use the key generated from PostgreSQL in Heroku's Config Vars.
11. In Config Vars, add DISABLE_COLLECTSTATIC = 1.
12. Run python3 manage.py makemigrations and python3 manage.py migrate.
13. Create a new super user for the production database with python3 manage.py createsuperuser and follow instructions in the terminal.
14. pip3 freeze > requirements.txt to make sure requirements.txt is up to date. 
15. Create a Procfile and add web: gunicorn finalmilestone.wsgi:application
16. In settings.py, comment out import env and set DEBUG = False.
17. In Heroku, go to Deploy and select GitHub as a deployment method. Find your repository. Manually deploy the master branch. Activate automatic deploys.
18. Add the deployed Heroku link to ALLOWED_HOSTS in settings.py and git push origin master. The Heroku app should now be working.

Deployed version here: 


## Development vs Deployed Version
In the development version, Debug is set to True and the env.py file is imported into settings.py. However, in the deployed version, Debug is set to False and env.py is commented out. Also, the env.py file is not pushed to GitHub or Heroku as this contains keys which need to remain hidden from other users. The deployed version uses Heroku's PostgreSQL database whereas the development version uses SQLite.

# Credits
The accounts app i used came from the lessons of Code Institue. This app includes the functionality for logging in and registering a user into the database. The checkout of Stripe i used is from [stripe checkout](https://testdriven.io/blog/django-stripe-tutorial/). In my opinion very easy to use. 
The simple ToDo app is used comes from [simple Django ToDo app](https://medium.com/fbdevclagos/how-to-build-a-todo-app-with-django-17afdc4a8f8c). Also i want to give my credits to a senior developer called Luigi van der Pal, he helped me a lot during this milestone.
Also many thanks for the tutors. I have used the Tutoring a lot during this milestone and they were really helpful. 

