from purplship.domain.client import Client

class USPSClient(Client):

    def __init__(self, server_url: str, username: str, password: str, carrier_name: str = "USPS"):
        self.username = username
        self.password = password
        self.server_url = server_url
        self.carrier_name = carrier_name