from .base_settings import *


DEBUG = True
SECRET_KEY = "environ.get('SECRET_KEY')"  # this line should be changed on production
WEBSITE_URL = "localhost"

# Applications
INSTALLED_APPS += ['silk']
MIDDLEWARE += ['silk.middleware.SilkyMiddleware']

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "djangoPreBuild.sqlite3",
    }
}
