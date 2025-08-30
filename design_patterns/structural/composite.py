from typing import List
from abc import ABC, abstractmethod


# Component
class FileSystemItem(ABC):
    @abstractmethod
    def show(self, indent: int = 0):
        pass


# Leaf
class File(FileSystemItem):
    def __init__(self, name: str):
        self.name = name

    def show(self, indent: int = 0):
        print(" " * indent + f"File: {self.name}")


# Composite
class Folder(FileSystemItem):
    def __init__(self, name: str):
        self.name = name
        self.children: List[FileSystemItem] = []

    def add(self, item: FileSystemItem):
        self.children.append(item)

    def remove(self, item: FileSystemItem):
        self.children.remove(item)

    def show(self, indent: int = 0):
        print(" " * indent + f"Folder: {self.name}")
        for child in self.children:
            child.show(indent + 2)


file1 = File("resume.pdf")
file2 = File("photo.png")
file3 = File("notes.txt")

personal_folder = Folder("Personal")
personal_folder.add(file1)
personal_folder.add(file2)

work_folder = Folder("Work")
work_folder.add(file3)

root_folder = Folder("Root")
root_folder.add(personal_folder)
root_folder.add(work_folder)

root_folder.show()
