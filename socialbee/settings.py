import os
import urlparse

from django.core.urlresolvers import reverse_lazy


PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = [
    # ("Your Name", "your_email@example.com"),
]

MANAGERS = ADMINS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "socialbee",
        "HOST": "127.0.0.1",
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "UTC"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-us"

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

MEDIA_URL = "/site_media/media/"
STATIC_URL = "/site_media/static/"
MEDIA_ROOT = os.path.join(os.environ.get("GONDOR_DATA_DIR", PACKAGE_ROOT), "site_media", "media")
STATIC_ROOT = os.path.join(os.environ.get("GONDOR_DATA_DIR", PACKAGE_ROOT), "site_media", "static")

# Additional locations of static files
STATICFILES_DIRS = [
    os.path.join(PACKAGE_ROOT, "static"),
]

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Make this unique, and don't share it with anybody.
SECRET_KEY = "dr_=me4xzuv^0vvpg%)7w5#-5sekwp(fq4kw-6v^#(n533b=(x"

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    "account.context_processors.account",
    "pinax_theme_bootstrap.context_processors.theme",
    "social_auth.context_processors.social_auth_by_name_backends",
    "socialbee.friends.context_processors.suggestions"
]


MIDDLEWARE_CLASSES = [
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "social_auth.middleware.SocialAuthExceptionMiddleware"
]

ROOT_URLCONF = "socialbee.urls"

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = "socialbee.wsgi.application"

TEMPLATE_DIRS = [
    os.path.join(PACKAGE_ROOT, "templates"),
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    # theme
    "pinax_theme_bootstrap",
    "django_forms_bootstrap",
    
    # external
    "account",
    "metron",
    "social_auth",
    "djcelery",
    
    # project
    "socialbee",
    "socialbee.friends",
    "socialbee.profiles",
]

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse"
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler"
        }
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    }
}

FIXTURE_DIRS = [
    os.path.join(PROJECT_ROOT, "fixtures"),
]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

ACCOUNT_OPEN_SIGNUP = True
ACCOUNT_USE_OPENID = False
ACCOUNT_REQUIRED_EMAIL = False
ACCOUNT_EMAIL_VERIFICATION = False
ACCOUNT_EMAIL_AUTHENTICATION = False
ACCOUNT_UNIQUE_EMAIL = EMAIL_CONFIRMATION_UNIQUE_EMAIL = False
ACCOUNT_LOGIN_REDIRECT_URL = "home"
ACCOUNT_LOGOUT_REDIRECT_URL = "home"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 2
LOGIN_URL = reverse_lazy("account_login")
LOGIN_REDIRECT_URL = reverse_lazy("home")

# Social Auth

LOGIN_ERROR_URL = "/account/social/connections/"

AUTHENTICATION_BACKENDS = [
    "social_auth.backends.twitter.TwitterBackend",
    "social_auth.backends.facebook.FacebookBackend",
    "social_auth.backends.google.GoogleOAuth2Backend",
]

SOCIAL_AUTH_ASSOCIATE_BY_MAIL = False

SOCIAL_AUTH_PIPELINE = [
    "socialbee.pipeline.prevent_duplicates",
    
    "social_auth.backends.pipeline.social.social_auth_user",
    "social_auth.backends.pipeline.user.get_username",
    "social_auth.backends.pipeline.user.create_user",
    "social_auth.backends.pipeline.social.associate_user",
    "social_auth.backends.pipeline.social.load_extra_data",
    "social_auth.backends.pipeline.user.update_user_details",
    
    "socialbee.pipeline.import_friends"
]

GOOGLE_OAUTH2_CLIENT_ID = os.environ.get("GOOGLE_OAUTH2_CLIENT_ID", "")
GOOGLE_OAUTH2_CLIENT_SECRET = os.environ.get("GOOGLE_OAUTH2_CLIENT_SECRET", "")

TWITTER_CONSUMER_KEY = os.environ.get("TWITTER_CONSUMER_KEY", "")
TWITTER_CONSUMER_SECRET = os.environ.get("TWITTER_CONSUMER_SECRET", "")

FACEBOOK_APP_ID = os.environ.get("FACEBOOK_APP_ID", "")
FACEBOOK_API_SECRET = os.environ.get("FACEBOOK_API_SECRET", "")
FACEBOOK_EXTENDED_PERMISSIONS = [
    "email",
]

GOOGLE_OAUTH_EXTRA_SCOPE = [
    "https://www.googleapis.com/auth/plus.login",
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
]

GOOGLE_OAUTH2_EXTRA_DATA = [
    ("given_name", "first_name"),
    ("family_name", "last_name"),
    ("email", "email"),
]

FACEBOOK_EXTRA_DATA = [
    ("first_name", "first_name"),
    ("last_name", "last_name"),
]

TWITTER_EXTRA_DATA = [
    ("name", "name"),
    ("screen_name", "screen_name"),
    ("profile_image_url", "profile_image_url"),
]


# Celery
if "GONDOR_REDIS_URL" in os.environ:
    urlparse.uses_netloc.append("redis")
    url = urlparse.urlparse(os.environ["GONDOR_REDIS_URL"])
    GONDOR_REDIS_HOST = url.hostname
    GONDOR_REDIS_PORT = url.port
    GONDOR_REDIS_PASSWORD = url.password
else:
    GONDOR_REDIS_HOST = "localhost"
    GONDOR_REDIS_PORT = 6379
    GONDOR_REDIS_PASSWORD = ""

BROKER_TRANSPORT = "redis"
BROKER_HOST = GONDOR_REDIS_HOST
BROKER_PORT = GONDOR_REDIS_PORT
BROKER_VHOST = "0"
BROKER_PASSWORD = GONDOR_REDIS_PASSWORD
BROKER_POOL_LIMIT = 10

CELERY_RESULT_BACKEND = "redis"
CELERY_REDIS_HOST = GONDOR_REDIS_HOST
CELERY_REDIS_PORT = GONDOR_REDIS_PORT
CELERY_REDIS_PASSWORD = GONDOR_REDIS_PASSWORD
CELERYD_HIJACK_ROOT_LOGGER = False
CELERYD_LOG_LEVEL = "INFO"
CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
CELERY_IGNORE_RESULT = True
CELERY_SEND_TASK_ERROR_EMAILS = True
CELERY_DISABLE_RATE_LIMITS = True
CELERY_TASK_PUBLISH_RETRY = True
CELERY_TASK_RESULT_EXPIRES = 7 * 24 * 60 * 60  # 7 Days
CELERYD_TASK_TIME_LIMIT = 120
CELERYD_TASK_SOFT_TIME_LIMIT = 120
