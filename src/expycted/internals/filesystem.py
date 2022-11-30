import os
from typing import Tuple, Type, Union

from expycted.internals.utils import assertion
from expycted.internals.base import BaseExpectation


class File:
    pass


class Folder:
    pass


def check_stringiness(param):
    if not isinstance(param, str):
        raise AssertionError(f"Expected a string, got a {type(param)}")


class Directory(BaseExpectation):
    _ASSERTION_MESSAGES = {
        "contain": "Expected {value1} to contain {value2}",
        "contain_file": "Expected {value1} to contain file {value2}",
        "contain_folder": "Expected {value1} to contain folder {value2}",
        "exist": "Expected {value1} to exist",
        "be_empty": "Expected {value1} to be empty",
    }

    def __init__(self, value: str):
        super().__init__(value)
        check_stringiness(self.value)

    def _internal_contain(
        self, name: str, type: Union[Type[File], Type[Folder], None, str] = None
    ) -> Tuple[bool, str]:
        check_stringiness(name)
        if type == File or str(type).lower() == "file":
            return os.path.isfile(os.path.join(self.value, name)), self._message("contain_file", name)

        if type == Folder or str(type).lower() == "folder":
            return os.path.isdir(os.path.join(self.value, name)), self._message("contain_folder", name)

        return os.path.exists(os.path.join(self.value, name)), self._message("contain", name)

    def _internal_contain_file(self, name: str) -> Tuple[bool, str]:
        return self._internal_contain(name, type=File)

    def _internal_contain_folder(self, name: str) -> Tuple[bool, str]:
        return self._internal_contain(name, type=Folder)

    def _internal_exist(self) -> Tuple[bool, str]:
        return os.path.exists(self.value), self._message("exist")

    def _internal_be_empty(self) -> Tuple[bool, str]:
        return os.listdir(self.value) == [], self._message("be_empty")

    @assertion
    def contain(
        self, name: str, type: Union[Type[File], Type[Folder], None, str] = None
    ) -> None:
        """
        Check if folder contains something with given name
        """
        pass

    @assertion
    def contain_file(self, name: str) -> None:
        """
        Check if folder contains file with given name
        """
        pass

    @assertion
    def contain_folder(self, name: str) -> None:
        """
        Check if folder contains folder with given name
        """
        pass

    @assertion
    def exist(self) -> None:
        """
        Check if folder exists
        """
        pass

    @assertion
    def be_empty(self) -> None:
        """
        Check if folder is empty
        """
        pass
