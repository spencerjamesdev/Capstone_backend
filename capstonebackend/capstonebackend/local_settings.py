DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'capstone_database',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}

SECRET_KEY = 'django-insecure-tbhhqm*hcs4l(&=!fjj8vq!)0pbgg%%p78w1-h7*sz-#g6$=v6'