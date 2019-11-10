# django-starter

## run

```shell
# setup database
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate
pipenv run python manage.py createsuperuser

# set SECRET_KEY
pipenv run python manage.py shell -c "from django.core.management import utils; print(utils.get_random_secret_key())"

# run
pipenv run python manage.py runserver
```

## How would I set this up myself?

```shell
# pipenv
env PIPENV_VENV_IN_PROJECT=true pipenv --python 3.6
pipenv install PACKAGES...

# create project
pipenv run django-admin startproject config .
mkdir -p apps/<app-name>
pipenv run python manage.py startapp <app-name> apps/<app-name>
```

Sphinx

```shell
pipenv run sphinx-quickstart docs
pipenv run sphinx-apidoc -f -o ./docs .
pipenv run sphinx-build -b html ./docs ./docs/_build
pipenv run make -C docs html
```
