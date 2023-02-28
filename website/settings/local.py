from .base import *

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="#qoes#^@@4iey*4ed#y(0vl03a886j2+kuqv*@sx8!_+drw=^_",
)
# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.envs/.local/'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS")

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env("POSTGRES_DB"),
        'USER': env("POSTGRES_USER"),
        'PASSWORD': env("POSTGRES_PASSWORD"),
        'HOST': env("POSTGRES_HOST"),
        'PORT': env("POSTGRES_PORT"),
        'ATOMIC_REQUESTS': False,
        'CONN_MAX_AGE': 20,
    },
}