def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class MyClass:
    def __init__(self):
        self.data = "My Unique Class"


my_class_1 = MyClass()
my_class_2 = MyClass()

print(my_class_1 is my_class_2)
