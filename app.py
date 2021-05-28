import os
from flask import Flask, request, Response
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s")


ASSETS_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)


@app.route('/incoming', methods=['POST'])
def incoming():
    logger.debug("received request. post data: {0}".format(request.get_data()))
    # handle the request here
    return Response(status=200)


#context = ('cert.pem', 'key.pem')
app.run(host='0.0.0.0', port=5000, debug=True)
