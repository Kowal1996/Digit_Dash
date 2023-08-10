# Digit Dash Website

## Table of contents

:sparkles: General info

:sparkles:Technologies

:sparkles: Setup

:sparkles: Screenshots

:sparkles: To Do

:sparkles: About

## General info

|= This is a final project of Python bootcamp from Software Development Academy (SDA). Our group had 40-class-hours to finish that project. The project was finish in a four-person team. To created this apllication we create around 40'ty branches so far.
At the beginning, our goal was to create a website that allows drawing numbers and typing them. Unfortunately, we have noticed that such an application will require more work from us than we assumed. So we created a simple game that allows users to draw one number and guess it. 
For now it is MVP realization. Our team plans to develop this project systematically. There are still areas that need to be perfected. The next goal is to implement our original assumption. This is a Django-basted website project which allow to relax and de-stress after a hard day at work. Actually, website consists of two individuals apps, each serving a specific purpose.=|

Below is an overview of each app and its features:

### Accounts App

The Accounts app facilitates user registration and login functionality. Key features include:

:sparkles: **User Registration**

|=*Allows users to create an account by providing necessary details such as username, email, password, first name, city, country, birth date. Registartion has to be confirmed by email. Users under 18 years old will not gain access to the application.*=|

:sparkles: **User Login**

*Provides a secure login mechanism users to access additional features.*

:sparkles: **Password Change**

*Logged-in users can change their password.*

:sparkles: **Edit Profile**

*Logged-in users can edit their profil. User can change own city, country and picture.*


:sparkles: **Profile Information**

|=*Logged-in users can check all information about their profile and check their acctual account balance. From this lever user can change the password, check all their games with the reasults and delete own account.*=|

### LottoGames.App
		
:sparkles: **Game One Out Of Twenty**

|=*App offers game for logged-in users. User has 10 chances to guess the right number(lucky number). User chooses one number out of twenty. If user does not pick up a lucky number, he will get information whether the selected number is higher or lower than lucky number. Moreover, user can get maximum 10 ponits. Points are added to account balance.*=|

:sparkles: **Leaderboard**

*Logged-in and logged-out user can chcek the list which presents the current player results.*

:sparkles: **User Games**

|=*Logged-in users have the opportunity of checking all the games they played. There they can find information about how many games - One Out Of Twenty - they have played do far, dates the game, how many scores they got and lucky numbers which was drawn.*=|

## Technologies

Project is created with:

:sparkles: Bootstrap v5.3 

:sparkles: Django 4.2.3 

## Setup

To run this project, install it locally using:

```
pip install -r requirements.txt
```

## Screenshots
    * Main page
![mainPage](/static/images/mainPage.png) 

    * Leaderboards
![leaderboard](/static/images/leaderboard.png)

    * Main page - Login user
![mainPageLoginUser](/static/images/mainPageLoginUser.png)

    * Profile information
![profileInformation](/static/images/profileInformation.png)

    * Game
![game](/static/images/game.png)

    * Game result
![gameResult](/static/images/gameResult.png)

    * User games
![userGames](/static/images/userGames.png)

## To Do:

- [] add api
- [] create an app which allows drawing numbers and typing them
– [] create blog where users can add posts about their achievements
– [] create a user level system f.ex (gold user, silver user etc)
– [] create the ability to play with other users

## About
This project was created with :heart: by four-person team. Feel free to contact us:

:star: Anhelina Smuhliy
    [<img align="left" alt="linked-in" src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />]()

:star2: Jakub Jasiński
    [<img align="left" alt="linked-in" src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/jasinski-jakub/)

:star2: Kamila Czajkowska
    [<img align="left" alt="linked-in" src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/kamila-czajkowska/)

:star: Szymon Kowalski
    [<img align="left" alt="linked-in" src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />]()