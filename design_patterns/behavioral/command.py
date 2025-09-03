from typing import List
from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class Copy(Command):
    def execute(self):
        print("Copying...")


class Paste(Command):
    def execute(self):
        print("Pasting...")


class Save(Command):
    def execute(self):
        print("Saving...")


class Macro:
    #
    # The invoker class.
    # It creates multiple concrete command objects and store them in a list
    #
    def __init__(self):
        self.commands: List[Copy] = []

    def add(self, command):
        self.commands.append(command)

    def run(self):
        for command in self.commands:
            command.execute()


macro = Macro()

macro.add(Copy())
macro.add(Paste())
macro.add(Save())

macro.run()
