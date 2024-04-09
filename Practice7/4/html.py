from contextlib import contextmanager
from typing import Iterator


class HTML:
    def __init__(self):
        self.tabs = 0

    @contextmanager
    def body(self) -> Iterator[None]:
        print(self.tabs * "\t" + "<body>")
        self.tabs += 1
        yield
        self.tabs -= 1
        print(self.tabs * "\t" + "</body>")

    @contextmanager
    def div(self) -> Iterator[None]:
        print(self.tabs * "\t" + "<div>")
        self.tabs += 1
        yield
        self.tabs -= 1
        print(self.tabs * "\t" + "</div>")

    def p(self, text: str) -> None:
        print(self.tabs * "\t" + "<p>")
        self.tabs += 1
        print(self.tabs * "\t" + text)
        self.tabs -= 1
        print(self.tabs * "\t" + "</p>")


html = HTML()
with html.body():
    with html.div():
        with html.div():
            html.p('Первая строка.')
            html.p('Вторая строка.')
        with html.div():
            html.p('Третья строка.')
