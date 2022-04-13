import os
from typing import Tuple, Type, Union

from expycted.internals.utils import to_not_fn

assertion_texts = {
    "contain": "Expected {value1} to contain {value2}",
    "contain_file": "Expected {value1} to contain file {value2}",
    "contain_folder": "Expected {value1} to contain folder {value2}",
    "exist": "Expected {value1} to exist",
    "be_empty": "Expected {value1} to be empty",
}


class File:
    pass


class Folder:
    pass


class Directory:
    def __init__(self, path: str):
        self.to = To(path)
        self.to_not = ToNot(path)


def check_stringiness(param):
    if not isinstance(param, str):
        raise AssertionError("Expected a string, got a {}".format(type(param)))


class To:
    def __init__(self, path: str):
        self.path = path
        check_stringiness(self.path)

    def _internal_contain(
        self, name: str, type: Union[Type[File], Type[Folder], None, str] = None
    ) -> Tuple[bool, str]:
        check_stringiness(name)
        if type == File or str(type).lower() == "file":
            return os.path.isfile(os.path.join(self.path, name)), assertion_texts[
                "contain_file"
            ].format(value1=self.path, value2=name)

        elif type == Folder or str(type).lower() == "folder":
            return os.path.isdir(os.path.join(self.path, name)), assertion_texts[
                "contain_folder"
            ].format(value1=self.path, value2=name)

        else:
            return os.path.exists(os.path.join(self.path, name)), assertion_texts[
                "contain"
            ].format(value1=self.path, value2=name)

    def _internal_contain_file(self, name: str) -> Tuple[bool, str]:
        return self._internal_contain(name, type=File)

    def _internal_contain_folder(self, name: str) -> Tuple[bool, str]:
        return self._internal_contain(name, type=Folder)

    def _internal_exist(self) -> Tuple[bool, str]:
        return os.path.exists(self.path), assertion_texts["exist"].format(
            value1=self.path
        )

    def _internal_be_empty(self) -> Tuple[bool, str]:
        return os.listdir(self.path) == [], assertion_texts["be_empty"].format(
            value1=self.path
        )

    def contain(
        self, name: str, type: Union[Type[File], Type[Folder], None, str] = None
    ) -> None:
        """
        Check if folder contains something with given name
        """
        res = self._internal_contain(name, type)
        assert res[0], res[1]

    def contain_file(self, name: str) -> None:
        """
        Check if folder contains file with given name
        """
        res = self._internal_contain_file(name)
        assert res[0], res[1]

    def contain_folder(self, name: str) -> None:
        """
        Check if folder contains folder with given name
        """
        res = self._internal_contain_folder(name)
        assert res[0], res[1]

    def exist(self) -> None:
        """
        Check if folder exists
        """
        res = self._internal_exist()
        assert res[0], res[1]

    def be_empty(self) -> None:
        """
        Check if folder is empty
        """
        res = self._internal_be_empty()
        assert res[0], res[1]


class ToNot(To):
    def __init__(self, path: str):
        super().__init__(path)
        to = To(path)
        for i in list(filter(lambda x: x.startswith("_internal_"), dir(to))):
            expect_method = getattr(to, i)
            self.__setattr__(i.replace("_internal_", ""), to_not_fn(expect_method))
