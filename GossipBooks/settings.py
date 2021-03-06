import os
import pathlib
import environ
from google.oauth2 import service_account
from google.oauth2.service_account import Credentials

env = environ.Env()
environ.Env.read_env()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = ['gossipsbook.herokuapp.com', '127.0.0.1', 'localhost', 'gossipsbook.com', 'www.gossipsbook.com']

INSTALLED_APPS = [
    'channels',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',

    # My apps
    'controls.apps.ControlsConfig',
    'questions.apps.QuestionsConfig',
    'gossips.apps.GossipsConfig',
    'cheaters.apps.CheatersConfig',
    'users.apps.UsersConfig',
    'answers.apps.AnswersConfig',
    'searches.apps.SearchesConfig',

    'messaging.apps.MessagingConfig',

    # Django all-auth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',

    # Django-Rest-Framework
    'rest_framework',
    'rest_framework.authtoken',
    'api.apps.ApiConfig',

    # Third Party Apps
    'crispy_forms',
    'django_rest_passwordreset',

]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
# ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'GossipBooks.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

ASGI_APPLICATION = "GossipBooks.asgi.application"
WSGI_APPLICATION = 'GossipBooks.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'd9t0iccvmsl35s',
#         'HOST': 'ec2-23-20-205-19.compute-1.amazonaws.com',
#         'PORT': 5432,
#         'USER': 'wnducfffnqafij',
#         'PASSWORD': '97dc744a5b901e34228171b4955eddb4e4417497c96c77cf7792f7208a9220cc'
#     }
# }

# postgres://cejupgskzndxgd:a619617fbad02bc074c5c623f1bb819689e68f1b730c7f158c7da5bc3575bf00@ec2-54-242-43-231.compute-1.amazonaws.com:5432/d54m80rajacatb

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("DATABASE_NAME"),
        'HOST': 'ec2-54-242-43-231.compute-1.amazonaws.com',
        'PORT': 5432,
        'USER': os.environ.get("DATABASE_USER"),
        'PASSWORD': os.environ.get("DATABASE_PASSWORD")
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    # 'DEFAULT_RENDERER_CLASSES': [
    #     'rest_framework.renderers.JSONRenderer',
    # ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 2
}


SITE_ID = 1

LOGIN_URL = '/accounts/login'
LOGIN_REDIRECT_URL = '/welcome'

EMAIL_BACKEND = 'sendgrid_backend.SendgridBackend'
SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")  # Gossips Book API KEY
SENDGRID_SANDBOX_MODE_IN_DEBUG = False

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}


# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels.layers.InMemoryChannelLayer"  # Good for testing and local server purposes
#     }
# }

# Channel Layers For Django Channels

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
             "hosts": [os.environ.get("REDIS_URL")],
        },
    },
}

# EMAIL_HOST = 'smtp.google.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True

# EMAIL_HOST_USER = 'gossipsbook.in@gmail.com'
# EMAIL_HOST_PASSWORD = "fmemsarqssvhjnds" #This is the generated password for your Gmail app. Only for backend auth purposes,
# # EMAIL_HOST_PASSWORD = "Ammananna@1991"

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587

# EMAIL_USE_TLS = True

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_FILE_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
GS_BUCKET_NAME = "gossipsbook_bucket"
STATICFILES_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
FILE_NAME = "gossipsbook-website-project-1eb1e8ba4391.json"
GS_CREDENTIALS = Credentials.from_service_account_file(FILE_NAME)
GS_PROJECT_ID = "gossipsbook-website-project"

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_dir')

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "staticfiles")
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'staticfiles/media')
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SECURE_PROXY_SSL_HEADER=('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST=True
USE_X_FORWARDED_PORT=True
SECURE_HSTS_SECONDS=3600
SECURE_HSTS_PRELOAD=True
SECURE_HSTS_INCLUDE_SUBDOMAINS=True
SECURE_SSL_REDIRECT=True
SECURE_REFERRER_POLICY=strict-origin
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
