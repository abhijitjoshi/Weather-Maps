# PostgreSQL database
POSTGRES_APP_DB_HOST = 'localhost'
POSTGRES_APP_DB_PORT = '5432'
POSTGRES_APP_DB_USER = 'abhijit'
POSTGRES_APP_DB_PASSWORD = 'xxxx'
POSTGRES_APP_DB_NAME = 'weathermaps'
READ_DB = 'read'
READ_DB_NAME = 'weathermaps'
READ_DB_USER = 'abhijit'
READ_DB_PASSWORD = 'xxxx'
READ_DB_HOST = 'localhost'
READ_DB_PORT = ''

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': POSTGRES_APP_DB_NAME,
       'USER': POSTGRES_APP_DB_USER,
       'PASSWORD': POSTGRES_APP_DB_PASSWORD,
       'HOST': POSTGRES_APP_DB_HOST,  # Empty for localhost through domain sockets or'127.0.0.1' for localhost through TCP.
       'PORT': POSTGRES_APP_DB_PORT,

   },
   'read': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': READ_DB_NAME,
        'USER': READ_DB_USER,
        'PASSWORD': READ_DB_PASSWORD,
        'HOST': READ_DB_HOST,
        'PORT': READ_DB_PORT,
    }
}
