# Wedding Gallery

Image gallery for saving and sharing all your friend's photos and memories!

## Requiremetns:
- Python 3.6+
- OS: MacOS and Ubuntu (tested), should work on Windows environment
- Database: SQLite (tested), should work on any other Database supported by SQLAlchemy

## Development Setup:

```
$ export FLASK_APP=/path/to/project/wedding_gallery/__init__.py
$ export SQLALCHEMY_DATABASE_API=/path/to/project/wedding_gallery/__init__.py
$ flask db migrate
```

After project setup, there will be Three users and some photos inserted on database

The initial usernames are:
- husband
- wife
- friend

Passwords are the same as username

NOTE: To run in a Production environment it's suggested to use uWSGI and Nginx. Here is a useful link to do it:
https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-14-04


## Usage:

To run the project:
```
flask run
```

"Anonymous" (not logged) users can only see/sort the Gallery images or Signin

Simple users can, in addition to previous actions, can Like and Upload Photos

"Master" users, in addition to previous actions, can manage Users and Approve Photos

It's possible to Create New Users and Delete Users


## How To:
- You can go to Home Screen whenever you want by clicking on `Gallery` at Top Right of your screen

- Login:
   1. Top right of the screen, Click `Login`
   2. Provide your credentials
   3. Click `Login`
   4. This Option will be replaced by `Logout` option

- Like/Dislike: There is a `Like` button below each photo, simply click it (also shows Like counts)

- Upload Photo:
   1. Login
   2. After Loging in, a new Option called `Upload Photos` should appear at Top Left of the screen, click it
   3. Click on `Choose Files`
   4. Select your files
   5. Click on `Upload`

- Delete Users:
  1. Login with a "Master" user
  2. Click on `Users` at the Top Bar
  3. Select Users to Delete and Click `Delete`
  4. Warning: Do not remove all master users

- Create User:
  1. Login with a "Master" user
  2. Click on `Users` at the Top Bar
  3. Click `Create User`
  4. Fill the form (there is a checkbox for "Master" User)
  5. Click on `Create User` button


- Approve Photos:
  1. Login with a "Master" user
  2. Click on `Approve Photos` at the Top Bar
  3. Select photos to be approved
  4. Click on `Approve Selected` button


## To do
- Edit User
- Prevent from removing all users
- Send files to a Cloud Storage
- Unnaprove Photos
- Remove Photos
