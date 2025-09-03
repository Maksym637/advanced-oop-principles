class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:

            self._observers.remove(observer)

        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


class Core(Subject):
    def __init__(self, name=""):
        Subject.__init__(self)
        self._name = name
        self._temperature = 0

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value
        self.notify()


class TemperatureViewer:
    def __init__(self, name):
        self._name = name

    def update(self, subject):
        print(f"{self._name}: {subject._name} has temperature {subject._temperature}")


core_1 = Core("Core 1")

viewer_1 = TemperatureViewer("TemperatureViewer 1")
viewer_2 = TemperatureViewer("TemperatureViewer 2")

core_1.attach(viewer_1)
core_1.attach(viewer_2)

core_1.temperature = 80
core_1.temperature = 100
