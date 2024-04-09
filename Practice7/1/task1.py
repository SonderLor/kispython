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
        self.__private_method()

    def _protected_method(self):
        print("This is a protected method")

    def __private_method(self):
        print("This is a private method")

    def __len__(self):
        return 0


def get_names(obj):
    return [name for name in vars(obj).keys() if not (name[:2] == "__" and name[-2:] == "__")]


if __name__ == "__main__":
    print(get_names(MyClass))
