# Django Blogging App

This is the simple blog created django web framework but it is a level up to a other normal blogging apps because in other blogging apps the only site manager could  post the blogs but here anyone could create an account and start blogging.

## Some Core Features
It allows user to create an account and login the page.
You can create blog very easily, it requires only a authenticated user and a creative mind.
This blogging app support the likes and comments on blogs.
The home page shows us latest 10 posts while all posts page shows us all posts.


## How it is made
The blog app is made through python web framework called django.
The authorization and authentication is done through the in-built django authentication backend.
I have use the users model and also uses different types of relationships like one to many relationship for blog post to its author and many to many relationship for likes.
The sign in , login and new blog forms are created through ModelForm class.
I have also used different type of class base generic views like listview, detailview, createview and formview.

## How to use
To use this code just clone this repository and run the command in powershell  

```shell
python manage.py runserver
```
