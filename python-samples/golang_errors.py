# pattern for using golang style errors in "typed" python

import typing as t
import abc


class Error(abc.ABC):
    @abc.abstractmethod
    def error(self) -> str:
        pass


class MyError(Error):
    def error(self) -> str:
        return "smells like go spirit"


T = t.TypeVar("T")

ValueOrError = t.Union[T, Error]


def get_string(my_string: str) -> ValueOrError[str]:
    if my_string == "":
        return MyError()
    return my_string


def get_int(my_int: int) -> ValueOrError[int]:
    if my_int == 0:
        return MyError()
    return my_int


s = get_string("goodbye exceptions!")
if isinstance(s, Error):
    raise Exception(s.error())

print(s.split(" "))

# $ mypy errors.py
# Success: no issues found in 1 source file

# $ python .tmp/play7.py
# ['goodbye', 'exceptions!']



