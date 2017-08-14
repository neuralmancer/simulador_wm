from flask_restful import Resource, reqparse
import string
import random

parser = reqparse.RequestParser()

xml_112 = '<?xml version="1.0"?><TPEDoc version="1.0"><response>\
<wmCode value="112" desc="documento invalido de POS"/></response></TPEDoc>'

class runGetFolio(Resource):
    def post(self):
        parser.add_argument('plaza')
        parser.add_argument('tienda')
        parser.add_argument('caja')
        args = parser.parse_args()
        if args['plaza'] and args['tienda'] and args['caja']:
            folio = ''.join(random.choice(string.digits) for _ in range(10))
            xmlStr = """<?xml version="1.0"?><TAEFolio><folio>{}</folio>\
            <wmCode>100</wmCode></TAEFolio>""".format(folio).strip()
            return xmlStr, 201
        else:
            return xml_112, 200

class runGetAuth(Resource):
    def post(self):
        parser.add_argument('folio')
        parser.add_argument('pv_date')
        parser.add_argument('ad_date')
        parser.add_argument('carrier')
        parser.add_argument('phone')
        parser.add_argument('amount')
        args = parser.parse_args()
        if args['folio'] and args['pv_date'] and args['ad_date'] and args['carrier'] and args['phone'] \
            and args['amount']:
            auth = ''.join(random.choice(string.digits) for _ in range(6))
            xmlStr = """<?xml version="1.0"?><TAEAuth><folio>{}</folio><swAuth>{}</swAuth>\
            <wmCode>000</wmCode><reAttempt>N</reAttempt></TAEAuth>""".format(args['folio'], auth).strip()
            return xmlStr, 201
        else:
            return xml_112, 200

class runGetAck(Resource):
    def post(self):
        parser.add_argument('folio')
        parser.add_argument('ack')
        args = parser.parse_args()
        if args['folio'] and args['ack']:
            xmlStr = """<?xml version="1.0"?><TAEAck><folio>{}</folio>\
            <wmCode>101</wmCode></TAEAck>""".format(args['folio']).strip()
            return xmlStr, 201
        else:
            return xml_112, 200
