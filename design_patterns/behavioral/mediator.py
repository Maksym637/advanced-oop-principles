from abc import ABC, abstractmethod


class ChatMediator(ABC):
    @abstractmethod
    def show_message(self, user, message):
        pass


class ChatRoom(ChatMediator):
    def show_message(self, user, message):
        print(f"[{user.name}] says: {message}")


class User:
    def __init__(self, name, mediator: ChatMediator):
        self.name = name
        self.mediator = mediator

    def send(self, message):
        self.mediator.show_message(self, message)


chatroom = ChatRoom()

user_1 = User("Alice", chatroom)
user_2 = User("Bob", chatroom)

user_1.send("Hi Bob!")
user_2.send("Hey Alice, how's it going?")
