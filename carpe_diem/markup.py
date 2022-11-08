from typing import Optional
from bs4 import BeautifulSoup


class Markup:
    def __init__(self, s: str, /):
        self.s = s


def tag(
    s: str, t: str, /, *, cl: Optional[str] = None, id: Optional[str] = None, **kwargs
) -> str:
    html_string = f"<{t}"
    if cl:
        html_string += f" class={cl}"
    if id:
        html_string += f" id={id}"
    for k, v in kwargs.items():
        html_string += f" {k}={v}"

    return f"{html_string}>{s}</{t}>"


def column(s: str, /) -> str:
    return tag(s, "div", cl="column")


def container(s: str, /) -> str:
    return tag(s, "div", cl="container")


def u_list(s: str, /) -> str:
    return tag(s, "ul", cl="list")


def title(s: str, /) -> str:
    return tag(s, "h2", cl="title")


def h_bar() -> str:
    return "<hr>"


def item(s: str, /, **kwargs) -> str:
    return tag(s, "li", cl="item", **kwargs)


def link(s, /, url: str) -> str:
    return tag(s, "a", href=url)


def prettify(s, /) -> str:
    return BeautifulSoup(s, "html.parser").prettify()
