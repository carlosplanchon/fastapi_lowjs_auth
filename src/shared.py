#!/usr/bin/env python3

from pathlib import Path

import tomllib


##################
# --- CONFIG --- #
##################
with Path("config.toml").open(mode="rb") as fp:
    CONFIG = tomllib.load(fp)


DB_USERNAME: str = CONFIG["database"]["DB_USERNAME"]
DB_PASSWORD: str = CONFIG["database"]["DB_PASSWORD"]
DB_HOST: str = CONFIG["database"]["DB_HOST"]
DB_PORT: str = CONFIG["database"]["DB_PORT"]
DB_NAME: str = CONFIG["database"]["DB_NAME"]

DB_URL: str = f"postgresql+asyncpg://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# used to sign JWTs, make sure it is really secret.
JWT_SIGNING_SECRET_KEY = CONFIG["security"]["JWT_SIGNING_SECRET_KEY"]

GOOGLE_CLIENT_ID = CONFIG["google"]["GOOGLE_CLIENT_ID"]
GOOGLE_CLIENT_SECRET = CONFIG["google"]["GOOGLE_CLIENT_SECRET"]
GOOGLE_REDIRECT_URI = CONFIG["google"]["GOOGLE_REDIRECT_URI"]

APP_ROOT_PATH = CONFIG["app"]["ROOT_PATH"]
