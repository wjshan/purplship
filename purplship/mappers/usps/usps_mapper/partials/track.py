from pyusps.TrackRequest import (
    TrackRequest,
    TrackIDType
)
from pyusps.TrackResponse import (
    TrackResponse
)
from lxml import etree
from .interface import reduce, Tuple, List, T, USPSMapperBase


class USPSMapperPartial(USPSMapperBase):

    def parse_track_response(self, response: etree.ElementBase) -> Tuple[List[T.TrackingDetails], List[T.Error]]:
        pass

    def _extract_tracking(self, trackings: List[T.TrackingDetails], track: etree.ElementBase) -> List[T.TrackingDetails]:
        pass

    def create_track_request(self, payload: T.tracking_request) -> TrackRequest:
        return TrackRequest(
            USERID=self.client.username,
            TrackID=[
                TrackIDType(
                    ID=tn,
                    valueOf_=None
                ) for tn in payload.tracking_numbers
            ]
        )

        