# technical-test-talenta365
## Installation

You'll need the following dependencies:
* python 3 (https://docs.python.org/3/using/index.html)

#### Steps
1. Clone repository: `git clone git@github.com:malonso11/technical-test-talenta365.git`
1. Open terminal and navigate to root folder project (**technical-test-talenta365**)
1. Install python dependencies: `pip install -r requirements.txt`
1. Run migrations: `python manage.py migrate`
1. Create super user: `python manage.py createsuperuser`

## Running

#### Steps for running first point
1. Open terminal and navigate to root folder project (**technical-test-talenta365**)
1. Run unit tests: `python manage.py test`
1. Run local server: `python manage.py runserver` and navigate to http://localhost:8000/admin/


#### Steps for running second point
1. Open terminal and navigate to root folder project (**technical-test-talenta365**)
1. Run unit tests: `python manage.py test`
1. Run unit tests: `python manage.py seek_letters 56`, change 56 for another number
