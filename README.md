[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

Training django and DRF project.

Part of [Open Classrooms](https://openclassrooms.com) "DA Python" formation, 12th Project.

# EpicEvents CRM

EpicEvents CRM is composed of an admin interface for managers, sales team and support team members on one part, and an API for front ends destined to sales team and support team members.

It is designed to manage data concerning clients, contracts they make with sales team members and events managed by support team members.

You can consult the ER diagram [here](https://drive.google.com/file/d/1YInVVbs5OBryGPh5ph_lB9dJhFbopM-b/view?usp=sharing).

### Creating Virtual environment and downloading the program:

You need Python 3 (tested on 3.10), git and venv installed on your machine.

Open a terminal and navigate into the folder you want EpicEvent CRM to be downloaded, and run the following commands:

* On Linux or macOS:
```bash
git clone https://github.com/YoannDeb/EpicEvents.git
cd EpicEvents
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

* On Windows:
```bash
git clone https://github.com/YoannDeb/EpicEvents.git
cd EpicEvents
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```

### Configure PostgreSQL database

You first must install postgresSQL and configure a database.

See [official PostgreSQL doc](https://www.postgresql.org/docs/14/tutorial.html) and [official Django doc](https://docs.djangoproject.com/en/4.0/ref/databases/#postgresql-notes) for more info.

You need to create a database for the app, and then configure it in `.env`.

```bash
DBNAME='db_name'
DBUSER='db_user'
DBPASSWORD='password'
DBHOST='127.0.0.1'
DBPORT=5432
DBENGINE='django.db.backends.postgresql'
SECRET_KEY='the secret key'
ALLOWED_HOSTS="[\"*\"]"
CSRF_HOSTS="[\"http://0.0.0.0:8000\"]"
```

### Initiate PostgreSQL database

Open a terminal and navigate into the root of the project (i.e. the folder where is situated manage.py) , and run the following commands:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py init_groups
```

### Create demo datas

Open a terminal and navigate into the root of the project (i.e. the folder where is situated manage.py) , and run the following commands:

```bash
python manage.py create_demo_datas 10 20 3 1
# 10 represents the number of users
# 20 represents the number of customers
# 3 represents the number of contracts per customer
# 1 represents the number of events per contract
```


### Create a superuser (administrator)

Open a terminal and navigate into the root of the project (i.e. the folder where is situated manage.py) , and run the following command:

```bash
python manage.py createsuperuser
```

You will be prompted an email, first and last name, and a password. That's it, the superuser is created !

### Run EpicEvents CRM

Open a terminal and navigate into the root of the project (i.e. same folder than manager.py), and run the following command:

```bash
python manage.py runserver
```

The admin page will be accessible at http://127.0.0.1:8000/admin
You can then login with previously created superuser email and password.
It is now possible to populate the database, with some sales or support team members (don't forget to assign roles).

API will be accessible (with Postman for example) at http://127.0.0.1:8000/api-v1/

### Documentation of the API endpoints

API specifications are accessible on this url:

https://documenter.getpostman.com/view/17391069/2s93RQUufb
