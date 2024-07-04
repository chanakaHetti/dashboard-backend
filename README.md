# Django Tastypie RESTfull API application

#### Steps

1. Create the Vagrant file
2. Create the requirements.txt file
3. Run `pip install -r requirements.txt`
4. Create the new dJango project
5. run `django-admin.py startproject backend` ( or `django-admin.py startproject backend .` if doesn't need a new folder backend)
6. Go to the created dJango project `cd backend`
7. Create the dJango app `python3 manage.py startapp playground`
8. Add the create file name inside the `/backend/settings.py/` file `INSTALLED_APPS`

#### Run server on the virtual machine

1. Run `vagrant ssh`
2. Run `cd /srv/django-tastypie-rest-api/backend`
3. Run server `python3 manage.py runserver 0.0.0.0:8051`
4. Then can access server via `http://127.0.0.1:8041/` on the browser

#### Adding the base app for handling users and accounts

1. Create the dJango app `python3 manage.py startapp base`
2. Add the create file name inside the `/backend/settings.py/` file `INSTALLED_APPS`

#### Migration run for each file

1. Run `vagrant ssh`
2. Run `cd /srv/django-tastypie-rest-api/backend`
3. Make migrations `python3 manage.py makemigrations base`
4. Apply migrations `python3 manage.py migrate`
