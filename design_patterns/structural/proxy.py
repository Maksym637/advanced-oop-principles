from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def request(self):
        pass


class RealSubject(Subject):
    def request(self):
        print("RealSubject: Handling the request.")


class Proxy(Subject):
    def __init__(self, real_subject: RealSubject):
        self._real_subject = real_subject

    def check_access(self):
        print("Proxy: Checking access before forwarding request...")
        return True

    def log_access(self):
        print("Proxy: Logging request.")

    def request(self):
        if self.check_access():
            self._real_subject.request()
            self.log_access()


def client_code(subject: Subject):
    subject.request()


print("\nClient: Executing with a real subject:")
real_subject = RealSubject()
client_code(real_subject)

print("\nClient: Executing with a proxy")
proxy = Proxy(real_subject)
client_code(proxy)
