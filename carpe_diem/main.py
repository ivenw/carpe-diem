from dataclasses import dataclass, field
from os import PathLike
from typing import Any, Protocol
import tomllib
from carpe_diem.markup import *


class Html:
    @staticmethod
    def list(s: str) -> str:
        return f"<li>{s}</li>"


@dataclass
class Block(Protocol):
    block_title: str
    content: str

    def build(self) -> str:
        ...


@dataclass
class ListBlock:
    block_title: str
    content: list[str] = field(default_factory=list)

    def build(self) -> str:
        content = "".join(self.content)
        css_class = self.block_title.lower().replace(" ", "-")
        return title(self.block_title) + h_bar() + u_list(content)


def load_toml(file_path: str | PathLike) -> dict[str, Any]:
    with open(file_path, "rb") as f:
        return tomllib.load(f)


def parse_contact(cv_data: dict[str, Any]):
    contact_info = []
    for key, value in cv_data["contact"].items():
        if isinstance(value, dict):
            contact_info.append(item(link(value["text"], value["url"]), id=key))
        else:
            contact_info.append(item(value, id=key))

    return ListBlock("Contact", contact_info).build()


if __name__ == "__main__":
    cv_data = load_toml("demo/cv.toml")
    print(prettify(parse_contact(cv_data)))
