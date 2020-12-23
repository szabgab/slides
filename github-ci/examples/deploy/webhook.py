from flask import Flask, request
import logging
import hashlib
import hmac


GITHUB_SECRET = 'shibboleth'

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

@app.route("/")
def main():
    return "Deployer Demo"

@app.route("/github", methods=["POST"])
def github():
    signature = request.environ.get('HTTP_X_HUB_SIGNATURE_256')
    app.logger.info(signature)  # sha256=e61920df1d6fb1b30319eca3f5e0d0f826b486a406eb16e46071c6cdd0ce3f9b
    data_as_json = request.data
    #app.logger.info(request.data_as_json)

    expected_signature = 'sha256=' + hmac.new(GITHUB_SECRET.encode('utf8'), data_as_json, hashlib.sha256).hexdigest()
    app.logger.info(expected_signature)
    if signature == expected_signature:
        app.logger.info('verified')

    data = request.json
    #app.logger.info(data)
    app.logger.info(data['repository']['full_name'])
    app.logger.info(data['after'])
    app.logger.info(data['ref']) # get the branch
    return "ok"

@app.route("/action", methods=["POST"])
def action():
    app.logger.info("action")
    secret = request.form.get('secret')
    app.logger.info(secret)
    sha = request.form.get('GITHUB_SHA')
    app.logger.info(sha)
    repository = request.form.get('GITHUB_REPOSITORY')
    app.logger.info(repository)

    return "ok"

