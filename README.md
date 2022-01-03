Article App
====

1. Install git package to the system

        pip install Flask
        pip install Flask-SQLAlchemy
        pip install flask-marshmallow
        pip install marshmallow-sqlalchemy
        pip install psycopg2
        pip install flask-restx
        pip install Flask-Cors


2. create DB (postgres)

         app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:123456@localhost/flask'

         python
         from app import db
         db.create_all() 
         exit()        


screenshot swagger on heroku
====

Link [https://articleflask.herokuapp.com/](https://articleflask.herokuapp.com/)

1. img_1

   ![](home_page.jpg)
   
