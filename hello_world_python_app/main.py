"""
Flask backend entrypoint.

Provides a minimal API:
- GET /     -> "Hello, World!"
- GET /bye  -> "Bye"

The app binds to HOST/PORT from environment variables when provided.
"""

import os

from flask import Flask

app = Flask(__name__)


@app.get("/")
def hello() -> str:
    """Return a simple greeting for sanity-checking the service."""
    return "Hello, World!"


@app.get("/bye")
def bye() -> str:
    """Return a simple 'Bye' response."""
    return "Bye"


if __name__ == "__main__":
    # Use env vars when available; defaults are suitable for local dev.
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "3001"))
    debug = os.getenv("NODE_ENV", "development").lower() != "production"
    app.run(host=host, port=port, debug=debug)
