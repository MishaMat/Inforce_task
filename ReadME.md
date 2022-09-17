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

and open in browser your localhost.

---

## Documentation

### 1. Url routes

> admin/
>
> restaurants/
>
>menu/
>
>create_restaurant/
>
>register_manager/
>
>managers/
>
>create_employee/
>
>employee/
>
>login/
>
>logout/
>
>today_menu/
>
>vote/<int:menu_id>/
>
>results/
>
>upload_menu/
___

## 2. Endpoints with post method

### 1.

> create_restaurant/

to create restaurant you will need:

- name
- rating (default - 1)
- contact_no (default - unknown)
- address (default - unknown)

Example:
> {"name":"Green Lion",<br>
> "rating":93,<br>
> "contact_no":"0878080008",<br>
> "address":"Zelena 2a"}
___

### 2.

> register_manager/

Manager is just simple django user with _i**s_staff=True**_
to create him you need:

- username
- first_name
- last_name
- email
- password

Example:
> {"username":"manager1",<br>
> "first_name":"Mike",<br>
> "last_name":"Vazovski",<br>
> "email":"manager@gmail.com",<br>
> "password":"root"}
___

### 3.

> create_employee/

Creating Emoloyee is almost the same but you need to add position. Only managers or superusers can create employees.

Example:
> {"username":"manager1",<br>
> "first_name":"Mike",<br>
> "last_name":"Vazovski",<br>
> "email":"manager@gmail.com",<br>
> "password":"root",<br>
> "position":"Python dev"}
___

### 4.

> login/

Example:
> {"username":"manager1",<br>
> "password":"root"}
___

### 5.

> upload_menu/

Only managers or superusers can upload menus.
To upload menu you need:

- restaurant id 
- menu 
- date (default - today)
- vote (deafult - 0)

Example:
>{"restaurant":2,<br>
> "menu":"1 - apple pie,2 - tea,"}
___





