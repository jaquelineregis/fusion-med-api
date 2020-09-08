# fusion-med-api

### Oficial API in Heroku

#### Landing Page
* https://fusion-med.herokuapp.com/

#### API URL
* https://fusion-med.herokuapp.com/api/

#### Admin URL
* https://fusion-med.herokuapp.com/admin/
- username: fusionmed
- password: fusionmed

#### Links URL (youtube, figma, github)
* https://fusion-med.herokuapp.com/links/

#### Steps to run

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
