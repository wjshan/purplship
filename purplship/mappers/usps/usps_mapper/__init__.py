from typing import Tuple, List, Union
from lxml import etree
from purplship.domain.mapper import Mapper
from purplship.domain import Types as T
from pyusps.RateV4Request import RateV4Request
from pyusps.IntlRateV2Request import IntlRateV2Request
from pyusps.TrackRequest import TrackRequest
from .partials import (
    USPSRateMapperPartial, 
    USPSTrackMapperPartial
)


class USPSMapper(
        Mapper,
        USPSRateMapperPartial,
        USPSTrackMapperPartial
    ):        

    def create_quote_request(self, payload: T.shipment_request) -> Union[RateV4Request, IntlRateV2Request]:
        is_intl = False
        return (
            self.create_intl_rate_request if is_intl else self.create_rate_request
        )(payload)

    def create_tracking_request(self, payload: T.tracking_request) -> TrackRequest:
        return self.create_track_request(payload)



    def parse_quote_response(self, response: etree.ElementBase) -> Tuple[List[T.QuoteDetails], List[T.Error]]:
        return self.parse_rate_response(response)

    def parse_tracking_response(self, response: etree.ElementBase) -> Tuple[List[T.TrackingDetails], List[T.Error]]:
        return self.parse_track_response(response)