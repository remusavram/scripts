'''
Created on Dec 16, 2014

@author: remusav
'''

from phonebook import Phonebook
import pytest

@pytest.fixture
def phonebook(tmpdir):
    "Provides an empty Phonebook"
    phonebook = Phonebook(tmpdir)
    return phonebook

def test_add_and_look_entry(phonebook):
    pytest.skip("WIP")
    phonebook = Phonebook()
    phonebook.add("Bob", "123")
    assert "123" == phonebook.lookup("Bob")
    
def test_phonebook_gives_access_to_names_and_numbers(phonebook):
    phonebook = Phonebook()
    phonebook.add("Alice", "12345")
    assert "Alice" in phonebook.names()
    assert "12345" in phonebook.numbers()

def test_missing_entry_raises_KeyError(phonebook):
    phonebook = Phonebook()
    with pytest.raises(KeyError):
        phonebook.lookup("missing")