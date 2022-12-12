from pathlib import Path
from typing import Tuple, Type, Union

from expycted.internals.base import BaseExpectation
from expycted.internals.utils import assertion, hidetraceback


class File:
    pass


class Folder:
    pass


class Directory(BaseExpectation):
    _ASSERTION_MESSAGES = {
        "contain": "Expected {expected} to contain {actual}",
        "contain_file": "Expected {expected} to contain file {actual}",
        "contain_folder": "Expected {expected} to contain folder {actual}",
        "exist": "Expected {expected} to exist",
        "be_empty": "Expected {expected} to be empty",
    }

    def __init__(self, expected: Union[str, Path]):
        super().__init__(self._normalize(expected))

    @staticmethod
    def _normalize(value: Union[str, Path]) -> Path:
        if not isinstance(value, (str, Path)):
            raise AssertionError(f"Expected a string or Path, got a {type(value)}")

        return Path(value)

    def _internal_contain(
        self,
        actual: str,
        type_: Union[Type[File], Type[Folder], None, str] = None,
    ) -> Tuple[bool, str]:
        name = self.expected.joinpath(self._normalize(actual))

        if type_ == File or str(type_).lower() == "file":
            return name.is_file(), self._message("contain_file", name)

        if type_ == Folder or str(type_).lower() == "folder":
            return name.is_dir(), self._message("contain_folder", name)

        return name.exists(), self._message("contain", name)

    def _internal_exist(self) -> Tuple[bool, str]:
        return self.expected.exists(), self._message("exist")

    def _internal_be_empty(self) -> Tuple[bool, str]:
        return not any(self.expected.iterdir()), self._message("be_empty")

    @assertion
    def contain(
        self,
        actual: str,
        type_: Union[Type[File], Type[Folder], None, str] = None,
    ) -> None:
        """
        Check if folder contains something with given name
        """

    @hidetraceback
    def contain_file(self, actual: str) -> None:
        """
        Check if folder contains file with given name
        """
        return self.contain(actual, type_=File)

    @hidetraceback
    def contain_folder(self, actual: str) -> None:
        """
        Check if folder contains folder with given name
        """
        return self.contain(actual, type_=Folder)

    @assertion
    def exist(self) -> None:
        """
        Check if folder exists
        """

    @assertion
    def be_empty(self) -> None:
        """
        Check if folder is empty
        """
