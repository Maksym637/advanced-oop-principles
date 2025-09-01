# Memento
class EditorMemento:
    def __init__(self, content):
        self._content = content

    def get_saved_content(self):
        return self._content


# Originator
class TextEditor:
    def __init__(self):
        self._content = ""

    def write(self, text):
        self._content += text

    def get_content(self):
        return self._content

    def save(self):
        return EditorMemento(self._content)

    def restore(self, memento: EditorMemento):
        self._content = memento.get_saved_content()


#
# Caretaker
# Manages the history of mementos
#
class History:
    def __init__(self):
        self._mementos = []

    def save_state(self, memento):
        self._mementos.append(memento)

    def undo(self):
        if not self._mementos:
            return None
        return self._mementos.pop()


editor = TextEditor()
history = History()

editor.write("Hello")
history.save_state(editor.save())

editor.write(" World")
history.save_state(editor.save())

editor.write("!")
print(f"Current content: {editor.get_content()}")

editor.restore(history.undo())
print(f"Current content: {editor.get_content()}")

editor.restore(history.undo())
print(f"Current content: {editor.get_content()}")
