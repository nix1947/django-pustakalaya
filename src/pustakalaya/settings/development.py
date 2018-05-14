from .base import * # NOQA

INSTALLED_APPS += [
    "debug_toolbar",
]

INTERNAL_IPS = [
    "127.0.0.1",
]



DATABASES = {
    'default': {

        #---Sqlite settings
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

        #---Postgres settings
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pustakalaya',
        'USER': 'pustakalaya_user',
        'PASSWORD': 'pustakalaya123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

