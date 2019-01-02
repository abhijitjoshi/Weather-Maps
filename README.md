
### Dependencies ###

* Python 3.x
* PostGreSQL 9.x


### Setting up database ###

* Create a user for postgres : "createuser <user_name> --pwprompt --superuser"
* Set password for the user that was created : <DB_PASSWORD>
* Create a database for the application : "createdb <db_name>"


### Setting up the virtual environment ###

* Setup python 3 virtual environment : "virtualenv -p python3 <env_name>"
* Activate the environment : source <env_name>/bin/activate


### Dependencies ###

* Install requirements: "pip install -r requirements.txt".
* In database_config.py, update the database password <DB_PASSWORD>
* Create migrations for the model "python manage.py makemigrations"
* Run migrations: "python manage.py migrate"
* Install forecastio by navigating to the forecastiopy3-master directory and running 'python setup.py install'
* Enter the Google API key in the script tag at the end in the webapp/templates/index.html file
* Enter Google API Key and the Dark Sky API Key in the webapp/apps/weather_apps/views.py file


### Running the server ###

* Running server: "python manage.py runserver"
* Go to http://127.0.0.1:8000/weather/home/
