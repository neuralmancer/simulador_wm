import logging
logging.basicConfig(level=logging.DEBUG)

from flask import Flask
from flask_restful import Api

from modulos.mx.tae import tae_mx

app = Flask(__name__)
api = Api(app)

api.add_resource(tae_mx.runGetFolio, '/taemx/runGetFolio')
api.add_resource(tae_mx.runGetAuth, '/taemx/runGetAuth')
api.add_resource(tae_mx.runGetAck, '/taemx/runGetAck')

if __name__ == '__main__':
    app.run(debug=True)
