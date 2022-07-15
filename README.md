# Personalised Newsfeed
Curates news periodically from newsapi.org. The news are displayed in a list. The list is paginated. The news are sorted by created time. 

SITE: [https://strativ.shampad.live](https://strativ.shampad.live) -- not live anymore

API DOCS: [https://strativ.shampad.live/api/docs](https://strativ.shampad.live/api/docs)  -- not live anymore

Credentials: Admin [link](https://strativ.shampad.live/nfCkAZEQe5wXWXlx8Qna1ShLIYN5J7pa/)
    
    [email]: sompod123@gmail.com
    [password]: 5946644S

## Features

- Django-based backend

    - [Django 3.2.13](https://www.djangoproject.com/)
    - [Postgresql 13](https://www.postgresql.org/)
    - [Django REST Framework 3.13.1](https://www.django-rest-framework.org/)
    - [Celery 5.2.7](https://www.celeryproject.org/)
    - [redis 4.3.3](https://redis.io/)
    - Separate settings for different environments (local/production)
    - Python 3.6 or later
    - Accessible from port `8000` for local development

- Batteries

    - Docker / Docker Compose integration
    - [py.test](http://pytest.org/) and [coverage](https://coverage.readthedocs.io/) integration
    - Deploy helpers
    - Production configuration for Traefik
    - Includes [PyCharm](https://www.jetbrains.com/pycharm/) project config


## Usage

To use this template, first ensure that you have
[Docker](https://www.docker.com/get-started/) available.

After that, you should:

1. Clone the repository
    ```
   git clone repository URL
   ```
2. Download the envs.zip from [here](https://drive.google.com/file/d/1Pz_SsRsi5W7DZR_wUX7YZIh6XO4ibWOf/view?usp=sharing)
3. Unzip the envs.zip and put the `.envs` folder in the project root directory - this is to prevent the API key from being public as Sendgrid bans the API
4. Build the image: `local.yml`
    ```
    docker-compose -f local.yml build
    ```
5. Migrate the database
    ```
    docker-compose -f local.yml run --rm django python manage.py migrate
    ```
6. Create a superuser. Follow steps to create an admin
    ```
    docker-compose -f local.yml run --rm django python manage.py createsuperuser
    ```

7. Run the server
    ```
    docker-compose -f local.yml up
    ```

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest
