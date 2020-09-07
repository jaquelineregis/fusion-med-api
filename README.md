# fusion-med-api

### API URL
* https://fusion-med.herokuapp.com/

### Steps to run

##### Terminal
* touch **.env**
  - _(Add this fields)_
  - SECRET_KEY=123
  - DEBUG=True
  - ALLOWED_HOSTS=127.0.0.1
* pip install -r requirements.txt (Environment PROD)
* pip install -r requirements-dev.txt (Environment DEV)
* python manage.py migrate
* python manage.py createsuperuser (optional)
* python manage.py runserver
