import os.path

def make_file():
    open("file.txt", 'w')

def test_make_file():
    make_file()
    assert os.path.exists("file.txt") == True
