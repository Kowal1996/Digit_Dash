<p></p>

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Satisfy&weight=800&size=40&pause=1000&color=000000&width=435&lines=Digit+Dash+Website)](https://git.io/typing-svg)

## Table of contents

:sparkles: Technologies

:sparkles: Screenshots

:sparkles: Setup

:sparkles: General info

:sparkles: To Do

:sparkles: About

## Technologies

Project is created with:

:sparkles: HTML5, CSS and Bootstrap v5.3 

:sparkles: Python and Django 4.2.3 

:sparkles: SQLite 3.42.0
## Screenshots
#### Main page
![mainPage](/static/images/mainPage.png)

#### Leaderboards
![leaderboard](/static/images/leaderboard.png)

#### Registration
![registration](/static/images/registration.png)

#### Login
![login](/static/images/login.png)

#### Main page - Login user
![mainPageLoginUser](/static/images/mainPageLoginUser.png)

#### Profile information
![profileInformation](/static/images/profileInformation.png)

#### Game
![game](/static/images/game.png)

#### Game result
![gameResult](/static/images/gameResult.png)

#### User games
![userGames](/static/images/userGames.png)

#### About us
![aboutUs](/static/images/aboutUs.png)
## Setup

1. To download the repository use:
    ```
    git clone https://github.com/Kowal1996/Digit_Dash.git
    ```
2. Navigate to the project directory:
    ```
    $ cd Digit_Dash
    ```
3. (Optional) It is recommended to create and activate a Python virtual environment:
    ```
    $ virtualenv env
    $ env/Scripts/activate
    ```

4. Set the environment variables:
    
    *Create file .env in main folder
    *Add bellow lines into .env file:
    ```
    *SECRET_KEY=django-insecure-t#fg#d7jy20kji!7b0=pn#82$#zdaa@jm-8t7x72!7nc_kde
    *EMAIL_HOST_USER = 'digitdashsdaproject@gmail.com'
    *EMAIL_HOST_PASSWORD = 'gedlrlgxzujtkami'
    ```
5. Install required packages using:
    ```
    pip install -r requirements.txt
    ```
6. Run the Django development server:
    ```
    $ python manage.py runserver
    ```
The application will be available at http://localhost:8000/
## General info

We are the members of workshops from Software Development Academy (SDA). Our group had 40-class-hours to finish assumed mvp. The project was created in a four-person team. To created this apllication we create around 50'ty branches so far. At the beginning, our goal was to create a website that allows drawing numbers and typing them. Unfortunately, we have noticed that such an application will require more work from us than we assumed. So we created a simple game that allows users to draw one number and guess it. 
For now it is MVP realization. Our team plans to develop this project systematically. There are still areas that need to be perfected. The next goal is to implement our original assumption. During this project we improved technical knowledge and due to the teamwork we reafine: communication skills, listen carefully and openness to suggestions, tips and ideas of others.
This is a Django-basted website project which allow to relax and de-stress after a hard day at work. Actually, website consists of two individuals apps, each serving a specific purpose.

Below is an overview of each app and its features:

### Accounts App

The Accounts app facilitates user registration and login functionality. Key features include:

:sparkles: **User Registration**

*Allows users to create an account by providing necessary details such as username, email, password, first name, city, country, birth date. Registartion has to be confirmed by email. Users under 18 years old will not gain access to the application.* 

:sparkles: **User Login**

*Provides a secure login mechanism users to access additional features.*

:sparkles: **Password Change**

*Logged-in users can change their password.*

:sparkles: **Password Reset**

*Unauthenticate users can reset their password by email address.*

:sparkles: **Edit Profile**

*Logged-in users can edit their profil. User can change own city, country and picture.*

:sparkles: **Profile Information**

*Logged-in users can check all information about their profile and check their acctual account balance. From this lever user can change the password, check all their games with the reasults and delete own account.*

### LottoGames.App
		
:sparkles: **Game One Out Of Twenty**

*App offers game for logged-in users. User has 10 chances to guess the right number(lucky number). User chooses one number out of twenty. If user does not pick up a lucky number, he will get information whether the selected number is higher or lower than lucky number. Moreover, user can get maximum 10 ponits. Points are added to account balance.*

:sparkles: **Leaderboard**

*Logged-in and logged-out user can chcek the list which presents the current player results.*

:sparkles: **User Games**

*Logged-in users have the opportunity of checking all the games they played. There they can find information about how many games - One Out Of Twenty - they have played do far, dates the game, how many scores they got and lucky numbers which was drawn.*

## To Do:

:sparkles: Create an app which allows drawing numbers and typing them

:sparkles: Create blog where users can add posts about their achievements

:sparkles: Create a user level system f.ex (gold user, silver user etc)

:sparkles: Create the ability to play with other users

## About us
This project was created with :heart: by four-person team. Feel free to contact us:

:star: Anhelina Smuhliy
    [<img align="left" alt="linked-in" src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/anhelina-smuhliy-b20200288)

:star2: Jakub Jasiński
    [<img align="left" alt="linked-in" src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/jasinski-jakub/)

:star2: Kamila Czajkowska
    [<img align="left" alt="linked-in" src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/kamila-czajkowska/)

:star: Szymon Kowalski
    [<img align="left" alt="linked-in" src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/szymon-kowalski-843806257/)