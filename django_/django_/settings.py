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

# Application definition

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
    "DEFAULT_PERMISSION_CLASSES": [
        # "rest_framework.permissions.IsAuthenticated",
        "rest_framework.permissions.AllowAny"
        ],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        ],
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]


ROOT_URLCONF = 'djoserauthapi.urls'

WSGI_APPLICATION = 'djoserauthapi.wsgi.application'

# JWT Settings
SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('Bearer', 'JWT',),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "UPDATE_LAST_LOGIN": True,
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
}

# Djoser Settings
DJOSER = {
    'LOGIN_FIELD': 'email',
    'PASSWORD_RESET_CONFIRM_URL': 'password-reset/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL':True,
    "ACTIVATION_URL": "accounts/auth/users/activate/{uid}/{token}",
    'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND': True,
    'TOKEN_MODEL':None,    
    "SOCIAL_AUTH_ALLOWED_REDIRECT_URIS": [
        'http://127.0.0.1:8000/accounts/auth/social/complete/github/',
        'http://127.0.0.1:8000/accounts/auth/social/complete/facebook/',
        'http://127.0.0.1:8000/accounts/auth/social/complete/google-oauth2/',
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
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2', # github <----
    'social_core.backends.facebook.FacebookOAuth2', # facebook <----
    'social_core.backends.google.GoogleOAuth2',  # google <----
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_GITHUB_KEY = '923e62395399fae6dd91'
SOCIAL_AUTH_GITHUB_SECRET = '2102d52907f9c08fe90fd30bd3c091aa5a27efbd'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '534268798718-451t7sn6c7iuu8ts9jqvbhjtalg2vqa4.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

SOCIAL_AUTH_FACEBOOK_KEY = "3738217359745570"
SOCIAL_AUTH_FACEBOOK_SECRET = "7fdf8462e923299f9b618e46656fd6b9"

SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
'https://www.googleapis.com/auth/userinfo.email',
]