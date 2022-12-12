from pathlib import Path

import pytest

from expycted import expect
from helpers.utils import expected_params


@pytest.fixture(name="directory")
def get_test_directory(tmp_path):
    tmp_path.joinpath("test_file.txt").write_text("test")
    tmp_path.joinpath("test_file2.txt").write_text("test")

    return tmp_path


@pytest.fixture(name="empty_directory")
def get_empty_test_directory(tmp_path):
    tmp_path.joinpath("empty").mkdir()

    return tmp_path.joinpath("empty")


@pytest.fixture(name="with_subdirectory")
def get_test_directory_with_subdirectory(tmp_path):
    tmp_path.joinpath("subdirectory").mkdir()

    return tmp_path


def test_to_contain(directory, with_subdirectory, context):
    expect.folder(with_subdirectory).to.contain("subdirectory")
    expect.folder(directory).to.contain("test_file.txt")
    expect.folder(directory).to.contain("test_file2.txt")
    expect.folder(directory).to_not.contain("test_file3.txt")

    with context.raises:
        expect.folder(with_subdirectory).to_not.contain("subdirectory")

    with context.raises:
        expect.folder(directory).to_not.contain("test_file.txt")

    with context.raises:
        expect.folder(directory).to_not.contain("test_file2.txt")

    with context.raises:
        expect.folder(directory).to.contain("test_file3.txt")


def test_to_contain_file(directory, context):
    expect.folder(directory).to.contain_file("test_file.txt")
    expect.folder(directory).to.contain_file("test_file2.txt")
    expect.folder(directory).to_not.contain_file("test_file3.txt")

    with context.raises:
        expect.folder(directory).to_not.contain_file("test_file.txt")

    with context.raises:
        expect.folder(directory).to_not.contain_file("test_file2.txt")

    with context.raises:
        expect.folder(directory).to.contain_file("test_file3.txt")


def test_to_be_empty(directory, empty_directory, with_subdirectory, context):
    expect.folder(empty_directory).to.be_empty()
    expect.folder(with_subdirectory).to_not.be_empty()
    expect.folder(directory).to_not.be_empty()

    with context.raises:
        expect.folder(empty_directory).to_not.be_empty()

    with context.raises:
        expect.folder(with_subdirectory).to.be_empty()

    with context.raises:
        expect.folder(directory).to.be_empty()


def test_to_contain_folder(with_subdirectory, empty_directory, context):
    expect.folder(with_subdirectory).to.contain_folder("subdirectory")
    expect.folder(empty_directory).to_not.contain_folder("subdirectory")

    with context.raises:
        expect.folder(with_subdirectory).to_not.contain_folder("subdirectory")

    with context.raises:
        expect.folder(empty_directory).to.contain_folder("subdirectory")


def test_to_exist(directory, context):
    expect.folder(directory).to.exist()
    expect.folder("absolutely_not_existing_folder").to_not.exist()

    with context.raises:
        expect.folder(directory).to_not.exist()

    with context.raises:
        expect.folder("absolutely_not_existing_folder").to.exist()


@expected_params([1, 2, {}, []], extract_ids=False)
def test_passing_wrong_types(expected, context):
    with context.raises:
        expect.folder(expected).to.exist()

    with context.raises:
        expect.folder(expected).to_not.exist()


def test_path_object_type(directory):
    expect.folder(directory).to.contain(Path("test_file.txt"))
