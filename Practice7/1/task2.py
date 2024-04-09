class MyClass:
    public_field = 0
    _protected_field = 0
    __private_field = 0

    def __init__(self, field1, field2, field3):
        self.public_field = field1
        self._protected_field = field2
        self.__private_field = field3

    def public_method(self):
        print("This is a public method")

    def _protected_method(self):
        print("This is a protected method")

    def __private_method(self):
        print("This is a private method")

    def __len__(self):
        return 0


def call_method(obj, method_name: str):
    return getattr(obj, method_name)()


if __name__ == "__main__":
    cls = MyClass(1, 2, 3)
    call_method(cls, "public_method")
