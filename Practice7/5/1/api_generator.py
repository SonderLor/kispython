import inspect
import matplotlib
import example


def create_doc(module):
    with open(f"{module.__name__}.md", "w") as f:
        f.write(f'# Модуль {module.__name__}' + '\n')
        f.write(module.__doc__)

        for key, class_ in inspect.getmembers(module, inspect.isclass):
            f.write(f'## Класс {key}' + '\n')
            if class_.__doc__ is not None:
                f.write(class_.__doc__.strip() + '\n')

            for name, func in inspect.getmembers(class_, inspect.isfunction):
                if func.__doc__ is not None:
                    try:
                        func_notation = inspect.getsource(func).split("\n")[0].strip()[4:-1]
                        f.write(f'* **Метод** `{func_notation}`' + '\n')
                        f.write(func.__doc__.strip() + '\n')
                    except OSError:
                        pass

        for name, func in inspect.getmembers(module, inspect.isfunction):
            if func.__doc__ is not None:
                f.write(f'## Функция {name}' + '\n')
                try:
                    func_notation = inspect.getsource(func).split("\n")[0].strip()[4:-1]
                    f.write(f'Сигнатура: `{func_notation}`' + '\n')
                    f.write(func.__doc__.strip())
                except OSError:
                    pass


if __name__ == "__main__":
    create_doc(matplotlib)
