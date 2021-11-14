"""
WSGI config for furryEC project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'furryEC.settings.dev')  # 上线的话修改这里的配置文件。
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'furryEC.settings.pro')

application = get_wsgi_application()
