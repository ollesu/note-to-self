import typing
from abc import abstractmethod

Key = typing.TypeVar("Key")
Value = typing.TypeVar("Value")


class KafkaRecord(typing.Generic[Key, Value]):
    def __init__(self, key: Key, value: Value) -> None:
        self.key = key
        self.value = value


class KafkaConsumer(typing.Generic[Key, Value]):
    @abstractmethod
    def pull(self) -> KafkaRecord[Key, Value]:
        raise NotImplementedError


class _Implementation1(KafkaConsumer[Key, Value]):
    def __init__(
        self,
        deserialize_key: typing.Callable[[bytes], Key],
        deserialize_value: typing.Callable[[bytes], Value],
    ) -> None:
        self.deserialize_key = deserialize_key
        self.deserialize_value = deserialize_value

    def pull(self) -> KafkaRecord[Key, Value]:
        return KafkaRecord[Key, Value](
            key=self.deserialize_key(b""), value=self.deserialize_value(b"")
        )


def bytes_to_str(b: bytes) -> str:
    return ""


def bytes_to_int(b: bytes) -> int:
    return 0


def pull_from_consumer(c: KafkaConsumer[str, str]) -> None:
    c.pull()


# run mypy
if __name__ == "__main__":
    pull_from_consumer(_Implementation1[str, str](bytes_to_str, bytes_to_str))
    # ok

    pull_from_consumer(_Implementation1[str, int](bytes_to_str, bytes_to_int))
    # play.py:42: error: Argument 1 to "pull_from_consumer" has incompatible type "_Implementation[str, int]"; expected "KafkaConsumer[str, str]"

