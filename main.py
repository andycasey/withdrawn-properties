
import logging

from flask import Flask

from sync import sync

app = Flask(__name__)


@app.route("/")
def hello():
    """Return a friendly HTTP greeting."""
    return "Hello World!"


@app.errorhandler(500)
def server_error(error):
    logging.exception("An error occurred during a request.")
    return (f"Internal error: <pre>{error}</pre>", 500)


@app.route("/sync")
def sync_call():
    num_listing, num_withdrawn = sync()
    return f"Num listed: {num_listing} and num_withdrawn: {num_withdrawn}"


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
