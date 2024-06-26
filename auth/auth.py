"""
Main file in autentification module
"""
from fastapi_users.authentication import (
    AuthenticationBackend,
    CookieTransport,
    JWTStrategy
)

# choose Transport (example: cooky)
cookie_transport = CookieTransport(cookie_max_age=3600)

SECRET = "SECRET"


# choose Strategies (example: jwt)
def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


# Creation backend
auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
