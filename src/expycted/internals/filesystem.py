import os
from typing import Union

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
        raise AssertionError('Expected a string, got a {}'.format(type(param)))
        

class To:
    def __init__(self, path: str):
        self.path = path
        check_stringiness(self.path)
    
    def _contain(self, name: str, type: Union[File, Folder, None, str]):
        check_stringiness(name)
        if type==File or str(type).lower() == 'file': 
            return os.path.isfile(os.path.join(self.path, name))
            
        elif type==Folder or str(type).lower() == 'folder':
            return os.path.isdir(os.path.join(self.path, name))
            
        else:
            return os.path.exists(os.path.join(self.path, name))
                    
    def _contain_file(self, name: str):
        return self._contain(name, type=File)
        
    def _contain_folder(self, name: str):
        return self._contain(name, type=Folder)
        
    def _exist(self):
        return os.path.exists(self.path)
        
    def _be_empty(self):
        return os.listdir(self.path) == []
    
    def contain(self, name: str, type: Union[File, Folder, None, str] = None):
        """
        Check if folder contains something with given name
        """
        assert self._contain(name, type)
    
    def contain_file(self, name: str):
        """
        Check if folder contains file with given name
        """
        assert self._contain_file(name)
    
    def contain_folder(self, name: str):
        """
        Check if folder contains folder with given name
        """
        assert self._contain_folder(name)
        
    def exist(self):
        """
        Check if folder exists
        """
        assert self._exist()
        
    def be_empty(self):
        """
        Check if folder is empty
        """
        assert self._be_empty()

class ToNot(To):
        
    def contain(self, name: str, type: Union[File, Folder, None, str] = None):
        """
        Check that folder does not contain anything with given name
        """
        assert not super()._contain(name, type)
        
    def contain_file(self, name: str):
        """
        Check that folder does not contain file with given name
        """
        assert not super()._contain_file(name)
    
    def contain_folder(self, name: str):
        """
        Check that folder does not contain folder with given name
        """        
        assert not super()._contain_folder(name)
    
    def exist(self):
        """
        Check that folder does not exist
        """
        assert not super()._exist()
    
    def be_empty(self):
        """
        Check that folder is not empty
        """
        assert not super()._be_empty()