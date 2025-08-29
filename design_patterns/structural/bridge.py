from abc import ABC, abstractmethod


# Implementor
class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class TV(Device):
    def turn_on(self):
        return "Turning on the TV."

    def turn_off(self):
        return "Turning off the TV."


class Radio(Device):
    def turn_on(self):
        return "Turning on the Radio."

    def turn_off(self):
        return "Turning off the Radio."


# Abstraction
class RemoteControl:
    def __init__(self, device: Device):
        self.device = device

    def turn_on_device(self):
        return self.device.turn_on()

    def turn_off_device(self):
        return self.device.turn_off()


class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        return "Muting the device."


tv = TV()
radio = Radio()

basic_remote = RemoteControl(tv)
print(basic_remote.turn_on_device())
print(basic_remote.turn_off_device())

advanced_remote = AdvancedRemoteControl(radio)
print(advanced_remote.turn_on_device())
print(advanced_remote.mute())
print(advanced_remote.turn_off_device())
