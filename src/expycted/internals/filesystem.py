from pathlib import Path
from typing import Tuple, Type, Union

from expycted.internals.utils import assertion, hidetraceback
from expycted.internals.base import BaseExpectation


class File:
    pass


class Folder:
    pass


class Directory(BaseExpectation):
    _ASSERTION_MESSAGES = {
        "contain": "Expected {value1} to contain {value2}",
        "contain_file": "Expected {value1} to contain file {value2}",
        "contain_folder": "Expected {value1} to contain folder {value2}",
        "exist": "Expected {value1} to exist",
        "be_empty": "Expected {value1} to be empty",
    }

    def __init__(self, value: Union[str, Path]):
        super().__init__(self._normalize(value))

    @staticmethod
    def _normalize(value: Union[str, Path]) -> Path:
        if not isinstance(value, (str, Path)):
            raise AssertionError(f"Expected a string or Path, got a {type(value)}")

        return Path(value)

    def _internal_contain(
            self,
            name: str,
            type_: Union[Type[File], Type[Folder], None, str] = None
    ) -> Tuple[bool, str]:
        name = self.value.joinpath(self._normalize(name))

        if type_ == File or str(type_).lower() == "file":
            return name.is_file(), self._message("contain_file", name)

        if type_ == Folder or str(type_).lower() == "folder":
            return name.is_dir(), self._message("contain_folder", name)

        return name.exists(), self._message("contain", name)

    def _internal_exist(self) -> Tuple[bool, str]:
        return self.value.exists(), self._message("exist")

    def _internal_be_empty(self) -> Tuple[bool, str]:
        return not any(self.value.iterdir()), self._message("be_empty")

    @assertion
    def contain(
            self,
            name: str,
            type_: Union[Type[File], Type[Folder], None, str] = None
    ) -> None:
        """
        Check if folder contains something with given name
        """

    @hidetraceback
    def contain_file(self, name: str) -> None:
        """
        Check if folder contains file with given name
        """
        return self.contain(name, type_=File)

    @hidetraceback
    def contain_folder(self, name: str) -> None:
        """
        Check if folder contains folder with given name
        """
        return self.contain(name, type_=Folder)

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
