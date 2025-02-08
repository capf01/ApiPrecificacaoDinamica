import os

# Configurações do Django
SECRET_KEY = 'chave_secreta'
DEBUG = True

# Configurações do banco de dados
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_do_banco',
        'USER': 'usuario_do_banco',
        'PASSWORD': 'senha_do_banco',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Configurações do Celery
CELERY_BROKER_URL = 'amqp://localhost'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# Configurações do Django Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

# Configurações do AWS
AWS_ACCESS_KEY_ID = 'sua_chave_de_acesso'
AWS_SECRET_ACCESS_KEY = 'sua_chave_secreta'
AWS_STORAGE_BUCKET_NAME = 'nome_do_bucket'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# Configurações do e-mail
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'seu_email@gmail.com'
EMAIL_HOST_PASSWORD = 'sua_senha'