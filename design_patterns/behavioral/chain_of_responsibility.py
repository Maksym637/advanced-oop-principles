from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        pass


class AuthenticationHandler(Handler):
    def handle(self, request):
        if request.get("authenticated", False):
            print("AuthenticationHandler: User authenticated.")
            if self._next_handler:
                return self._next_handler.handle(request)
            return True
        else:
            print("AuthenticationHandler: Authentication failed.")
            return False


class AuthorizationHandler(Handler):
    def handle(self, request):
        if request.get("role") == "admin":
            print("AuthorizationHandler: User authorized as admin.")
            if self._next_handler:
                return self._next_handler.handle(request)
            return True
        else:
            print("AuthorizationHandler: Authorization failed.")
            return False


class LoggingHandler(Handler):
    def handle(self, request):
        print(f"LoggingHandler: Logging request {request}")
        if self._next_handler:
            return self._next_handler.handle(request)
        return True


auth = AuthenticationHandler()
authorize = AuthorizationHandler()
logger = LoggingHandler()

auth.set_next(authorize).set_next(logger)
auth.handle(request={"authenticated": True, "role": "admin"})
