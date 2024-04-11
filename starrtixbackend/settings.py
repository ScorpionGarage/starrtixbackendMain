
from pathlib import Path
from datetime import timedelta
import environ

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
env_path = BASE_DIR / 'starrtixbackend'/ '.env'
environ.Env.read_env(env_file=env_path, overwrite=True)



SECRET_KEY = env("DJANGO_SECRET_KEY")
DEBUG = True

ENVIRONMENT = env("ENVIRONMENT")

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'User',
    'rest_framework.authtoken',
    'Event',
    'blog',
        'corsheaders',
        'media'
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',

    ],
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'starrtixbackend.urls'

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

WSGI_APPLICATION = 'starrtixbackend.wsgi.application'



if ENVIRONMENT == 'development':
    
    DATABASES = {
        'default': {
        'ENGINE': "django.db.backends.sqlite3",
        'NAME': "db.sqlite3"
        }
    }
else:
    DATABASES = {
        'default': {
        'ENGINE': env('DJANGO_DB_ENGINE'),
            'NAME': env('DJANGO_DB_NAME'),
            'USER': env('DJANGO_DB_USER'),
            'PASSWORD': env('DJANGO_DB_PASSWORD'),
            'HOST': env('DJANGO_DB_HOST'),
            'PORT': env('DJANGO_DB_PORT'),
        }
    }
try:
    from django.db import connections
    connection = connections['default']
    connection.connect()
    print("Database connected Successfully")
    
except Exception as e:
    print(f"Error connecting to database: {e}")
    
    
    

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



STATIC_URL = 'static/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'User.CustomUser'

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=12),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),  # Example for refresh token
    # Add any other custom settings here
}
CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://127.0.0.1:9000",
]

MEDIA_ROOT = BASE_DIR/'media'
MEDIA_URL = '/media/'
