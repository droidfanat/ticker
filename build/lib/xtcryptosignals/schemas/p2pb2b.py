__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from marshmallow import (
    fields,
    pre_load,
)
from xtcryptosignals.schemas.base import BaseSchema
import xtcryptosignals.settings as s


class P2pb2b(BaseSchema):
    symbol = fields.Str(required=True)
    ticker = fields.Str(required=True)
    source = fields.Str(required=True)
    ask = fields.Float(required=True, attribute='price')

    @pre_load
    def pre_load(self, data):
        data['source'] = s.P2PB2B
        return data
