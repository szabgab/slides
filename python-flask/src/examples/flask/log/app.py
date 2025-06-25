from flask import Flask
import logging
app = Flask(__name__)


# minimum log level defaults to warning
# we can set the minimum loge level
app.logger.setLevel(logging.INFO)
app.logger.debug('debug')
app.logger.info('info')
app.logger.warning('warning')

@app.route("/")
def main():
    app.logger.debug("Some debug message")
    app.logger.info("Some info message")
    app.logger.warning("Some warning message")
    app.logger.error("Some error message")
    return "Hello World"

