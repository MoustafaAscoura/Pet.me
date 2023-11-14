from pathlib import Path
import os
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*38y&7z!pu-1+&gm7-2qbx29s5nvoeh)l-fm1i%xu_5=r!=+_)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'djoser',
    'drf_yasg',
    "corsheaders",
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'social_django',
    'django_cleanup.apps.CleanupConfig',
    'pets.apps.PetsConfig',
    'offers.apps.OffersConfig',
    'social.apps.SocialConfig',
    'chats.apps.ChatsConfig',
    'accounts.apps.AccountsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
        'rest_framework.filters.SearchFilter',
    ],
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_PAGINATION_CLASS': 'pets.pagination.CustomPagination',
    'PAGE_SIZE': 12,
    'DEFAULT_THROTTLE_RATES': {
        'anon': '50/minute',
        'user': '100/minute'
    }
}

DOMAIN = "127.0.0.1:3000"
SITE_NAME = "PetMe"

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

ROOT_URLCONF = 'djoserauthapi.urls'

WSGI_APPLICATION = 'djoserauthapi.wsgi.application'

# JWT Settings
SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('Bearer', 'JWT',),
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": True,
    "UPDATE_LAST_LOGIN": True,
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
}

# Djoser Settings
DJOSER = {
    'LOGIN_FIELD': 'email',
    "ACTIVATION_URL": "accounts/users/activate/{uid}/{token}",
    'PASSWORD_RESET_CONFIRM_URL': 'password-reset/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL':'username-reset/{uid}/{token}',

    'SEND_ACTIVATION_EMAIL':True,
    'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND': True,
    'TOKEN_MODEL':None,    
    "SOCIAL_AUTH_ALLOWED_REDIRECT_URIS": [
        'http://localhost:3000/accounts/social/complete/github/',
        'http://localhost:3000/accounts/social/complete/facebook/',
        'http://localhost:3000/accounts/social/complete/google-oauth2/',
    ],

    "SERIALIZERS": {
        "user": "accounts.serializers.UserSerializer",
        'current_user': 'accounts.serializers.UserSerializer',

    },
}

AUTH_USER_MODEL = 'accounts.User'


# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "petme.api@gmail.com"
EMAIL_HOST_PASSWORD = "yyiycndhqjwhlmpq"


ROOT_URLCONF = 'django_.urls'

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',

            ],
        },
    },
]

WSGI_APPLICATION = 'django_.wsgi.application'

# DATABASES = {
#     "default": {
#     "ENGINE": "django.db.backends.postgresql",
#     "NAME": "pet_me",
#     "USER": "mariam",
#     "PASSWORD": "123456789@m",
#     "HOST": "localhost",
#     "PORT": "5432",
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = 'media/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2', # github <----
    'social_core.backends.facebook.FacebookOAuth2', # facebook <----
    'social_core.backends.google.GoogleOAuth2',  # google <----
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_GITHUB_KEY = '923e62395399fae6dd91'
SOCIAL_AUTH_GITHUB_SECRET = 'a9decba498cee01e861f989733b1d252857a95c0'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '824848817431-3395fioo7nn8pvq96fbpdgqcgj28ajmt.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

SOCIAL_AUTH_FACEBOOK_KEY = "153943981107306"
SOCIAL_AUTH_FACEBOOK_SECRET = "4b7b1ee8dd76f30370333a23fee61bfb"
SOCIAL_AUTH_FACEBOOK_API_VERSION = '18.0'
