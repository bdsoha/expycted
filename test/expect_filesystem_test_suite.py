from expycted import expect
import pytest

import os
import shutil

@pytest.fixture
def get_test_directory():
    os.mkdir('test_directory')
    with open('test_directory/test_file.txt', 'w') as f:
        f.write('test')
        
    with open('test_directory/test_file2.txt', 'w') as f:
        f.write('test')
        
    yield 'test_directory'
    
    shutil.rmtree('test_directory')
        
@pytest.fixture
def get_empty_test_directory():
    os.mkdir('empty_test_directory')
    
    yield 'empty_test_directory'
    
    shutil.rmtree('empty_test_directory')
    
@pytest.fixture
def get_test_directory_with_subdirectory():
    os.mkdir('test_directory')
    os.mkdir('test_directory/subdirectory')
    yield 'test_directory'
    shutil.rmtree('test_directory')
    
    
def test_to_contain_file(get_test_directory):
    expect.folder(get_test_directory).to.contain_file('test_file.txt')
    
def test_to_contain_file_failing(get_test_directory):
    with pytest.raises(AssertionError):
        expect.folder(get_test_directory).to.contain_file('test_file3.txt')

def test_to_not_be_empty(get_test_directory):
    expect.folder(get_test_directory).to_not.be_empty()
    
def test_to_not_be_empty_failing(get_empty_test_directory):
    with pytest.raises(AssertionError):
        expect.folder(get_empty_test_directory).to_not.be_empty()
    
def test_to_not_contain_file(get_test_directory):
    expect.folder(get_test_directory).to_not.contain_file('test_file3.txt')
    
def test_to_not_contain_file_failing(get_test_directory):
    with pytest.raises(AssertionError):
        expect.folder(get_test_directory).to_not.contain_file('test_file.txt')
    
def test_to_contain_file_failing(get_empty_test_directory):
    with pytest.raises(AssertionError):
        expect.folder(get_empty_test_directory).to.contain_file('test_file3.txt')
 
def test_to_be_empty(get_empty_test_directory):
    expect.folder(get_empty_test_directory).to.be_empty()
    
def test_to_be_empty_failing(get_test_directory):
    with pytest.raises(AssertionError):
        expect.folder(get_test_directory).to.be_empty()
        
def test_to_not_be_empty(get_test_directory):
    expect.folder(get_test_directory).to_not.be_empty()
    
def test_to_not_be_empty_failing(get_empty_test_directory):
    with pytest.raises(AssertionError):
        expect.folder(get_empty_test_directory).to_not.be_empty()
        
def test_to_contain_subfolder(get_test_directory_with_subdirectory):
    expect.folder(get_test_directory_with_subdirectory).to.contain_folder('subdirectory')
    
def test_to_contain_subfolder_failing(get_test_directory):
    with pytest.raises(AssertionError):
        expect.folder(get_test_directory).to.contain_folder('subdirectory2')
    
def test_to_not_contain_subfolder(get_test_directory_with_subdirectory):
    expect.folder(get_test_directory_with_subdirectory).to_not.contain_folder('subdirectory2')

def test_to_not_contain_subfolder_failing(get_test_directory_with_subdirectory):
    with pytest.raises(AssertionError):
        expect.folder(get_test_directory_with_subdirectory).to_not.contain_folder('subdirectory')
    
def test_to_contain_not_provided_what(get_test_directory):
    expect.folder(get_test_directory).to.contain('test_file.txt')

def test_to_contain_not_provided_what_failing(get_test_directory):
    with pytest.raises(AssertionError):
        expect.folder(get_test_directory).to.contain('test_file3.txt')
    
def test_to_not_contain_not_provided_what(get_test_directory):
    expect.folder(get_test_directory).to_not.contain('test_file3.txt')
    
def test_to_not_contain_not_provided_what_failing(get_test_directory):
    with pytest.raises(AssertionError):
        expect.folder(get_test_directory).to_not.contain('test_file2.txt')
    
def test_to_exist(get_test_directory):
    expect.folder(get_test_directory).to.exist()
    
def test_to_not_exist(get_empty_test_directory):
    expect.folder('absolutely_not_existing_folder').to_not.exist()
    
def test_to_not_exist_failing(get_test_directory):
    with pytest.raises(AssertionError):
        expect.folder(get_test_directory).to_not.exist()
    
def test_to_exist_failing():
    with pytest.raises(AssertionError):
        expect.folder('absolutely_not_existing_folder').to.exist()

@pytest.mark.parametrize('name', [1, 2, {}, []])
def test_passing_wrong_things(name):
    with pytest.raises(AssertionError):
        expect.folder(name).to.exist()
    


    