from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def publish(self, context):
        pass

    @abstractmethod
    def reject(self, context):
        pass


class DraftState(State):
    def publish(self, context):
        print("Document is now under review.")
        context.set_state(ModerationState())

    def reject(self, context):
        print("Draft rejected. No further action.")


class ModerationState(State):
    def publish(self, context):
        print("Document has been published.")
        context.set_state(PublishedState())

    def reject(self, context):
        print("Document rejected. Going back to draft.")
        context.set_state(DraftState())


class PublishedState(State):
    def publish(self, context):
        print("Document is already published. No action taken.")

    def reject(self, context):
        print("Published document cannot be rejected.")


class Document:
    def __init__(self):
        self._state = DraftState()

    def set_state(self, state):
        self._state = state

    def publish(self):
        self._state.publish(self)

    def reject(self):
        self._state.reject(self)


document = Document()

document.publish()
document.publish()
document.reject()
