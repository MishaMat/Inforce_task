Hello,
---
firstly you need to write command
> pip install -r requrements.txt

also you need to run you PostgreSQL server with such parameters
>        "NAME": "postgres",
>        "USER": "postgres",
>        "PASSWORD": "postgres",
>        "HOST": "localhost" or "127.0.0.1",
>        "PORT": "5432",

next, you need to make migrations
> python manage.py makemigrations

> python maname.py migrate


That's all now you can run server using command
> python manage.py runserver

