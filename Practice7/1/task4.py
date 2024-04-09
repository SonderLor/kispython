def get_inheritance(cls):
    if cls.__name__ == "object":
        return 'object'
    return ' -> '.join([cls.__name__] + get_inheritance(cls.__base__).split(' -> '))


if __name__ == "__main__":
    print(get_inheritance(OSError))
