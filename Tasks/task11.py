class MealyError(Exception):
    pass


class StateMachine:
    def __init__(self):
        self.state = "A"

    def herd(self):
        if self.state == "A":
            self.state = "B"
            return 0
        if self.state == "B":
            self.state = "C"
            return 2
        if self.state == "C":
            self.state = "D"
            return 4
        if self.state == "D":
            self.state = "E"
            return 5
        if self.state == "E":
            self.state = "F"
            return 7
        raise MealyError("herd")

    def drag(self):
        if self.state == "A":
            self.state = "D"
            return 1
        if self.state == "B":
            self.state = "E"
            return 3
        if self.state == "E":
            self.state = "E"
            return 8
        if self.state == "D":
            self.state = "G"
            return 6
        if self.state == "F":
            self.state = "G"
            return 9
        raise MealyError("drag")


def main():
    return StateMachine()


def raises(func, error):
    output = None
    try:
        output = func()
    except Exception as e:
        assert type(e) is error
    assert output is None


def test():
    o = main()
    assert o.herd() == 0
    assert o.herd() == 2
    raises(lambda: o.drag(), MealyError)
    assert o.herd() == 4
    assert o.herd() == 5
    assert o.herd() == 7
    raises(lambda: o.herd(), MealyError)
    assert o.drag() == 9
    o = main()
    assert o.drag() == 1
    assert o.drag() == 6
    raises(lambda: o.drag(), MealyError)
    raises(lambda: o.herd(), MealyError)
    o = main()
    assert o.herd() == 0
    assert o.drag() == 3
    assert o.drag() == 8


if __name__ == "__main__":
    test()
