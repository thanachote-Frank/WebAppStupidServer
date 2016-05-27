# Django Webserver

## Setup

1. Setup virtual environment: `virtualenv venv; source venv/bin/activate`
2. Setup requirements: `pip install -r requirements.txt`
3. Sync database: `python manage.py migrate`
4. Add user: `python manage.py createsuperuser`



## Development

- Run webserver: `python manage.py runserver`
- Enter the front page at http://localhost:8000/static/index.html
 OR
- Run webserver: `python manage.py runserver 0.0.0.0:80`
- Enter the front page at http://127.0.0.1/static/index.html
