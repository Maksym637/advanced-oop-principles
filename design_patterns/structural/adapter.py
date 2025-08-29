class EuropeanSocket:
    def connent(self):
        return "Connected to European socket with 2-pin plug."


class USPlugInterface:
    def connent(self):
        pass


class USPlugToEuropeanAdapter(USPlugInterface):
    def __init__(self, european_socket: EuropeanSocket):
        self.european_socket = european_socket

    def connent(self):
        return self.european_socket.connent()


def use_socket(plug: USPlugInterface):
    print(plug.connent())


euro_socket = EuropeanSocket()
adapter = USPlugToEuropeanAdapter(euro_socket)
use_socket(adapter)
