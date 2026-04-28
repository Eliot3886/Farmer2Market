"""
ASGI config for farm2market project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

# 1. Set the default settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farmer2market.settings')

# 2. Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing any apps/models (like api.routing)
django_asgi_app = get_asgi_application()

# 3. Now it is safe to import Channels and routing
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import api.routing

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            api.routing.websocket_urlpatterns
        )
    ),
})
